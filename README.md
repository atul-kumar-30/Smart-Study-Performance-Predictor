# 📚 Smart Study Performance Predictor

A Machine Learning + Flask Web Application that predicts a student's final exam score based on study hours.

---

## 🚀 Project Overview

Smart Study Performance Predictor is a regression-based machine learning project that analyzes study patterns and predicts final scores.

This project demonstrates:
- Data Analysis (EDA)
- Machine Learning Model Training
- Model Saving using Joblib
- Web Deployment using Flask

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- HTML (Frontend)

---

## 📊 Machine Learning Model

- Algorithm Used: Linear Regression
- Evaluation Metrics:
  - MAE (Mean Absolute Error)
  - MSE (Mean Squared Error)
  - R² Score

---

## 📂 Project Structure

```
SMART-STUDY-PERFORMANCE-PREDICTOR/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── model.pkl
│
├── templates/
│   └── index.html
│
├── data/
│   └── student_scores.csv
│
└── notebooks/
    └── EDA.ipynb
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/Smart-Study-Performance-Predictor.git
cd Smart-Study-Performance-Predictor
```

### 2️⃣ Create virtual environment

```bash
python -m venv .venv
```

Activate environment:

**Windows**
```bash
.venv\Scripts\activate
```

**Mac/Linux**
```bash
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

---

## 🎯 How It Works

1. User enters study hours
2. Model predicts expected final score
3. Result is displayed instantly on web page

---

## 📈 Sample Prediction

Input:
```
Study Hours: 5
```

Output:
```
Predicted Score: 51.23
```

---

## 🧠 Future Improvements

- Add multiple input features (attendance, sleep hours, previous score)
- Improve UI using CSS/Bootstrap
- Deploy using Render/Heroku
- Add Classification (Pass/Fail)

---

## 👨‍💻 Author

Atul Kumar  
Final Year B.Tech CSE Student  
Graphic Era University  

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
