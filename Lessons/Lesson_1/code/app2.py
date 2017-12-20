from flask import Flask

app = Flask(__name__,static_url_path='')

@app.route("/")
def index():
    print("HELLO")
    return app.send_static_file('hello.html')


@app.route("/<name>")
def say_name(name):
    text = """<!DOCTYPE html>
    <html >
        <head>
            <style>
            body {
            background-color: #275399;
            font-family: 'Ubuntu', sans-serif;
            }
            </style>
        </head>
        <body>
            Hello, %s!
            <br>
            <br>
            This is cool, huh?
        </body>
    </html>
    """
    return text % name

if __name__=="__main__":
    app.run(debug=True)


