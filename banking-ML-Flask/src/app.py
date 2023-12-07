from flask import Flask , request, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return {
        "name" : "oussama",
        "age" : 20
    }

@app.post("/informationVerfier")
def informationVerfier():
    data = request.get_json()
    if 'username' in data:
        return 0
