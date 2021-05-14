from telegram.ext import *
import requests 
from pprint import pprint


KEY = '1689920088:AAEWH9vem9qTxjxLxkGpNI5cyg0oKjPOTMg'

# def slot():

#     header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}

#     URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=590001&date=14-05-2021"
#     response = requests.get(URL, headers=header).json()

#     for hospital in response['centers']:
#         print(hospital['name'])
#         for day in hospital['sessions']:
#             print(day['date'])
#             if day['min_age_limit'] == 45 and day['available_capacity'] != 0:
#                 print('seats: ', day['available_capacity'])
#             else:
#                 print('No slot')
#             print('---------------------------')




def start_command(update, context):
    update.message.reply_text('Welcome, to Cowin-BGM notification')

def help_command(update, context):
    update.message.reply_text('Please contact Admin!')

def handle_message(update, context):
    update.message.reply_text('Hi, Im sammed kamate')

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()