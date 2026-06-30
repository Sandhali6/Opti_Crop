from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load("model/model.pkl")
scaler = joblib.load("model/scaler.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/findyourcrop")
def findyourcrop():
    return render_template("findyourcrop.html")

@app.route("/predict", methods=["POST"])
def predict():
    values = [float(x) for x in request.form.values()]
    values = np.array(values).reshape(1, -1)
    values = scaler.transform(values)
    prediction = model.predict(values)

    return render_template(
        "findyourcrop.html",
        prediction_text=f"Recommended Crop: {prediction[0]}"
    )

if __name__ == "__main__":
    app.run(debug=True)