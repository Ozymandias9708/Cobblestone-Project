# Python file for genrating stream

import numpy as np

def generate_data_stream(length=1000, periodicity=50):
    base_pattern = np.sin(np.linspace(0, length, num=length) / periodicity)  # Sinusoidal base trend
    random_noise = np.random.normal(0, 0.5, length)  # Gaussian noise for realism
    anomaly_flags = np.random.choice([0, 1], size=length, p=[0.98, 0.02])  # Randomly generate anomalies
    anomaly_magnitude = anomaly_flags * np.random.uniform(5, 10, size=length)  # Anomalies with large values
    data_stream = base_pattern + random_noise + anomaly_magnitude
    return data_stream
