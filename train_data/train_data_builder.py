import random

from tqdm import tqdm
from transformers import RobertaTokenizer

from data_io.file_io import *
from go_tree_sitter.go_parser import GoParser
from go_tree_sitter.go_tree_sitter_tool import GoTreeSitterTool


class TrainDataBuilder:

    def __init__(self, src_path, dst_path):
        self.src_path = src_path
        self.dst_path = dst_path

        self.parser = GoParser()

        self.MAX_INPUT_TOKEN_LEN = 512
        self.MAX_OUTPUT_TOKEN_LEN = 256

        self.tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-small', cache_dir="D:\huggingface_cache")

    def get_token_num(self, code):
        return len(self.tokenizer(code, return_tensors="pt").input_ids[0])

    def build(self):
        print(f"{'=' * 20} start building train data {'=' * 20}")
        shuffle_list = []
        for src_line in tqdm(data_from_jsonl(self.src_path)):
            src_code = src_line["code"]
            root_node = self.parser.parse(src_code)

            functions = GoTreeSitterTool.get_function_declaration(root_node)
            for function in functions:
                function_code = function.text.decode("utf8")

                function_name = function.child_by_field_name("name").text.decode("utf8")
                if function_name == "main":
                    continue

                function_body = function.child_by_field_name("body")
                if function_body is None:
                    continue
                else:
                    function_body = function_body.text.decode("utf8")
                    if len(function_body[1:-1].strip()) == 0:
                        continue

                function_signature = function_code.replace(function_body, "")

                prompt = src_code.replace(function_code, "") + "\n\n" + function_signature
                ground_truth = function_body

                if self.get_token_num(prompt) <= self.MAX_INPUT_TOKEN_LEN and self.get_token_num(
                        ground_truth) <= self.MAX_OUTPUT_TOKEN_LEN:
                    train_data_line = {"input": prompt, "output": ground_truth}
                    shuffle_list.append(train_data_line)
        random.shuffle(shuffle_list)

        for train_data_line in shuffle_list:
            data_to_jsonl_append(self.dst_path, train_data_line)
