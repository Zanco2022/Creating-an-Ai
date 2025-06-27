import openai

openai.api_key = 'your-api-key-here'

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are an expert resume writer."},
    {"role": "user", "content": prompt}
  ],
  temperature=0.7
)

custom_resume = response['choices'][0]['message']['content']
print(custom_resume)
