# service.py
from .chat import get_response, bot_name

class HealthCheckService:
    @staticmethod
    def check_health():
        return {'status': 'ok'}
    
class Service:
    @staticmethod
    def chatbot (self):
        return {bot_name:get_response(self)}
