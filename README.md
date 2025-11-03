##  Synthetic Grid Dataset — EnerSynapse Project

The **Synthetic Grid Dataset** is a Python-generated simulation of a smart energy grid designed for AI-based prediction, optimization, and digital-twin modeling.  
It represents realistic operational data from interconnected grid nodes over time — including voltage, current, load, temperature, and probabilistic failures.

###  Purpose
This dataset powers the **EnerSynapse** AI model — a self-learning digital twin that predicts grid faults, optimizes load distribution, and improves reliability across an energy network.  
It was created to mimic real-world energy behavior without relying on private or restricted industrial data.

###  Dataset Overview
| Column | Description |
|:--|:--|
| **Timestamp** | 5-minute interval timestamps starting from 01-Jan-2025 |
| **Node_ID** | Unique identifier for each grid node (N001–N050) |
| **Voltage_V** | Electrical voltage at node (fluctuates around 230 V) |
| **Current_A** | Current drawn at that node, influenced by load |
| **Load_kW** | Active load in kilowatts |
| **Temperature_C** | Node-level temperature affected by load and time |
| **Power_Factor** | Efficiency ratio (0.85 – 1.0 range) |
| **Energy_Output_kWh** | Energy generated or transmitted within each interval |
| **Fault** | Binary indicator (1 = fault event, 0 = normal) |
| **Failure_Risk** | Calculated probability (0 – 1) of system failure |

**Rows:** 10 000  
**Nodes simulated:** 50  
**Sampling interval:** every 5 minutes

###  Generation Logic
The dataset was generated using NumPy and Pandas.  
Randomized fluctuations emulate voltage variation, temperature drift, and rare fault occurrences (≈1 % probability).  
Failure risk is derived using weighted combinations of load, temperature, and fault presence.

###  Example Use Cases
- **Predictive Maintenance:** Train ML models to forecast transformer or line failures.  
- **Load Forecasting:** Use time-series models (LSTM, Prophet) to predict grid demand.  
- **Anomaly Detection:** Detect voltage or current spikes indicating potential faults.  
- **Reinforcement Learning Simulation:** Test AI load-balancing agents safely.

###  How to Regenerate
Run the dataset generator:

📊 [View the Synthetic Grid Dataset](./synthetic_grid_dataset.csv)


```bash
python generate_dataset.py

