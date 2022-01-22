
from flask import Flask
from functools import wraps
app=Flask(__name__)

def make_bold(function):    
    def wrapper():
        return f' <b> {function()} and</b>'
    return wrapper

@app.route("/")
def index():
    return '''<h1 style="text-align: center">Dönüşüm</h1>
    <br>
    <img style="text-align: center;" src="https://www.cumhuriyet.com.tr/Archive/2021/4/10/1827121/kapak_154320.jpg">
    <p>Gregor Samsa bir sabah bunaltıcı düşlerden uyandığında, kendini yatağında devasa bir böceğe dönüşmüş olarak buldu.</p>
    '''

@app.route("/boldtexts")
@make_bold
def boldtexts():
    return "hello"