'''CREATING A BASIK FLASK APPLICATION
'''
#first import flas module
from flask import Flask
#make sure you name a variable app
app = Flask(__name__)

#use a decorator to connect to your url
@app.route('/')
#create a function
def hello():
    '''
    A fuction that returns greetings to our website.

    Returns: Hello world

    '''
    return f"Hello World!"




if __name__ == "__main__":
    '''The debud = True argument used with app.run() helps to automatically start flask'''
    app.run(debug = "True")