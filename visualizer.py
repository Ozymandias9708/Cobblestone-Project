# Python file for visualziing the results

import matplotlib.pyplot as plt

def plot_data_with_anomalies(data_stream, anomalies):
    plt.plot(data_stream, label="Data Stream")
    
    if anomalies:
        anomaly_indices, anomaly_values = zip(*anomalies)  # Unpack anomaly positions and values
        plt.scatter(anomaly_indices, anomaly_values, color='red', label="Detected Anomalies")  # Highlight anomalies
    
    plt.title("Real-Time Data Stream with Detected Anomalies")
    plt.legend()
    plt.show()
