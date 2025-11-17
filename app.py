from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        voltage = float(request.form['voltage'])
        current = float(request.form['current'])
        power_kw = float(request.form['power_kw'])
        temperature = float(request.form['temperature'])
        load_kw = float(request.form['load_kw'])
        failure_risk = float(request.form['failure_risk'])

        # Combine all inputs into a single row
        features = np.array([[voltage, current, power_kw, temperature, load_kw, failure_risk]])

        # Scale and predict
        scaled_features = scaler.transform(features)
        prediction = model.predict(scaled_features)[0]

        return render_template('result.html', prediction=round(prediction, 2))

    except Exception as e:
        return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

