from flask import Flask,render_template

app = Flask(__name__,static_url_path='')

@app.route("/")
def index():
    print("HELLO")
    return app.send_static_file('eitan.html')

@app.route("/<name>")
def say_name(name):
    return render_template('hello3.html',name=name)

if __name__=="__main__":
    app.run(debug=True)


