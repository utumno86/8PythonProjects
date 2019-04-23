from flask import Flask, render_template, request

from src.models.user import User

app = Flask(__name__)

@app.route('/')
def hello_method():
  return render_template('login.html')

@app.route('/login')
def login_user():
  email = request.form['email']
  password = request.form['password']

  if User.login_valid(email, password):
    User.login(email)

  return render_template('profile.html')

if __name__ == '__main__':
  app.run(port=4995)
