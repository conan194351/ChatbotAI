# handler.py
from flask import jsonify,request
from services.service import HealthCheckService

class HealthCheckHandler:
    @staticmethod
    def health_check():
        # Gọi phương thức check_health từ service
        health_status = HealthCheckService.check_health()
        # Trả về response JSON
        return jsonify(health_status)
    def chat():
        data = request.get_json()
        msg_value = data.get('msg')
        return jsonify(HealthCheckService.chatbot(msg_value))