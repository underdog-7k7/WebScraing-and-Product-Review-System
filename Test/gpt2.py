import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
model_name = 'gpt2'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
def generate_text(prompt, max_length=100):
    input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
    outputs = model.generate(input_ids, max_length=max_length, num_return_sequences=1)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text
prompt = "Narendra modi is the prime minister of India as of the year 2014, he is one of the most influential persons in the country, before this he was the chief minister of the state of Gujrat"
generated_text = generate_text(prompt)
print(generated_text)
