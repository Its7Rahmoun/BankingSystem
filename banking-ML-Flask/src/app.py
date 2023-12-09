from flask import Flask , request, jsonify
from tensorflow.keras.models import load_model
from py_eureka_client import eureka_client
import pickle


app = Flask(__name__)

# Eureka server configuration
eureka_client.init(eureka_server="http://localhost:8761/eureka",
                   app_name="MLSERVICE",
                   instance_port=5000)


def predection(deta):
    new_data=[]
    new_data.append(deta)
    loaded_model = load_model("ANN_model.h5")
    with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
        loaded_tfidf_vectorizer = pickle.load(vectorizer_file)

    new_data_tfidf = loaded_tfidf_vectorizer.transform(new_data).toarray()
    predictions = (loaded_model.predict(new_data_tfidf) > 0.5).astype(int)

    # 'predictions' now contains the predicted labels for the new data
    return predictions

@app.get("/")
def index():
    return {
        "name" : "oussama",
        "age" : 20
    }

@app.post("/informationVerfier")
def informationVerfier():
    data = request.get_json()
    value = 0
    if 'username' in data:
        pre = predection(data["username"])
        for i in pre:
            for j in i:
                value=j
        return {"predected":str(value)}


if __name__ == "__main__":
    app.run(debug=True)
