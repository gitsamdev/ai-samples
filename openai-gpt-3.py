import openai

openai.api_key = 'YOUR_API_KEY'

# Streaming callback function
def stream_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        stream=True  # Enable streaming
    )
    for chunk in response:
        if chunk.choices[0].text:
            print(chunk.choices[0].text, end='', flush=True)

# Example usage
stream_response("Tell me a story about a robot learning to love.")
