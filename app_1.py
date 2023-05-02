'''CREATES A BASIK FLASK APPLICATION THAT ALLOWS MULTIPLE ENTRIES
Introducs us to render_template and redirect functions
'''
from flask import Flask, render_template, redirect

app = Flask("__main__")
friends = ["Josh", "Kibo", "Wazi"]

@app.route('/')
def say_hi():
    return render_template("index.html", my_friends = friends)

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/home')
def home():
    '''
    This function redirects the route to home page using flsk.redirect function
    '''
    return redirect('/')



if __name__ == "__main__":
    app.run(debug= True)
