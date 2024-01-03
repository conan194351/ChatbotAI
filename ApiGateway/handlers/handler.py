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
        return jsonify(Service.chatbot(msg_value))
    # def message(self):
            