import openai

# OpenAI API kalitingiz
openai.api_key = 'YOUR_API_KEY'

# ChatGPT bilan suhbatlashish funksiyasi
def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # "gpt-3.5-turbo" yoki "gpt-4"dan foydalanishingiz mumkin
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Foydalanuvchi savolini berish
user_prompt = "What is the capital of Uzbekistan?"
gpt_response = chat_with_gpt(user_prompt)

print(gpt_response)
