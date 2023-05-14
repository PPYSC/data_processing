from tqdm import tqdm

from data_io.file_io import data_from_jsonl, data_to_jsonl_append


class TestCaseMaker:
    def __init__(self, src_path, dst_path, go_generator):
        self.src_path = src_path
        self.dst_path = dst_path

        self.go_generator = go_generator

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

        for test_case_line in test_case_list:
            data_to_jsonl_append(self.dst_path, test_case_line)
