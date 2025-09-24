from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Witaj w moim środowisku developerskim!</h1><p>Przejdź do /code, /adminer, /portainer, /gitea</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)