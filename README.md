# **Efficient Data Stream Anomaly Detection**

## **Overview**
This project implements a Python-based anomaly detection system for continuous data streams, which could represent metrics such as financial transactions, system metrics, or other time-series data. The system simulates a real-time data stream with regular patterns, noise, and injected anomalies, detecting outliers based on statistical methods. The solution is optimized for speed and includes a simple visualization tool to display the data stream along with any detected anomalies.

## **Features**
- **Real-Time Anomaly Detection**: Detects anomalies using a sliding window approach, flagging points that deviate significantly from the norm.
- **Data Stream Simulation**: Generates synthetic data streams with customizable length, noise, seasonality, and injected anomalies.
- **Real-Time Visualization**: Visualizes the data stream and highlights anomalies using `matplotlib`.
- **Optimized for Efficiency**: Sliding window implementation ensures minimal computational overhead for real-time detection.

## **Algorithm**
The anomaly detection uses a **Z-score-based method**. For each incoming data point, the rolling mean and standard deviation of recent values are calculated. If the new value deviates beyond a defined threshold (e.g., 3 standard deviations), it is flagged as an anomaly. This approach adapts to the evolving nature of the stream, making it suitable for real-time scenarios.

## **Installation**

### **Requirements**
- Python 3.x
- `numpy`
- `matplotlib`

### **Step-by-Step Setup**
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/ozy/EfficientDataStreamAnomalyDetection.git
   cd EfficientDataStreamAnomalyDetection
