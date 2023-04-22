from tqdm import tqdm

from data_io.file_io import *
from filter.internal_import_filter import InternalImportFilter
from go_tree_sitter.go_parser import GoParser
from go_tree_sitter.go_tree_sitter_tool import GoTreeSitterTool
from filter.undefined_behavior_filter import UndefinedBehaviorFilter


class DataProcessor:

    def __init__(self, src_path, dst_path):
        self.src_path = src_path
        self.dst_path = dst_path

        self.parser = GoParser()

        self.MAX_SIZE = 6000

    def do_filter(self, code, node, size):
        return GoTreeSitterTool.has_error(node) or \
            size > self.MAX_SIZE or \
            InternalImportFilter.do_filter(node) or \
            UndefinedBehaviorFilter.do_filter(node) or \
            False

    def delete_all_comment(self, code):
        node = self.parser.parse(code)

        comments = [elem.text.decode("utf8") for elem in GoTreeSitterTool.get_comment(node)]
        comments.sort(key=lambda x: len(x), reverse=True)

        for comment in comments:
            code = code.replace(comment, "")

        rst_code = ""
        for line in code.splitlines():
            if len(line) == 0:
                rst_code = rst_code + line + "\n"
            if len(line.replace("\t", "")) != 0:
                rst_code = rst_code + line + "\n"

        return rst_code.strip()

    def process(self):
        print(f"{'=' * 20} start processing raw data {'=' * 20}")
        pass_cnt = 0
        for src_line in tqdm(data_from_jsonl(self.src_path)):
            src_code = self.delete_all_comment(src_line["code"])
            root_node = self.parser.parse(src_code)

            if not self.do_filter(src_code, root_node, src_line["size"]):
                pass_cnt += 1
                dst_line = {"code": src_code, "size": src_line["size"]}
                data_to_jsonl_append(self.dst_path, dst_line)
        return pass_cnt
