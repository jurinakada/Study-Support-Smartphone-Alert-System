# from discordwebhook import Discord
# import requests
# import os

# #discord = Discord(url="webhook url")

# # WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
# WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

# class disc_send:
#     #test
#     # dis_send(final_report):
#     #     discord.post(content='final_report')

#     # dis_send("hello this is test")

#     def  warning_notification(warning_message):
#         data = {
#             #send warning message to discord
#             "content": "this is test for sending final report"
#             }

#     def send_final_report(final_report):
#         data = {
#         #"content": final_report
#         #send final report to discord
#         "content": "this is test for sending final report"
#         }

#         try:
#             response = requests.post(WEBHOOK_URL, json=data)

#             if response.status_code == 204:
#                 print("Message sent successfully!")
#             else:
#                 print(f"Failed to send: {response.status_code}")

#         except requests.exceptions.RequestException as e:
#             print("Network error. Final report was not sent.")
#             print(e)
            
            
import os
import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


def send_discord(message):
    data = {
        "content": message
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("Sent successfully!")
    else:
        print("Failed:", response.status_code)


if __name__ == "__main__":
    send_discord("Hello from Raspberry Pi!")




