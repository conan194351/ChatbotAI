# service.py
from .chat import get_response, bot_name
import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()
class HealthCheckService:
    @staticmethod
    def check_health():
        # Đây là nơi để thực hiện các kiểm tra sức khỏe cụ thể
        # Trong trường hợp này, chúng ta chỉ trả về một thông báo thành công
        return {'status': 'ok'}
    
class Service:
    @staticmethod
    def chatbot (self):
        return {bot_name:get_response(self)}
    def webhook(entries):
        for entry in entries:
            webhook_event = entry['messaging'][0]
            print(webhook_event)
            sender_psid  = webhook_event['sender']['id']
            print('Sender PSID: ' + sender_psid)
            if 'message' in webhook_event:
                handle_message(sender_psid, webhook_event['message'])
            elif 'postback' in webhook_event:
                handle_postback(sender_psid, webhook_event['postback'])
        

def handle_message(sender_psid, received_message):
    global PAGE_ACCESS_TOKEN
    response = None

    if 'text' in received_message:
        response = {
            get_response(received_message)
        }
    elif 'attachments' in received_message:
        attachment_url = received_message['attachments'][0]['payload']['url']
        response = {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [{
                        "title": "Is this the right picture?",
                        "subtitle": "Tap a button to answer.",
                        "image_url": attachment_url,
                        "buttons": [
                            {
                                "type": "postback",
                                "title": "Yes!",
                                "payload": "yes",
                            },
                            {
                                "type": "postback",
                                "title": "No!",
                                "payload": "no",
                            }
                        ],
                    }]
                }
            }
        }

    call_send_api(sender_psid, response)

def handle_postback(sender_psid, received_postback):
    global PAGE_ACCESS_TOKEN
    response = None

    payload = received_postback['payload']

    if payload == 'yes':
        response = {"text": "Thanks!"}
    elif payload == 'no':
        response = {"text": "Oops, try sending another image."}

    call_send_api(sender_psid, response)

def call_send_api(sender_psid, response):
    global PAGE_ACCESS_TOKEN
    request_body = {
        "recipient": {
            "id": sender_psid
        },
        "message": response
    }

    url = "https://graph.facebook.com/v12.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}

    response = requests.post(url, params=params, json=request_body)

    if response.status_code == 200:
        print('Message sent!')
    else:
        print(f'Unable to send message: {response.status_code}, {response.text}')

# You would need to set PAGE_ACCESS_TOKEN to your actual Facebook Page access token.
PAGE_ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', None)
