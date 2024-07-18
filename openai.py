import openai

openai.api_key = "sk-proj-n2sgoyqflSnHU3jPWqlFT3BlbkFJ9oLKSD51U5iPG5zCj0wk"

# Define synthetic data

prompt = [
    ["The cat sat on the", "mat."],
    ["The quick brown fox jumps over the", "lazy dog."],
    ["An apple a day keeps the", "doctor away."],
]

# Fine-tune the model
model = "text-davinci-002"
fine_tuned_model = openai.Completion.create(
    engine=model,
    prompt= prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=1

)

# Test the fine-tuned model
text = "The sun is shining and the"
response = openai.Completion.create(
    engine=model,
    prompt=text,
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5
)
print(response.choices[0].text)