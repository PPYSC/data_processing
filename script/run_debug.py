import os

from train_data.train_data_builder import TrainDataBuilder

DATA_COUNT = 50

SRC_PATH = f"./output/processed_data/data_{DATA_COUNT}.jsonl"
DST_PATH = f"./output/train_data/data_{DATA_COUNT}.jsonl"

if os.path.isfile(DST_PATH):
    os.remove(DST_PATH)

train_data_builder = TrainDataBuilder(SRC_PATH, DST_PATH)
train_data_builder.build()