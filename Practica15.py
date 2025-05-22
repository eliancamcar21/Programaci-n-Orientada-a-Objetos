from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return "como anda la muchachada?"

if __name__ == "__main__":
    app.run(host='10.2.81.163', port=4000)
