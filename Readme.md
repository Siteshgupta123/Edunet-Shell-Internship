<p align="center">
  <img src="static/Edunet-Foundation-logo.png" alt="Edunet Foundation" height="40" style="margin-right: 15px;">
  <img src="static/Shell-Logo.png" alt="Shell" height="15">
</p>

# <h1 align="center">🌍GHG Emission Predictor Web App</h1>
Predict greenhouse gas emissions based on energy consumption inputs using a Flask-powered web interface.This project is apart of Edunet Foundation x Shell AI/ML Internship, focusing on real-world applications of machine learning for sustainability.
---
## 📂 Project Structure
```
GHG Emission App/
├── app.py                       # Main Flask application file
├── requirements.txt             # List of required Python packages
├── runtime.txt                  # Python version specification for Render
├── .gitattributes               # Git attributes configuration
├── data/
│   └── GHG Dataset.xlsx         # Dataset used for model development
├── model/
│   ├── LR_model.pkl             # Trained linear regression model
│   └── scaler.pkl               # Scaler used for preprocessing
├── static/
│   ├── Edunet-Foundation-logo.png
│   └── Shell-Logo.png           # Logos displayed in the web UI
└── templates/
    └── index.html               # Main HTML template rendered by Flask
```
---------------------
 ## Notes
- app.py: Binds the port dynamically for Render and routes to index.html
- static/: Contains images used in your web layout (like the Edunet and Shell logos)
- model/: Stores serialized ML assets to avoid retraining on deployment
- requirements.txt: Should include only essential, compatible libraries
- runtime.txt: Ensures Render uses Python 3.10 (not 3.13!)

----
## 🧠 Technologies Used
- **Python 3.10**
- **Flask** — Web framework
- **scikit-learn** — For model building and prediction
- **pandas** — Data processing
- **joblib** — Model serialization
- **openpyxl** — Excel file support

---
## 🖥️ How to Run Locally
1. Clone the repo:
```
git clone https://github.com/Siteshgupta123/Edunet-Shell-Internship.git
cd Edunet-Shell-Internship
```
2. Install dependencies:
```
pip install -r requirements.txt
```
3. Run the app:
```
python app.py
```
4. Visit in browser:
```
http://localhost:5000
```
Features
- Interactive HTML form for GHG prediction
- Uses trained ML model to estimate emissions
- Scales inputs dynamically using StandardScaler
- Sleek web interface with Edunet & Shell branding
----
Example Inputs: Energy Scenario
| **Field**                      | **Value**                          |
|-------------------------------|------------------------------------|
| Substance                     | Carbon dioxide                     |
| Unit                          | kg CO₂e / 2018 USD, purchaser price |
| Source                        | Energy                             |
| Supply Chain                  | 52.3                               |
| Margin                        | 12.5                               |
| DQ Reliability                | 0.88                               |
| DQ Temporal Correlation       | 0.72                               |
| DQ Geographical Correlation   | 0.90                               |
| DQ Technological Correlation  | 0.86                               |
| DQ Data Collection            | 0.82                               |
| Predicted Emission            | 61.3274 kg CO₂e/unit               |
-----------------------------------------------------------------------------
