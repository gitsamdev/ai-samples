from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load pre-trained model and tokenizer
model_name = "facebook/llama"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Function to generate text in a streaming-like manner
def stream_response(prompt, max_length=50, chunk_size=10):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs["input_ids"], max_length=max_length, do_sample=True)

    # Decode and print the output in chunks
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    for i in range(0, len(text), chunk_size):
        print(text[i:i+chunk_size], end='', flush=True)
        time.sleep(0.1)  # Simulate streaming delay

# Example usage
stream_response("In a futuristic city, a young hacker discovered a secret,")
