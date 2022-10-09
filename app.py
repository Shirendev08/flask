from django.shortcuts import render
from flask import Flask, escape, request, render_template

app = Flask(__name__)
@app.route('/')

def hello():
    
    return render_template("index.html")

@app.route('/greet')  
def greet():
    return render_template("greet.html",name=request.args.get("name"))