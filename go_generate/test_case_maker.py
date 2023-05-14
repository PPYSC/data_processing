from tqdm import tqdm

from data_io.file_io import data_from_jsonl, data_to_jsonl_append
from filter.internal_import_filter import InternalImportFilter
from filter.undefined_behavior_filter import UndefinedBehaviorFilter
from go_tree_sitter.go_parser import GoParser
from go_tree_sitter.go_tree_sitter_tool import GoTreeSitterTool


class TestCaseMaker:
    def __init__(self, src_path, dst_path, go_generator):
        self.src_path = src_path
        self.dst_path = dst_path

        self.parser = GoParser()

        self.go_generator = go_generator

        self.data_list = []
        self.data_count = 0

    def build_data_list(self):
        self.data_list = []
        for index, src_line in enumerate(data_from_jsonl(self.src_path)):
            src_line["index"] = index
            self.data_list.append(src_line)
        self.data_count = len(self.data_list)

    def do_filter(self, node):
        return GoTreeSitterTool.has_error(node) or \
            UndefinedBehaviorFilter.do_filter(node) or \
            False

    def check(self):
        cnt = 0
        for dst_line in data_from_jsonl(self.dst_path):
            code = dst_line["input"] + dst_line["output"]
            node = self.parser.parse(code)
            if self.do_filter(node):
                cnt += 1
        print(cnt)

    def get_input_text(self):
        input_texts = []
        for src_line in data_from_jsonl(self.src_path):
            input_texts.append(src_line["input"])

        return input_texts

    def generate_test_case(self, count=1):
        input_text_list = self.get_input_text()
        test_case_list = []
        for input_text in tqdm(input_text_list):
            output_text = self.go_generator.generate(input_text)
            test_case = {"input": input_text, "output": output_text}
            test_case_list.append(test_case)
            break

        for test_case_line in test_case_list:
            data_to_jsonl_append(self.dst_path, test_case_line)
