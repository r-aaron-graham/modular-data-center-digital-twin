# Modular data center digital twin

An illustrative Monte Carlo capacity and failure simulation. Each module
contains ten randomly sized racks and has 120 kW power and cooling capacity.
A trial succeeds when every module fits its capacity and avoids a sampled
failure. Each module has an assumed 1% failure probability per trial.

## Run the example

```bash
python -m pip install -r requirements.txt
python digital_twin.py --modules 2 --simulation-runs 1000 --seed 42
```

The CLI prints the fraction of successful simulated trials. Repeating the
same command and seed reproduces the output. The trial probability has no
specified time interval, so the result is an illustrative scenario measure.
Measured facility availability would need time-based failure and recovery
data.

## Verify

```bash
python -m unittest discover -s tests -v
```

The tests cover reproducible CLI output, invalid parameters, and loads at or above capacity.
A load equal to capacity can operate. Any overload yields zero successful trials.
The model rejects empty facilities, invalid capacities, and invalid rack loads.
