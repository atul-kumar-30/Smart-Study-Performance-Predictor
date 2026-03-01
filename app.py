from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model
model = joblib.load("models/model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    hours = float(request.form["hours"])
    
    input_data = pd.DataFrame([[hours]], columns=["Hours"])
    prediction = model.predict(input_data)[0]

    return render_template("index.html",
                           prediction_text=f"Predicted Score: {round(prediction, 2)}")

if __name__ == "__main__":
    app.run(debug=True)