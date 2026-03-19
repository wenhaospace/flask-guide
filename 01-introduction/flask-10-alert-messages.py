from flask import Flask, request, render_template, make_response, flash, redirect, url_for
app = Flask(__name__)

# /login display login form
@app.route('/')
def index(): 
    return render_template('login_index.html') 


@app.route('/login', methods=['GET', 'POST'])
# login function verify username and password
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again !'
        else:

            # flashes on successful login
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login_index.html', error=error)


if __name__ == '__main__':
    app.run(debug=True)