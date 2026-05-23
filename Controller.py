import urllib.request
import json
import time

API_URL = "http://127.0.0.1:5000/telemetry"

print("--- SDN Central Controller Started. Monitoring Optical Network... ---")
print("-" * 65)

while True:
    try:
        # 1. Fetch telemetry data from the Optical Node API
        with urllib.request.urlopen(API_URL) as response:
            data = json.loads(response.read().decode())
            
        # 2. Parse and analyze data for each node
        for node_name, info in data.items():
            status = info["status"]
            power = info["optical_power"]
            ber = info["ber"]
            
            # 3. Fault monitoring and real-time alerts
            if status == "Degraded":
                print(f"?? [ALERT] {node_name} is Degraded! Low Power: {power}dBm | High BER: {ber}")
            elif status == "Down":
                print(f"?? [CRITICAL] {node_name} is DOWN! Signal Lost: {power}dBm")
            else:
                print(f"? {node_name}: Status is Stable and Normal.")
                
        print("-" * 65)
        
    except Exception as e:
        print("Connection Error! Is the Optical Node Simulator running?")
        
    # Poll the network state every 3 seconds
    time.sleep(3)