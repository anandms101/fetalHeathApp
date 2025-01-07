# fetalHeathApp
 
# **Fetal Health Classification App**

A Streamlit-based web application for predicting fetal health using machine learning. This app classifies fetal health into three categories: **Normal**, **Suspect**, and **Pathological** based on input features derived from Cardiotocogram (CTG) data.

---

## **Project Overview**

This web app utilizes a trained Random Forest model to provide predictions on fetal health. The features include baseline fetal heart rate, accelerations, fetal movement, uterine contractions, and histogram-based metrics. The app is designed to assist in early detection and diagnosis of fetal health conditions.

For the full implementation of the model training pipeline, visit the [Fetal Health Model Training Repository](https://github.com/anandms101/fetal-health-classification).

---

## **Live Demo**

You can access the live application [here](https://fetalhealthcheck.streamlit.app/).

---

## **Features**

- **Interactive Input Form**: Users can input specific fetal health metrics.
- **Real-Time Predictions**: Outputs the predicted fetal health category: `Normal`, `Suspect`, or `Pathological`.
- **User-Friendly Design**: Intuitive interface built using Streamlit.
- **Scalable and Portable**: Easily deployable on various cloud platforms.

---

## **Model Overview**

The app uses a **Random Forest Classifier**, trained on the [Fetal Health Classification Dataset](https://www.kaggle.com/datasets/andrewmvd/fetal-health-classification). The model achieved:
- **Accuracy**: 95.3%
- **ROC-AUC Score**: 0.97

Detailed model training, data preprocessing, and hyperparameter optimization steps are available in the [Model Training Repository](https://github.com/anandms101/fetal-health-classification).

---

## **Installation**

To run the app locally, follow these steps:

### **1. Clone the Repository**
```bash
git clone https://github.com/anandms101/fetalHealthApp.git
cd fetalHealthApp
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the App**
```bash
streamlit run app.py
```
