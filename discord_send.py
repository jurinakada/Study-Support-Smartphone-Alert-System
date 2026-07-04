from discordwebhook import Discord
import requests

#discord = Discord(url="webhook url")

WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_URL"


class disc_send:
    #test
    # dis_send(final_report):
    #     discord.post(content='final_report')

    # dis_send("hello this is test")

    warning_notification():

    send_final_report(final_report):
        data = {
        #"content": final_report
        "content": "this is test for sending final report"

        }

        try:
            response = requests.post(WEBHOOK_URL, json=data)
        
        if response.status_code == 204:
            print("Message sent successfully!")
        else:
            print(f"Failed to send: {response.status_code}")




