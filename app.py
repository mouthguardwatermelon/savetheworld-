from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    username = None
    password = None
    message = ''
    email = None
    email_message = ''
    if request.method == 'POST':
        username = request.form.get('username')
        with open('username.txt', 'r+') as f:
            contents = f.read()
            lines = contents.split(" ")
            lines = [line for line in lines if line]
            if username in lines:
                message = "Username already has been taken!"
            else:
                f.write(f"{username} ")
                f.seek(0)  # Reset cursor position to the beginning of the file
        password = request.form.get('password')
        with open('password.txt', 'r+') as x:
            x.write(f"{password} ")
            x.seek(0)  # Reset cursor position to the beginning of the file
        email = request.form.get('email')
        with open('email.txt', 'r+') as i:
            contents = i.read()
            emails = contents.split(" ")
            emails = [line for line in emails if line]
            if email in emails:
                email_message = "Email has already been registered"
            else:
                i.write(f"{email} ")
                i.seek(0)  # Reset cursor position to the beginning of the file
        if username not in lines and email not in emails:
            message = "Sign up successful!"
    return render_template('sign_up.html', username=username, password=password, email=email, message=message, email_message=email_message)

@app.route('/login', methods=['GET', 'POST'])
def login():
    username = None
    password = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        with open('username.txt','r') as f:
            contents = f.read()
            lines = contents.split(" ")
            lines = [line for line in lines if line]  
        with open('password.txt','r') as f:
            contents = f.read()
            passwords = contents.split(" ")
            passwords = [line for line in passwords if line]
        if username in lines:
            index = lines.index(username)
            if passwords[index] == password:
                return render_template('success.html' , username = username)
            else:
                return render_template('fail.html',username = username)
        else:
            return render_template('fail.html',username = username)
    return render_template('login.html', username = username, password = password,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

