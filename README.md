
---

# **README – EnerSynapse: Smart Energy Output Prediction System**

## **Project Overview**

EnerSynapse is a lightweight, AI-powered energy prediction system designed to estimate energy output (kWh) using key electrical and environmental parameters such as Load (kW), Voltage, Current, Temperature, and operational conditions.
The goal is to help users and organizations understand energy behavior in advance, reduce inefficiency, and support informed decision-making through a simple, accurate, and accessible tool.

---

## **Problem Statement**

Modern energy systems generate large amounts of parameter data, but this information is often underutilized.
Many users lack a simple tool that can:

* Predict future energy output
* Help optimize load management
* Reduce operational inefficiencies
* Provide insights without complex dashboards

EnerSynapse solves this by offering a lightweight ML-based prediction system accessible through a clean web interface.

---

## **Project Goal**

The main objective of EnerSynapse is to build a model that:

* Accurately predicts energy output (kWh)
* Works on a simple dataset
* Is easy to deploy using a minimal web app
* Can be used even by non-technical users

---

## **Tools & Technologies Used**

### **Languages & Libraries**

* **Python** → Core development language
* **Pandas & NumPy** → Data cleaning, preprocessing, feature handling
* **Scikit-Learn** → Model training, evaluation, scaling
* **Flask** → Backend server & routing
* **HTML, CSS, Jinja2** → Web interface

### **Development Environment**

* **VS Code** → Code development & debugging

---

## **Methodology (Step-by-Step)**

1. **Dataset Creation**

   * Generated a synthetic dataset representing load, voltage, current, temperature, and energy output.

2. **Data Preprocessing**

   * Handled missing values
   * Scaled features using StandardScaler
   * Extracted relevant columns

3. **Model Development**

   * Tested multiple models
   * Selected the best-performing algorithm
   * Saved the model (`model.pkl`) and scaler (`scaler.pkl`)

4. **Backend Integration**

   * Built Flask routes for input and prediction
   * Integrated the ML model into API endpoints

5. **Frontend UI**

   * Created a simple, clean, responsive HTML-CSS interface
   * Designed input form + result display page

6. **Final Deployment Structure**

   * Organized templates, static files, model files, and server code

---

## **Project Structure**

```
enersynapse/
│_ app.py
│_ model.pkl
│_ scaler.pkl
│_ synthetic_grid_dataset.csv
│
│_ templates/
│     |_ index.html
│     |_ result.html
│
│_ static/
│     |_ style.css
│
│_ README.md
```

## **Conclusion**

EnerSynapse delivers a clean, simple, and efficient solution for predicting energy output using machine learning.
The project demonstrates core concepts of data preprocessing, model deployment, and web integration—making it both useful and easy to extend in the future.

---
