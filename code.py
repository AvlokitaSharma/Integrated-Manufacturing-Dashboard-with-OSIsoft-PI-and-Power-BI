import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_data(days=1, freq='H'):
    base_time = datetime.now() - timedelta(days=days)
    timestamps = pd.date_range(start=base_time, periods=24*days, freq=freq)
    data = {
        'Timestamp': timestamps,
        'MachineID': np.random.choice(['M001', 'M002', 'M003'], size=(24*days)),
        'ProductionRate': np.random.randint(50, 100, size=(24*days)),
        'Downtime': np.random.choice([0, 1], size=(24*days), p=[0.95, 0.05])  # 5% chance of downtime
    }
    return pd.DataFrame(data)

# Generate simulated data for the past 7 days
df = generate_data(days=7)
csv_file = 'simulated_machine_data.csv'
df.to_csv(csv_file, index=False)
print(f"Data saved to {csv_file}.")
