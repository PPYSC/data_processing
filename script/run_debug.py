import torch

from go_generate.go_generator import GoGenerator
from go_generate.test_case_maker import TestCaseMaker

MODEL_PATH = "PPY039/codet5-small-go_generation_v2"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
CACHE_DIR = "D:\huggingface_cache"

go_generator = GoGenerator(MODEL_PATH, DEVICE, CACHE_DIR)

DATA_COUNT = 71421
SRC_PATH = f"./output/split_train_data/data_{DATA_COUNT}/test.jsonl"
DST_PATH = f"./output/test_case/data_{DATA_COUNT}.jsonl"

test_case_maker = TestCaseMaker(SRC_PATH, DST_PATH, go_generator)

test_case_maker.check()