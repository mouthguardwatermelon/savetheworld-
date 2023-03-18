from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
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
    return render_template('index.html', username = username, password = password,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)

