from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load tokenizer and model
model_name = "mistralai/Mistral-7B-Instruct-v0.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")


def generate_prompt(prompt_text, max_length=100, temperature=0.7):  # Set max_length to 100 for faster output
    inputs = tokenizer(prompt_text, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs["input_ids"],
                             max_length=max_length,
                             temperature=temperature,
                             pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# test generate_prompt function
prompt =  "why do lawyers wear suits?"
print(generate_prompt(prompt))
