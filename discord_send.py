import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DiscordSend:
    
    def __init__(self):
        # WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"
        self.webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
        
        #check the existence of Discord Webhook URL
        if self.webhook_url is None:
            print("DISCORD_WEBHOOK_URL was not found in .env")
    
    #warnnig notification
    def warning_notification(self, warning_message):
        if self.webhook_url is None:
            print("Discord warning notification was not sent")
            return

        data = {
            #send warning message to discord
            "content": warning_message
        }
        
        response = requests.post(self.webhook_url, json=data)

        if response.status_code == 204:
            print("Sent successfully!")
        else:
            print("Failed:", response.status_code)
            
    #sending final report
    def send_final_report(self, final_report):
        if self.webhook_url is None:
            print("Final report was not sent")
            return

        data = {
            "content": final_report
        }
        
        response = requests.post(self.webhook_url, json=data)

        if response.status_code == 204:
            print("Sent successfully!")
        else:
            print("Failed:", response.status_code)


#testing
# if __name__ == "__main__":
#     discord = DiscordSend()
#     discord.warning_notification("Smartphone usage has been detected")
#     discord.warning_notification("Please put your smartphone down")
#     discord.send_final_report("Final report ....")