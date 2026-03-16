# Modular Data Center Digital Twin

This repository implements a simplified digital twin for modular
containerized data centers.  It models capacity (power, cooling,
rack space), simulates component failures, and estimates system
availability under different configurations.  The twin can be used to
evaluate design changes and understand system behavior without
deploying physical hardware.

## Model

Each data center module contains a number of racks, each with a
certain power draw and thermal profile.  The twin tracks the
utilization of power and cooling resources, and simulates failures
such as power supply loss or cooling unit failure.  Monte Carlo
simulation is used to estimate overall uptime.

## Usage

Install dependencies and run the simulation:

```bash
pip install -r requirements.txt
python digital_twin.py --modules 2 --simulation-runs 1000
```

The script prints estimated availability for the given configuration.

## Extending

Add more detailed component models (e.g., UPS, chillers), integrate
real failure statistics, or provide a dashboard to visualize
utilization over time.  You could also connect this simulation to a
live monitoring system for predictive maintenance.