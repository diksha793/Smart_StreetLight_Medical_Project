import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import time

print("--- Smart Street Light Medical Risk Monitoring System ---\n")

# Step 1: Sample dataset generation representing sensor data from different street light poles
np.random.seed(42)
n_samples = 1000

data = {
    'Pole_ID': np.random.randint(101, 150, n_samples),
    'Temperature': np.random.uniform(30.0, 48.0, n_samples), # Celsius
    'Humidity': np.random.uniform(20.0, 90.0, n_samples),     # Percentage
    'AQI': np.random.uniform(50.0, 450.0, n_samples),          # Air Quality Index
    'Hour': np.random.randint(0, 24, n_samples)
}

df = pd.DataFrame(data)

# Step 2: Define Medical Risk Logic (Target Variable Creation)
def calculate_risk(row):
    if row['Temperature'] > 42.0 or row['AQI'] > 350:
        return 2  # High Emergency Risk
    elif (row['Temperature'] > 38.0 and row['Humidity'] > 70) or row['AQI'] > 200:
        return 1  # Moderate Risk
    else:
        return 0  # Normal

df['Medical_Risk'] = df.apply(calculate_risk, axis=1)

# Step 3: Machine Learning Model Training (Classification)
X = df[['Temperature', 'Humidity', 'AQI', 'Hour']]
y = df['Medical_Risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("Model Training Complete!\n")

# Step 4: Real-time Simulation & Automated Medical Alert System
def simulate_street_light_sensor_stream(trained_model):
    print("--- Simulating Live Sensor Stream from Street Light Poles ---")
    
    incoming_readings = [
        {'Pole_ID': 105, 'Temperature': 43.5, 'Humidity': 65.0, 'AQI': 180.0, 'Hour': 14},
        {'Pole_ID': 112, 'Temperature': 34.0, 'Humidity': 45.0, 'AQI': 90.0, 'Hour': 8},
        {'Pole_ID': 120, 'Temperature': 44.0, 'Humidity': 80.0, 'AQI': 380.0, 'Hour': 15}
    ]
    
    for reading in incoming_readings:
        features = [[reading['Temperature'], reading['Humidity'], reading['AQI'], reading['Hour']]]
        prediction = trained_model.predict(features)[0]
        
        print(f"\n[Pole {reading['Pole_ID']}] Reading -> Temp: {reading['Temperature']}°C, Humidity: {reading['Humidity']}%, AQI: {reading['AQI']}")
        
        if prediction == 2:
            print("🚨 HIGH MEDICAL EMERGENCY ALERT! Risk of Heat Stroke / Severe Breathing Issues.")
            print(f"-> Action: Notifying nearest hospital & dispatching emergency medical support to Pole {reading['Pole_ID']} zone.")
        elif prediction == 1:
            print("⚠️ WARNING: Moderate health risk detected for vulnerable citizens.")
        else:
            print("✅ Status Normal. Environment safe.")
        
        time.sleep(1)

# Run the simulation
simulate_street_light_sensor_stream(model)