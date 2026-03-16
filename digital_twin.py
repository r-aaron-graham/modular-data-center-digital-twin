"""Digital twin simulation for modular data centers."""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import List

import click


@dataclass
class Rack:
    power_kw: float
    thermal_kw: float


@dataclass
class Module:
    racks: List[Rack]
    power_capacity_kw: float
    cooling_capacity_kw: float

    def utilization(self) -> float:
        total_power = sum(r.power_kw for r in self.racks)
        total_thermal = sum(r.thermal_kw for r in self.racks)
        power_util = total_power / self.power_capacity_kw
        thermal_util = total_thermal / self.cooling_capacity_kw
        return max(power_util, thermal_util)

    def is_failed(self) -> bool:
        # Simple random failure model: module fails with 1% probability
        return random.random() < 0.01


def simulate(modules: List[Module], runs: int = 1000) -> float:
    """Monte Carlo simulation of availability.

    Returns the estimated fraction of runs where the data center remains
    operational (i.e. no module failures and utilization < 1).
    """
    successes = 0
    for _ in range(runs):
        all_ok = True
        for module in modules:
            if module.is_failed() or module.utilization() > 1.0:
                all_ok = False
                break
        if all_ok:
            successes += 1
    return successes / runs


def build_modules(num_modules: int) -> List[Module]:
    modules: List[Module] = []
    for _ in range(num_modules):
        racks = [Rack(power_kw=random.uniform(5, 10), thermal_kw=random.uniform(5, 10)) for _ in range(10)]
        module = Module(racks=racks, power_capacity_kw=120.0, cooling_capacity_kw=120.0)
        modules.append(module)
    return modules


@click.command()
@click.option("--modules", type=int, default=1, show_default=True, help="Number of modules to simulate.")
@click.option("--simulation-runs", type=int, default=1000, show_default=True, help="Number of Monte Carlo runs.")
def main(modules: int, simulation_runs: int) -> None:
    data_center = build_modules(modules)
    availability = simulate(data_center, runs=simulation_runs)
    click.echo(f"Estimated availability: {availability * 100:.2f}%")


if __name__ == "__main__":  # pragma: no cover
    main()