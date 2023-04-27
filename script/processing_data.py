import os

from data_processor.data_processor import DataProcessor

DATA_COUNT = 30000

SRC_PATH = f"./output/raw_data/data_{DATA_COUNT}.jsonl"
DST_PATH = f"./output/processed_data/data_{DATA_COUNT}.jsonl"

if os.path.isfile(DST_PATH):
    os.remove(DST_PATH)

data_processor = DataProcessor(SRC_PATH, DST_PATH)
pass_cnt = data_processor.process()

print(f"Pass: {pass_cnt}/{DATA_COUNT}")
