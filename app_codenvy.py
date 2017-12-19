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
    

@app.route("/friend/friend")
def friend(name):
    return "Hi, my friend, " + name


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    