import openai

# OpenAI API kalitini o'rnating
openai.api_key = 'SIZNING_API_KALITINGIZ'

# ChatGPT bilan suxbat qilish
response = openai.Completion.create(
  engine="text-davinci-003",  # Yoki boshqa model, masalan, GPT-4
  prompt="Salom, bugun qanday yordam bera olaman?",
  max_tokens=150
)

# Javobni chop etish
print(response.choices[0].text.strip())
