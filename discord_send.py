import requests
import os
from dotenv import load_dotenv

load_dotenv()

class DiscordSend:
    
    def __init__(self):
        # WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        
    #warnnig notification
    def  warning_notification(self,warning_message):
        data = {
            #send warning message to discord
            "content": warning_message
            }
        
        response = requests.post(self.webhook_url, json=data)

        if response.status_code == 204:
            print("Sent successfully!")
        else:
            print("Failed:", response.status_code)
            
    #seinding final report
    def send_final_report(self,final_report):
        data = {
            "content": final_report
        }
        
        response = requests.post(self.webhook_url, json=data)

        if response.status_code == 204:
            print("Sent successfully!")
        else:
            print("Failed:", response.status_code)

if __name__ == "__main__":
    discord = DiscordSend()
    discord.warning_notification(" smartphone usage has been detected")
    discord.warning_notification(" Please put your smartphone down")
    discord.end_final_report("final repot ....")
    
        

            
 
 #temporarily codes for testing           
# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")


# def send_discord(message):
#     data = {
#         "content": message
#     }

#     response = requests.post(WEBHOOK_URL, json=data)

#     if response.status_code == 204:
#         print("Sent successfully!")
#     else:
#         print("Failed:", response.status_code)


# if __name__ == "__main__":
#     send_discord("Hello from Raspberry Pi!")




