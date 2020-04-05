import pytest


@pytest.fixture
def simulation():
    from simulation import Simulation
    from datetime import date

    my_simulation: Simulation = Simulation(date.today())
    return my_simulation


def test_tick(simulation):
    assert simulation.current_tick == 0
    simulation.tick()
    assert simulation.current_tick == 1
