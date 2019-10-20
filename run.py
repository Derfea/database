from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    render_template(upload.html)


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["inputFile"]

    return file.filename

if __name__ =="__main__":
    app.run(debug=True)