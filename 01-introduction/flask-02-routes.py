from flask import Flask
app = Flask(__name__)


# 方式一 ==============================
# decorator to route URL 
@app.route('/hello1') 

# binding to the function of route 
def hello_world_1():     
    return 'Hello world 1' 


# 方式二 ===============================
def hello_world_2():
    return 'hello world 2'
  
app.add_url_rule('/', 'hello',hello_world_2)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 