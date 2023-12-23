# handler.py
from flask import jsonify,request
from services.service import HealthCheckService,Service
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

class HealthCheckHandler:
    @staticmethod
    def health_check():
        # Gọi phương thức check_health từ service
        health_status = HealthCheckService.check_health()
        # Trả về response JSON
        return jsonify(health_status)
    
class Handler:
    @staticmethod
    def chat():
        data = request.get_json()
        msg_value = data.get('msg')
        return jsonify(HealthCheckService.chatbot(msg_value))
    def webhook():
        data = request.get_json()
        if data.get('object') == "page":
            entries = data.get('entry')
            Service.webhook(entries)
        else:
            return jsonify(404)
        
    def get_webhook():
        token = os.getenv('MYTOKEN', None)
        print(token)
        mode = request.args.get("hub.mode")
        verify_token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if mode and verify_token:
            if mode == "subscribe" and token == verify_token:
                print("WEBHOOK_VERIFIED")
                return challenge, 200
            else:
                return "Forbidden", 403
            