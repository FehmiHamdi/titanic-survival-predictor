# 🚢 Titanic Survival Predictor

This project predicts whether a passenger would survive the Titanic disaster using a machine learning model trained in a Google Colab notebook, and deployed via a **FastAPI** backend. A simple web frontend is provided for user interaction.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1xpeY8_nUaa3SiA4CU2K7QBVZo3O8cUrn#scrollTo=QLiru92VO53r)

---

## 📁 Project Structure

```
titanic-survival-predictor/
├── app.py                        # FastAPI backend
├── titanic_model.pkl             # Trained model
├── index.html                   # Web interface
└── README.md
```

---

## 🧠 Features Used in the Model

- `Pclass`: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)
- `Sex`: Encoded (0 = Female, 1 = Male)
- `Age`: Age in years
- `SibSp`: Number of siblings/spouses aboard
- `Parch`: Number of parents/children aboard
- `Fare`: Passenger fare
- `Cabin`: Encoded cabin number
- `Embarked`: Encoded (0 = Cherbourg, 1 = Queenstown, 2 = Southampton)

---

## 🧪 Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/FehmiHamdi/titanic-survival-predictor.git
cd titanic-survival-predictor
```

### 2. Install Dependencies

```bash
pip install fastapi uvicorn joblib scikit-learn
```

### 3. Start FastAPI Backend

```bash
uvicorn app:app --reload
```

Open the interactive API docs at:  
👉 http://127.0.0.1:8000/docs

### 4. Run the Frontend

```bash
python -m http.server 8080
```

Open in browser:  
👉 http://localhost:8080

---

## 📓 Model Training

To understand or modify how the model was built and trained, check the Colab notebook:  
▶️ [Open in Google Colab](https://colab.research.google.com/drive/1xpeY8_nUaa3SiA4CU2K7QBVZo3O8cUrn#scrollTo=QLiru92VO53r)

---


## 🛠 Technologies Used

- Python
- Scikit-Learn
- FastAPI
- Google Colab
- HTML + JavaScript

---

## 📜 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share.

