# route.py
from flask import Blueprint
from handlers.handler import HealthCheckHandler,Handler

# Tạo Blueprint để đăng ký route
routers = Blueprint('health_check', __name__)

# Đăng ký route "/health" với phương thức GET và xử lý từ HealthCheckHandler
@routers.route('/health', methods=['GET'])
def health_check_route():
    return HealthCheckHandler.health_check()

@routers.route('/chat', methods=['POST'])
def chat():
    return Handler.chat()

@routers.route('/webhook', methods=['POST'])
def webhook():
    return Handler.webhook()

@routers.route('/webhook', methods=['GET'])
def messaging_webhook():
    return Handler.get_webhook()