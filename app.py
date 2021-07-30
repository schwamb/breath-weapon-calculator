from flask import Flask, request, render_template, jsonify, Response
from flask_cors import CORS
from joblib import load
import pandas as pd
from sqlalchemy import create_engine, func

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate')
def calculate():
    height = request.args.get("height")
    angle = request.args.get("angle")
    

    datum[f"SR_TYPE_{srType}"]=1
    print(reg.predict(pd.DataFrame([datum]))[0])
    X = pd.DataFrame([datum])
    X_scaled = scaler.transform(X)
    inDays = (reg.predict(X_scaled)[0][0])
    print(inDays)
    output = (round(inDays, 2))
    print(output)
    return render_template("index.html",prediction_text='Your projected turnaround time is: {} days'.format(output))

if __name__ == "__main__":
    app.run(debug=True)