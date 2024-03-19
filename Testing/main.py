import flask
from flask import render_template, url_for
from Testing.poem import poem_dic

app = flask.Flask(__name__)
app.config["secret_key"] = "melancholicMelodies"


@app.route("/")
def index():
    return render_template("index.html", data=poem_dic)


if __name__ == "__main__":
    app.run(debug=True)
    app.run()
