from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'My world'

@app.route('/username/<peru>')
def greet(peru):
    return f'Hello {peru}'

if __name__ == '__main__':
    app.run()

















# Function decorater
# import time
#
#
# def timer_function(func):
#     def wrapper_function():
#         time.sleep(3)
#         func()
#     return wrapper_function()
#
# @timer_function
# def main():
#     print("This is my main function")
#
# @timer_function
# def greeting():
#     print("Hello everyone")