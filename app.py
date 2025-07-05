# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
@app.route("/")
def home():
    return "🚀 Deployment works!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


# === Load Model and Scaler ===
model_path  = os.path.join('Model', 'LR_model.pkl')
scaler_path = os.path.join('Model', 'scaler.pkl')
model: RandomForestRegressor = joblib.load(model_path)
scaler: StandardScaler = joblib.load(scaler_path)
# === Check if Model and Scaler are Loaded Correctly ===
if model and scaler:
    print("Model and Scaler loaded successfully.")
else:

    print("Error loading Model and Scaler.")
# === Categorical Mappings ===
SUBSTANCE_MAP = {
    'Carbon Dioxide':              [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'Methane':                     [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    'Nitrous Oxide':              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
}


UNIT_MAP = {
    'kg/2018 USD, purchaser price': [1, 0],
    'kg CO2e/2018 USD, purchaser price': [0, 1],
}

SOURCE_MAP = {
    'Commodity': [1, 0],
    'Industry':  [0, 1],
    'Transport': [0, 0, 1],
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # === Get Form Inputs ===
        substance       = request.form['substance']
        unit            = request.form['unit']
        source          = request.form['source']
        supply_wo_margin= float(request.form['supply_wo_margin'])
        margin          = float(request.form['margin'])
        dq_reliability  = float(request.form['dq_reliability'])
        dq_temporal     = float(request.form['dq_temporal'])
        dq_geo          = float(request.form['dq_geo'])
        dq_tech         = float(request.form['dq_tech'])
        dq_data         = float(request.form['dq_data'])

        # === Feature Vector Construction ===
        input_vector = (
            SUBSTANCE_MAP[substance] +
            UNIT_MAP[unit] +
            SOURCE_MAP[source] +
            [
                supply_wo_margin,
                margin,
                dq_reliability,
                dq_temporal,
                dq_geo,
                dq_tech,
                dq_data
            ]
        )

        # === Predict ===
        input_array  = np.array(input_vector).reshape(1, -1)
        scaled_input = scaler.transform(input_array)
        prediction   = model.predict(scaled_input)[0]

        return render_template(
            'index.html',
            submitted=True,
            prediction_text=f"Estimated GHG Emission: {prediction:.4f} kg CO₂e/unit",
            inputs=[
                substance, unit, source,
                supply_wo_margin, margin,
                dq_reliability, dq_temporal,
                dq_geo, dq_tech, dq_data
            ]
        )

    except Exception as e:
        return render_template(
            'index.html',
            submitted=False,
            prediction_text=f"Error: {str(e)}"
        )

if __name__ == '__main__':
    app.run(debug=True)