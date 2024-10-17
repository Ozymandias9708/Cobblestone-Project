# Main file for the project. Install the dependencies and excute this file

from stream_simulator import generate_data_stream
from anomaly_detector import detect_anomalies
from visualizer import plot_data_with_anomalies

if __name__ == "__main__":
    # Generate simulated data stream
    data_stream = generate_data_stream(length=1000, periodicity=50)
    
    # Perform anomaly detection on the stream
    anomalies = detect_anomalies(data_stream, window=50, z_threshold=3)
    
    # Visualize the data stream with anomalies
    plot_data_with_anomalies(data_stream, anomalies)
