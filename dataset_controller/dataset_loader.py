from datasets import load_dataset


class DatasetLoader:

    def __init__(self, is_iter, *args, **kwargs):
        self.dataset = load_dataset(*args, **kwargs)
        if is_iter:
            self.dataset = iter(self.dataset)


''' 

load_dataset(path="codeparrot/github-code-clean", languages=["GO"], split="train",
                                    cache_dir="D:\huggingface_cache", streaming=True)
'''
