from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
        <h1>Welcome to development environment!</h1>
        <p>Go to:</p>
        <ul>
            <li><a href="/code">code-server</a></li>
            <li><a href="/adminer">Adminer</a></li>
            <li><a href="/portainer">Portainer</a></li>
            <li><a href="/gitea">Gitea</a></li>
        </ul>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)