from transformers import RobertaTokenizer, T5ForConditionalGeneration

tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-base', cache_dir="D:\huggingface_cache")
model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-base', cache_dir="D:\huggingface_cache")

text = """package main

func Add(a, b int) int {
	return a + b
}

func Multi(a, b int) int {
	return a * b
}

func Add_and_Multi(a,b int) {
    
}
"""

input_ids = tokenizer(text, return_tensors="pt").input_ids

# simply generate a single sequence
generated_ids = model.generate(input_ids, max_length=8)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
