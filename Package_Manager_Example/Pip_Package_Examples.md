
# 📦 Python pip Package Examples (With Use Cases)

This guide covers practical examples of commonly used pip-installed Python packages across different domains.

---

## 🌐 Web Development

### 🔸 Flask – Lightweight Web Framework
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
```

### 🔸 Django – Full Stack Web Framework
```bash
pip install django
django-admin startproject mysite
cd mysite
python manage.py runserver
```

### 🔸 FastAPI – High-Performance API (Async)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

---

## 📊 Data Analysis and Science

### 🔸 NumPy – Numerical Computing
```python
import numpy as np

arr = np.array([1, 2, 3])
print(arr.mean())  # Output: 2.0
```

### 🔸 Pandas – DataFrame and CSV Handling
```python
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())
```

### 🔸 Matplotlib – Visualization
```python
import matplotlib.pyplot as plt

plt.plot([1, 2, 3], [4, 5, 6])
plt.title("Simple Plot")
plt.show()
```

### 🔸 Seaborn – Statistical Visualizations
```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
```

---

## 🤖 Machine Learning & AI

### 🔸 scikit-learn – ML Algorithms
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([2, 4, 6])
model = LinearRegression().fit(X, y)
print(model.predict([[4]]))  # Output: [8.0]
```

### 🔸 TensorFlow – Deep Learning
```python
import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, input_shape=(1,))
])
model.compile(optimizer='adam', loss='mse')
model.summary()
```

### 🔸 PyTorch – Deep Learning
```python
import torch

x = torch.tensor([1.0, 2.0])
print(x * 2)  # Output: tensor([2., 4.])
```

---

## 🔍 Web Scraping & Automation

### 🔸 Requests – HTTP Library
```python
import requests

res = requests.get("https://api.github.com")
print(res.status_code)
print(res.json())
```

### 🔸 BeautifulSoup – HTML Parsing
```python
from bs4 import BeautifulSoup
import requests

html = requests.get("https://example.com").text
soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
```

### 🔸 Selenium – Browser Automation
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
print(driver.title)
driver.quit()
```

---

## 📁 Excel and Files

### 🔸 OpenPyXL – Excel Read/Write
```python
from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws["A1"] = "Hello Excel"
wb.save("example.xlsx")
```

---

## 🧪 Testing

### 🔸 Pytest – Advanced Testing
```python
# test_sample.py
def test_add():
    assert 1 + 1 == 2
```

Run: `pytest test_sample.py`

---

## 🛠️ Utility Tools

### 🔸 Python-dotenv – Load .env Files
```python
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("MY_SECRET"))
```

### 🔸 SQLAlchemy – ORM for SQL Databases
```python
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")
conn = engine.connect()
result = conn.execute("SELECT sqlite_version();")
print(result.fetchone())
```

### 🔸 Pygame – Game Development
```python
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Pygame")
```

---

## ✅ Summary

This document demonstrates how to use popular pip packages in web development, data science, machine learning, scraping, automation, and more. Explore and combine them as per your project needs.
