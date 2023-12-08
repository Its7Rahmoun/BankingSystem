from tensorflow.keras.models import load_model
import pickle

def predection(new_data):
    loaded_model = load_model("ANN_model.h5")
    with open("tfidf_vectorizer.pkl", "rb") as vectorizer_file:
        loaded_tfidf_vectorizer = pickle.load(vectorizer_file)

    new_data_tfidf = loaded_tfidf_vectorizer.transform(new_data).toarray()
    predictions = (loaded_model.predict(new_data_tfidf) > 0.5).astype(int)

    # 'predictions' now contains the predicted labels for the new data
    return predictions
