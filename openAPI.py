import openai

# Authenticate with your API key
openai.api_key = 'sk-[XXXXXXXXXXXXXXXXXXXXx]'

# Make a completion request
response = openai.Completion.create(
  model="text-davinci-003",  # or another model of your choice
  prompt="What is the work of a consultant with a magic stick?'",
  max_tokens=60
)

# Print the response
print(response.choices[0].text.strip())
