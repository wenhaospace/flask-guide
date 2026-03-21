from datetime import timedelta

from flask import Flask, render_template
app = Flask(__name__)


# 基本配置语法
# 1. 在上下文环境设置
# app.config['CONFIG_NAME'] = 'value'
# 2. 从外部文件加载设置
# app.config.from_pyfile('config.py')

# 常见的Flask Configurations
# - Security settings : 例如 secret keys and session handling.
# - Database settings : 连接管理数据库
# - Debugging options : to enable automatic reloading and error reporting.
# - Session management : for handling user sessions.
# - File handling & uploads : configuring file storage.

# 举例：Setting Up a Secret Key
app.config['SECRET_KEY'] = 'your_secret_key' # 保护session cookies等

# 举例： 配置数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 举例： Session Management Configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

# 举例： Configuring JSON Responses
app.config['JSON_SORT_KEYS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 