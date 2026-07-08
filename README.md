# 🌱 OptiCrop – Smart Crop Recommendation System

## 📖 Overview

OptiCrop is an AI-powered Crop Recommendation System that recommends the most suitable crop based on soil nutrients and environmental conditions. The application features a modern, responsive web interface built using Flask, HTML, and CSS, enabling users to receive real-time crop recommendations through a trained Machine Learning model. It helps farmers and agricultural enthusiasts make informed crop selection decisions for improved productivity and sustainable farming.

---

## 🚀 Features

- 🌾 AI-powered crop recommendation
- 📊 Machine Learning-based prediction model
- 🧪 Accepts 7 soil and environmental parameters:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- ⚡ Instant crop prediction
- 💻 Modern responsive web interface
- 🌿 Animated agriculture-themed user interface
- 📱 Mobile-friendly design
- 🚜 Supports smart farming decisions

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Pandas
- NumPy
- Scikit-learn
- Joblib

---

## 📂 Project Structure

```text
Opti_Crop/
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── model/
│   ├── model.pkl
│   └── scaler.pkl
│
├── static/
│   ├── images/
│   └── style.css
│
├── templates/
│   ├── home.html
│   ├── about.html
│   └── findyourcrop.html
│
├── app.py
├── train_model.py
├── requirements.txt
└── README.md
```

---

## 📊 Machine Learning Models Compared

| Model | Accuracy |
|--------|---------:|
| Logistic Regression | 96.36% |
| K-Nearest Neighbors (KNN) | 95.68% |
| Decision Tree | 98.64% |
| Random Forest | 99.32% |
| Naive Bayes | **99.55%** |

**Best Model:** Naive Bayes

---

## 📁 Dataset

The Crop Recommendation dataset contains:

- 2200 records
- 22 crop categories
- 7 input features
- No missing values

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

### Output

- Recommended Crop

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Sandhali6/Opti_Crop.git
```

### Navigate to the project

```bash
cd Opti_Crop
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment (Windows)

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Machine Learning Model

```bash
python train_model.py
```

---

## 🌐 Run the Flask Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📷 Application Screens

### 🏠 Home Page

*(Add Home page screenshot here)*

### 🌱 Find Your Crop

*(Add Crop Prediction page screenshot here)*

### ℹ️ About

*(Add About page screenshot here)*

---

## 📈 Model Workflow

1. Load the crop recommendation dataset
2. Perform data preprocessing
3. Split data into training and testing sets
4. Scale numerical features using StandardScaler
5. Train multiple Machine Learning models
6. Compare model performance
7. Select the best-performing model
8. Save the trained model and scaler
9. Integrate the model with Flask
10. Generate real-time crop recommendations

---

## 🚀 Deployment

The application is deployed using **Render** and can be accessed through a public web URL for real-time crop recommendations.

**Live Demo:** *(Add your Render URL here after deployment)*

---

## 📌 Future Enhancements

- 🌦️ Weather API integration
- 🧪 Fertilizer recommendation
- 🌱 Crop disease detection
- 📈 Crop yield prediction
- 🌍 Multi-language support
- 👤 User authentication

---

## 👩‍💻 Team Members

- **Dasari Sandhali Sandhali** (Team Lead)
- **J Daniya Saman** (Member)
- **Mighty Abhishek Darivemula** (Member)
- **Mohammed Fasi Faraz** (Member)

---

## 📄 License

This project is developed for educational purposes as part of an academic Machine Learning project.