# 🌱 OptiCrop – Smart Crop Recommendation System

## 📖 Overview

OptiCrop is a Machine Learning-based web application that recommends the most suitable crop to cultivate based on soil nutrients and environmental conditions. The system helps farmers and agricultural enthusiasts make informed crop selection decisions using predictive analytics.

---

## 🚀 Features

- 🌾 Predicts the most suitable crop
- 📊 Uses Machine Learning for accurate recommendations
- 🧪 Accepts soil and climate parameters:
  - Nitrogen (N)
  - Phosphorus (P)
  - Potassium (K)
  - Temperature
  - Humidity
  - pH
  - Rainfall
- 💻 User-friendly Flask web interface
- ⚡ Fast and accurate predictions

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib

---

## 📂 Project Structure

```
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
|-------|---------:|
| Logistic Regression | 96.36% |
| K-Nearest Neighbors (KNN) | 95.68% |
| Decision Tree | 98.64% |
| Random Forest | 99.32% |
| **Naive Bayes** | **99.55%** |

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

Recommended crop.

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

### Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Model

Train the machine learning model:

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

## 📷 Application Pages

- 🏠 Home
- ℹ️ About
- 🌱 Find Your Crop

---

## 📈 Model Workflow

1. Load dataset
2. Perform data preprocessing
3. Split data into training and testing sets
4. Scale input features
5. Train multiple ML models
6. Compare model accuracies
7. Select the best-performing model
8. Save the trained model
9. Deploy using Flask

---

## 📌 Future Enhancements

- Weather API integration
- Fertilizer recommendation
- Disease prediction
- Crop yield estimation
- Multi-language support

---

## 👩‍💻 **Team Members**

- Dasari Sandhali Sandhali (Team Lead)
- J Daniya Saman (Member)
- Mighty Abhishek Darivemula (Member)
- Mohammed Fasi Faraz (Member)

## 📄 License

This project is created for educational purposes.