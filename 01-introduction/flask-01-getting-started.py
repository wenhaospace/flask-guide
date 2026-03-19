from flask import Flask
app = Flask(__name__) # Flask 构造器

# 关联url对应的function
@app.route('/')
def hello():
    return 'HELLO'

if __name__ == '__main__':
    app.run(debug=True)



 