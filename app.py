from flask import Flask, render_template, request, redirect, url_for
import os
from flask.cli import F
import numpy as np
import pandas as pd
from src.datascienceproject.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Route to train the pipeline
@app.route("/train")
def train():
    os.system("python main.py")
    # You can add the training logic here if needed
    return "Training started! Check the logs for details."


# Route to predict
@app.route("/predict", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            fixed_acidity = float(request.form["fixed_acidity"])
            volatile_acidity = float(request.form["volatile_acidity"])
            citric_acid = float(request.form["citric_acid"])
            residual_sugar = float(request.form["residual_sugar"])
            chlorides = float(request.form["chlorides"])
            free_sulfur_dioxide = float(request.form["free_sulfur_dioxide"])
            total_sulfur_dioxide = float(request.form["total_sulfur_dioxide"])
            density = float(request.form["density"])
            pH = float(request.form["pH"])
            sulphates = float(request.form["sulphates"])
            alcohol = float(request.form["alcohol"])
            # Create a DataFrame from the input data
            data = [
                fixed_acidity,
                volatile_acidity,
                citric_acid,
                residual_sugar,
                chlorides,
                free_sulfur_dioxide,
                total_sulfur_dioxide,
                density,
                pH,
                sulphates,
                alcohol,
            ]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            predict = obj.predict(data)

            return render_template("results.html", prediction=str(predict))
        except Exception as e:
            return "Something went wrong: " + str(e)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
