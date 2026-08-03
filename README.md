# 🛡️ Phishing URL Detection System

An end-to-end **Machine Learning-based Phishing URL Detection System** that analyzes website URLs and predicts whether they are **Legitimate** or **Phishing** using a trained Scikit-learn Pipeline. The project includes feature extraction, preprocessing, model inference, and a user-friendly web interface.

---

## 📌 Table of Contents

* Overview
* Features
* Project Demo
* Project Architecture
* Machine Learning Pipeline
* Dataset
* Project Structure
* Installation
* Usage
* API/Prediction Flow
* Model Performance
* Technologies Used
* Future Improvements
* Screenshots
* License
* Author

---

# 📖 Overview

Phishing websites attempt to steal sensitive information such as usernames, passwords, banking credentials, and personal information by impersonating legitimate websites.

This project detects phishing websites using **Machine Learning** by extracting important URL and webpage features and predicting whether a URL is safe or malicious.

The application provides:

* URL analysis
* Automatic feature extraction
* ML prediction
* Confidence score
* Easy-to-use interface

---

# ✨ Features

* 🔍 Detects phishing URLs
* 🤖 Machine Learning prediction
* ⚡ Fast prediction
* 📊 Feature preprocessing using Scikit-learn Pipeline
* 📈 Trained classification model
* 🌐 User-friendly web application
* 🧹 Automatic missing value handling
* 📦 End-to-end deployment ready
* 🔄 Reusable prediction pipeline

---

# 🎥 Project Demo

## Input

```text
https://google.com
```

Prediction

```text
Legitimate Website
```

---

Input

```text
http://paypal-login-security-update.xyz
```

Prediction

```text
Phishing Website
```

---

# 🏗️ Project Architecture

```text
                     User URL
                         │
                         ▼
              Feature Extraction
                         │
                         ▼
                Data Preprocessing
                         │
                         ▼
              Trained ML Pipeline
                         │
                         ▼
              Phishing Prediction
                         │
                         ▼
                 Result Display
```

---

# ⚙️ Machine Learning Pipeline

The complete prediction pipeline consists of:

### 1. URL Input

User enters a website URL.

↓

### 2. Feature Extraction

Extracts multiple handcrafted features from the URL and webpage.

Examples include:

* URL Similarity Index
* TLD Probability
* URL Length
* Letter Ratio
* Number of Special Characters
* HTML Features
* JavaScript Count
* External References
* CSS Count
* Image Count
* Domain Title Match
* URL Title Match
* Responsive Website
* Social Media Presence

↓

### 3. Data Preprocessing

* Missing Value Imputation
* Feature Scaling
* One-Hot Encoding
* ColumnTransformer
* Scikit-learn Pipeline

↓

### 4. Model Prediction

The processed features are passed into the trained machine learning model.

↓

### 5. Final Output

Returns:

* Legitimate
* Phishing

---

# 📂 Dataset

Dataset Used:

**PhiUSIIL Phishing URL Dataset**

Dataset includes thousands of phishing and legitimate URLs with engineered numerical and categorical features.

Target Column

```text
label

0 → Legitimate
1 → Phishing
```

---

# 📁 Project Structure

```text
phishing-url-detection/
│
├── app.py
├── predictor.py
├── feature_extractor.py
├── utils.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── models/
│   ├── phishing_decision_tree_pipeline.pkl
│   └── feature_names.json
│
├── assets/
│   └── images/
│       ├── home.png
│       ├── prediction.png
│       └── architecture.png
│
├── notebooks/
│   └── EDA.ipynb
│
└── dataset/
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/phishing-url-detection.git
```

Go into the project folder

```bash
cd phishing-url-detection
```

Create virtual environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

If using Streamlit

```bash
streamlit run app.py
```

If using FastAPI

```bash
uvicorn app:app --reload
```

---

# 🔄 Prediction Workflow

```text
User URL
    │
    ▼
Feature Extraction
    │
    ▼
Data Cleaning
    │
    ▼
Scaling & Encoding
    │
    ▼
Decision Tree Pipeline
    │
    ▼
Prediction
```

---

# 📊 Model Performance

| Metric    | Score |
| --------- | ----: |
| Accuracy  |  100% |
| Precision |  100% |
| Recall    |  100% |
| F1 Score  |  100% |
| ROC-AUC   |  100% |

> **Note:** These results are based on the evaluation performed on the selected dataset and split used during training.

---

# 🛠️ Technologies Used

### Programming

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit
* FastAPI

### Model Serialization

* Joblib

### Version Control

* Git
* GitHub

---

# 📷 Screenshots

## Home Page

Add screenshot here

```text
assets/images/home.png
```

---

## Prediction

Add screenshot here

```text
assets/images/prediction.png
```

---

## Architecture

Add screenshot here

```text
assets/images/architecture.png
```

---

# 🚀 Future Improvements

* Deep Learning models
* Explainable AI (SHAP/LIME)
* Real-time browser extension
* Batch URL prediction
* REST API deployment
* Docker containerization
* CI/CD using GitHub Actions
* Cloud deployment (AWS/Azure/GCP)
* URL reputation integration
* Threat intelligence feeds

---

# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Govardhan Reddy**

* GitHub: https://github.com/YOUR_USERNAME
* LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

## ⭐ Support

If you found this project useful:

⭐ Star this repository

🍴 Fork it

📢 Share it with others

---

> Built with Python, Machine Learning, and Cybersecurity to help detect phishing websites efficiently.
