AI-Powered Health Monitoring System

A real-time AI system that monitors health data from wearable devices to detect anomalies and provide personalized health recommendations.


---

📱 Overview

This project uses data from smartwatches and fitness trackers to monitor:

Heart rate

Blood oxygen levels

Activity level
The system analyzes the data to detect abnormal health patterns and generate actionable insights using machine learning.



---

🧩 Key Features

✅ Real-time health data simulation
✅ Anomaly detection using Isolation Forest
✅ Personalized recommendations
✅ Simple Flask web interface
✅ JSON data handling
✅ Designed for mobile or wearable integration (future)


---

📂 Project Structure

📁 ai-health-monitor
├── main.py              # Flask app
├── health_data.json     # Sample health data
├── templates/
│   └── index.html       # Web interface
└── README.md


---

⚙️ How It Works

1. Simulated Data: A script generates mock health data (heart rate, blood oxygen).


2. Anomaly Detection: Isolation Forest is used to classify health status (Normal or Anomaly).


3. Web Interface: Flask serves a page displaying metrics and status.


4. Deployment Ready: Can be hosted on Azure, Replit, or other cloud services.




---

🧠 Tech Stack

Python

Flask

Scikit-learn

Google Colab (for model development)

Replit (for deployment)

GitHub (for version control)



---

🚀 Future Improvements

Integrate with real wearable APIs (e.g., Fitbit, Apple Health)

Use LSTM models for better time-series forecasting

Add user login and historical tracking

Mobile app using Flutter or React Native



---

📌 Getting Started

1. Clone or download this repo


2. Run main.py to start Flask app


3. Visit http://localhost:5000 (or your Replit link)


4. View real-time health status

