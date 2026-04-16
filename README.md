# 🛡 AI-Powered Phishing URL Detection System

An intelligent cybersecurity application that detects phishing URLs using Machine Learning, advanced feature engineering, and real-time threat intelligence via VirusTotal API.

---

## 🚀 Project Overview

Phishing attacks are one of the most common and dangerous cyber threats, where attackers trick users into visiting fake websites to steal sensitive information.

This project provides a solution by combining:
- Machine Learning (Random Forest)
- Feature Engineering
- External Threat Intelligence (VirusTotal API)

to accurately classify URLs as **Legitimate** or **Phishing** with a confidence score.

---

## 🔍 Key Features

- 🤖 AI-based URL classification  
- 📊 Confidence score for predictions  
- 🔐 Detection of phishing patterns (login, verify, secure, etc.)  
- 🌐 Domain analysis (TLD, subdomain, IP detection)  
- 🔎 URL entropy & randomness detection  
- 🧠 Trusted domain recognition  
- ⚡ VirusTotal API integration (real-time scanning)  
- 🎨 Clean and responsive Flask UI  

---

## 🧠 How It Works

1. User enters a URL  
2. System extracts multiple features:
   - URL length & structure  
   - Special characters & digit ratio  
   - Suspicious keywords  
   - Entropy (randomness of URL)  
   - Domain characteristics  
3. Machine Learning model predicts:
   - **Legitimate (0)**  
   - **Phishing (1)**  
4. VirusTotal API checks the URL externally  
5. Final result is displayed with a confidence score  

---

## 🛠 Tech Stack

- Python  
- Flask  
- Scikit-learn  
- Pandas & NumPy  
- tldextract  
- Requests  
- VirusTotal API  

---

## 📊 Dataset

The model is trained on a custom dataset containing:

- ✅ Legitimate URLs (trusted domains, real-world patterns)  
- ⚠️ Phishing URLs (login scams, fake domains, IP-based attacks)  

Dataset improvements include:
- Root domain variations (`google.com`, `www.google.com`)  
- Realistic phishing patterns (`google-login.com`)  
- Balanced and structured data  

## 📸 Screenshots

### ✅ Legitimate URL Detection
![Legitimate](screenshots/legit)

### ⚠️ Phishing URL Detection
![Phishing](screenshots/phishing)

---

## ▶️ How to Run

### 1. Clone Repository
```bash
git clone https://github.com/your-username/phishing-url-detector.git
cd phishing-url-detector
