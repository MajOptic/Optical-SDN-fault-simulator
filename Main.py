from flask import Flask, jsonify
import random

app = Flask(__name__)

# Initial network nodes state
network_nodes = {
    "Node_A": {
        "status": "Active",
        "optical_power": 3.5,
        "ber": 0.000000001
    },
    "Node_B": {
        "status": "Active",
        "optical_power": 4.0,
        "ber": 0.000000001
    }
}

# Function to simulate random network faults
def simulate_network_faults():
    hazard = random.choice(["none", "fiber_bend", "laser_failure"])
    
    if hazard == "fiber_bend":
        # Fiber bent: Node_A optical power drops and BER increases
        network_nodes["Node_A"]["optical_power"] = -12.5
        network_nodes["Node_A"]["ber"] = 0.02
        network_nodes["Node_A"]["status"] = "Degraded"
    elif hazard == "laser_failure":
        # Laser failed: Node_B goes down completely
        network_nodes["Node_B"]["optical_power"] = -40.0
        network_nodes["Node_B"]["ber"] = 1.0
        network_nodes["Node_B"]["status"] = "Down"
    else:
        # Network is healthy and back to normal
        network_nodes["Node_A"] = {"status": "Active", "optical_power": 3.5, "ber": 0.000000001}
        network_nodes["Node_B"] = {"status": "Active", "optical_power": 4.0, "ber": 0.000000001}

@app.route('/telemetry', methods=['GET'])
def get_telemetry():
    simulate_network_faults()
    return jsonify(network_nodes)

if __name__ == '__main__':
    print("--- Optical Node Simulator is Running on Port 5000 ---")
    app.run(port=5000)