# route.py
from flask import Blueprint
from handlers.handler import HealthCheckHandler

# Tạo Blueprint để đăng ký route
health_check_bp = Blueprint('health_check', __name__)

# Đăng ký route "/health" với phương thức GET và xử lý từ HealthCheckHandler
@health_check_bp.route('/health', methods=['GET'])
def health_check_route():
    return HealthCheckHandler.health_check()

@health_check_bp.route('/chat', methods=['POST'])
def chat():
    return HealthCheckHandler.chat()