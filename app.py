from flask import Flask
import socket

app = Flask(__name__)


@app.route("/")
def home():
    hostname = socket.gethostname()

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Project 2 Application</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                padding: 40px;
            }}

            .container {{
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            }}

            h1 {{
                color: #222;
            }}

            .status {{
                color: green;
                font-weight: bold;
            }}
        </style>
    </head>

    <body>
        <div class="container">
            <h1>Project 2 Web Application</h1>

            <p>
                Application Status:
                <span class="status">RUNNING</span>
            </p>

            <p>EC2 Instance: {hostname}</p>

            <p>Database Status: Connecting...</p>

            <p>Visitor Count: Coming Soon</p>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)