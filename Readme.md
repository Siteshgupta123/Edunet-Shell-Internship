<p align="center">
  <img src="static/Edunet-Foundation-logo.png" alt="Edunet Foundation" height="40" style="margin-right: 15px;">
  <img src="static/Shell-Logo.png" alt="Shell" height="45px">
</p>

# 🌱 Greenhouse Gas (GHG) Emission Prediction Project

### Internship Project under ,**[Edunet Foundation](https://www.linkedin.com/company/edunetfoundation/posts/?feedView=all)** × **[Shell Energy](https://www.linkedin.com/company/shell-energy/)**

This project was developed as part of my **AI/ML with Data Analytics internship** at **[Edunet Foundation](https://www.linkedin.com/company/edunetfoundation/posts/?feedView=all)** in collaboration with **[Shell Energy](https://www.linkedin.com/company/shell-energy/)** focused on applying data science to sustainability and environmental impact analysis.

---

## Problem Statement:
We were provided with official **U.S. supply chain emissions data (2010–2016)** categorized by industry and commodity. The main objective was to build a **regression-based ML model** to **predict Greenhouse Gas (GHG) emission factors with margins**, using a combination of:
- Emission descriptors (substance, unit, source)
- Data quality indicators (reliability, correlations, etc.)

---

## Project Goal:
To design a machine learning solution that predicts **Supply Chain Emission Factors (kg CO₂e/unit)** by analyzing:
- Commodity and Industry Metadata
- Data Quality Scores (DQ)
- Source Type, Unit Format, and Geographical Span

---

## Dataset Source:
- [U.S. GHG Emission Factors Dataset – Data.gov](https://catalog.data.gov/dataset/supply-chain-greenhouse-gas-emission-factors-for-us-industries-and-commodities)

---

## Tech Stack(For .ipynb file):
- **Language**: Python  
- **Libraries**:  
  - Pandas & NumPy – Data manipulation  
  - Seaborn & Matplotlib – Data visualization  
  - Scikit-learn – Machine learning models  
- **Environment**: Jupyter Notebook

## For The Web App:
Technologies Used
- **Python 3.10**
- **Flask** — Web framework
- **scikit-learn** — For model building and prediction
- **pandas** — Data processing
- **joblib** — Model serialization
- **openpyxl** — Excel file support

---

## Project Workflow:
### Week 1:  
- Data loading, structure understanding  
- Cleaning null and inconsistent values  
- Categorical encoding

### Week 2:  
- Exploratory Data Analysis  
- Feature correlations and visualizations  
- Handling outliers & data imputation

### Week 3:  
- Regression modeling (Linear, Random Forest)  
- Evaluation metrics: **R² Score, MAE, RMSE**  
- Sample predictions & output visualization

---

## 📈 Model Performance:

| Metric         | Value       |
|----------------|-------------|
| R² Score       | 0.89        |
| RMSE           | 4.21        |
| MAE            | 2.77        |

> The model demonstrated good generalization with strong predictive accuracy.

---
## Project View:
![GreenHouse Gas Emmsion Prediction WebApp View](https://github.com/user-attachments/assets/5b4a1639-9947-47cb-9b32-9aeb5229afa0)
![GreenHouse Gas Emmsion Prediction WebApp View-2](https://github.com/user-attachments/assets/3443b36f-2591-4f1c-bd13-f769c7a435ba)

https://github.com/user-attachments/assets/68a33ae2-9fea-402a-86ba-cb6d4a1c5905

--------------------------------------
## Project Structure:
```
GHG Emission App/
├── app.py                       # Main Flask application file
├── requirements.txt             # List of required Python packages
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
 ## Notes:
- app.py: Binds the port dynamically for Render and routes to index.html
- static/: Contains images used in your web layout (like the Edunet and Shell logos)
- model/: Stores serialized ML assets to avoid retraining on deployment
- requirements.txt: Should include only essential, compatible libraries
- runtime.txt: Ensures Render uses Python 3.10 (not 3.13!)

---
##  How to Run Locally:
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
### Features:
- Interactive HTML form for GHG prediction
- Uses trained ML model to estimate emissions
- Scales inputs dynamically using StandardScaler
- Sleek web interface with Edunet & Shell branding

----
### A sample prediction from the final model showing the GHG emission estimation for a commodity:
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
| Predicted Emission            | 97.88 kg CO₂e/unit                 |
> Value may be vary at time of prediction.
-----------------------------------------------------------------------------

## Key Learnings:
- Preprocessing real-world, multi-feature environmental datasets
- Role of feature engineering in sustainability analytics
- How data quality indicators affect machine learning predictions
- Visualizing and interpreting GHG-related outputs for practical impact

---
## Future Scope
- Integrate this model into a **Flask dashboard(Already Integrated)**  
- Expand prediction logic with **time series emissions trend**  
- Include external variables like policy impact, regional energy mix

---

## Acknowledgment:
Special thanks to **[Raghunanadan M S Sir](https://www.linkedin.com/in/raghunandanms/)**,**[Dr. Dulari Bhatt Ma’am](https://www.linkedin.com/in/dulari-bhatt/)** for their continued mentorship throughout the internship. This project gave me real-world experience in sustainable analytics and AI/ML pipeline development.

------
## Thank You! 💙

Thanks for checking out my project! If you found it useful, please consider:  
[![GitHub stars](https://github.com/Siteshgupta123)] 
⭐ **Starring** the repo  
🐛 **Reporting** issues  
🛠 **Contributing** improvements  

Coded with ❤️ by **Sitesh Gupta**  
🔗 www.linkedin.com/in/guptasitesh | 💌 Email-guptasitesh05@email.com


------------------
