from twilio.rest import Client

# Twilio credentials
account_sid = 'AC371b3ce7c2fa113db888cad13f32e66b'
auth_token = '2251c0703e9fc96ab5edb4013e216dd1'

client = Client(account_sid, auth_token)

message_body = """Stay safe from COVID-19!😷️
Wear a mask, wash your hands frequently, and maintain social distancing.
Get vaccinated💉️ to protect yourself and your loved ones.
If you have any health queries or doubts, ask our chatbot here 👉️
https://chat.seasalt.ai/chat/2fd0447c29f04551a9888dfc3144fa48
"""
message = client.messages.create(
    body=message_body,
    from_='whatsapp:+14155238886',
    to='whatsapp:+916300585614'
)

print(message.sid)

