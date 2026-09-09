from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Project 2 Web Application</title>
        </head>
        <body>
            <h1>Project 2 Web Application</h1>
            <p>Application: UP</p>
            <p>Database: Not connected yet</p>
        </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)