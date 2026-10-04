# 🧠 Smart Review Intelligence System

## 📌 Overview

Smart Review Intelligence System is a Machine Learning-based sentiment analysis application that analyzes Amazon product reviews and classifies them as **Positive** or **Negative**.

The project uses **TF-IDF for text feature extraction** and **Linear Support Vector Machine (SVM)** for sentiment classification. A Streamlit web application provides an interactive interface for real-time review analysis.

---

## 🎯 Objectives

- Analyze customer reviews automatically
- Classify reviews into Positive and Negative sentiments
- Compare multiple Machine Learning algorithms
- Identify the best-performing sentiment classification model
- Build an interactive Streamlit application
- Create a reusable ML pipeline for deployment

---

## 🗂️ Dataset

The project uses Amazon product review data containing customer review text and sentiment labels.

### Classes

- `pos` → Positive review
- `neg` → Negative review

The dataset was cleaned and preprocessed before training the Machine Learning models.

---

## 🔄 Project Workflow

```text
Amazon Reviews
      ↓
Data Cleaning
      ↓
Train-Test Split
      ↓
TF-IDF Feature Extraction
      ↓
Model Training
      ↓
Model Comparison
      ↓
Linear SVM Selection
      ↓
Evaluation
      ↓
Pipeline Creation
      ↓
Streamlit Application