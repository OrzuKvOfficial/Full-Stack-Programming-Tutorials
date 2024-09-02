import openai

# OpenAI API kalitingizni kiriting
openai.api_key = "YOUR_API_KEY"

def ai_yordamchi(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Yoki boshqa mavjud model nomini kiriting
        prompt=user_input,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

while True:
    user_input = input("Sizning savolingiz: ")
    if user_input.lower() in ["chiqish", "exit", "quit"]:
        print("Yordamchi dasturdan chiqish...")
        break
    
    response = ai_yordamchi(user_input)
    print("Yordamchi: ", response)
