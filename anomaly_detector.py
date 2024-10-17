# python file to detect the existence of anomaly in the stream

from collections import deque # Will be using dequeue to store the data points
import numpy as np 

def detect_anomalies(stream_data, window=50, z_threshold=3):
    mean_window = deque(maxlen=window)  # Fixed-size window to store recent data points
    detected_anomalies = []
    
    for current_index, current_value in enumerate(stream_data):   # iterating over stream
        if len(mean_window) == window:
            current_mean = np.mean(mean_window)
            current_std = np.std(mean_window)
            
            # Check if current value is beyond threshold (Z-score method)
            if abs(current_value - current_mean) > z_threshold * current_std:
                detected_anomalies.append((current_index, current_value))
                
        mean_window.append(current_value)  # Update sliding window with the current data point
    
    return detected_anomalies
