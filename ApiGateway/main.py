# app.py
from flask import Flask
from routers.route import routers

app = Flask(__name__)

# Đăng ký Blueprint cho route health check
app.register_blueprint(routers)

if __name__ == '__main__':
    # bot.run_discord_bot()
    app.run(debug=True,port=8081)
    pass
