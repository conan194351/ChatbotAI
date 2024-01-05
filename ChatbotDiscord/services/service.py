# service.py
from .chat import get_response, bot_name

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
    def handler_message(message)->str:
        p_message = message.lower()
        return get_response(p_message)
