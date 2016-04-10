from ..main import NormalCar, PoliceCar

import pytest


class TestObserver():
    def test_observer_behaviour(self):
        police = PoliceCar()
        civilians = [NormalCar() for _ in range(3)]
        villain = NormalCar()

        # Civilians should listen to the siren whereas villains should not.
        for civilian in civilians:
            police.add_observer(civilian)

        police.activate_siren()
        assert not any([civilian.is_driving for civilian in civilians])
        assert villain.is_driving

        police.deactivate_siren()
        assert all([civilian.is_driving for civilian in civilians])
        assert villain.is_driving

