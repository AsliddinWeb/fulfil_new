import requests
from .models import Admin

def send_message_telegram(ism, telefon, telegram):
    adminlar = Admin.objects.all()

    for i in adminlar:
        try:
            token = i.bot_token
            method = 'sendMessage'
            response = requests.post(
                url=f'https://api.telegram.org/bot{token}/{method}',
                data={
                    'chat_id': i.telegram_id,
                    'text': f"Yangi ariza\n\n"
                            f"Ismi: {ism}\n"
                            f"Telefon raqami: {telefon}\n"
                            f"Telegram: {telegram}"
                }
            ).json()
            print(response)
        except:
            pass