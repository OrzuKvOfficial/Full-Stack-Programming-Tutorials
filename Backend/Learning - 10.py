import openai

# OpenAI API kalitingizni qo'shing
openai.api_key = "YOUR_API_KEY"

def ai_calculator(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Hisoblashni bajaring: {prompt}",
            max_tokens=50
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Xato: {e}"

print("AI Kalkulyator: Foydalanuvchi so'rovlarini tahlil qiladi va natijani qaytaradi.")
while True:
    user_input = input("Kirish (yoki 'chiqish' deb yozing): ")
    if user_input.lower() == "chiqish":
        break
    print(ai_calculator(user_input))
