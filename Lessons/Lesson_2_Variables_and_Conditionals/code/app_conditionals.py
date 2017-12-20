from flask import Flask

app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    print("HELLO")
#    return "HELLO"
    return app.send_static_file('hello.html')


@app.route("/sayname/<name>")
def say_name(name):
    return "Hi, my friend, " + name


@app.route("/taco")
def unknown_taco_money():
    print("Please tell me how much money you have")
    return "Please tell me how much money you have"

@app.route("/taco/<int:money>")
def can_buy_taco(money):
    if money > 5:
        print("I have enough money for a taco")
        return "I have enough money for a taco"
    elif money == 5:
        print("I have exactly enough money for a taco")
        return "I have exactly enough money for a taco"
    elif money == 4:
        print("I don't have enough money for a taco...but I can buy tortilla chips!")
        return "I don't have enough money for a taco...but I can buy tortilla chips!"
    else:
        print("I don't have enough money for a taco")
        return "I don't have enough money for a taco"




if __name__ == "__main__":
    app.run()

