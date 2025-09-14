from twilio.rest import Client

account_sid = 'AC371b3ce7c2fa113db888cad13f32e66b'
auth_token = '2251c0703e9fc96ab5edb4013e216dd1'
client = Client(account_sid, auth_token)

numbers = [
    '+916300585614',
    '+918074694203',
]

for number in numbers:
    message = client.messages.create(
        body=(
            "Stay safe from COVID-19! 😷\n"
            "Wear a mask, wash your hands frequently, and maintain social distancing.\n"
            "Get vaccinated 💉 to protect yourself and your loved ones.\n\n"
            "If you have any health queries or doubts, ask our chatbot here 👉 "
            "https://chat.seasalt.ai/chat/2fd0447c29f04551a9888dfc3144fa48"
        ),
        from_='+14195574262',  # Your Twilio numbder
        to=number
    )
    print(f"Message sent to {number}, SID: {message.sid}")

