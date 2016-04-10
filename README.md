## The Observer Pattern

Here's a quick implementation of the Observer pattern described by Gamma et al. (1994).

### Context

In the Observer pattern, we have two types of objects; the subject and the observer. It is the role of the subject to track and notify its observers whenever it changes state. It is the role of the observer to update its state accordingly.

To demonstrate this, we introduce a police car as a subject and an ordinary car as an observer. When the police car activates its siren, the ordinary car should stop driving.

To further illustrate the functionality of the observer, we'll introduce a villain that pays no heed to the siren; it'll continue driving regardless.

### Demonstration

```python
from observer_pattern import NormalCar, PoliceCar


# Create the subject.
police = PoliceCar()

# Create several observers.
civilians = [fiesta, polo] = [NormalCar(), NormalCar()]
villain = corsa = NormalCar()

# Subscribe some of the observers to the subject.
for civilian in civilians:
	police.add_observer(civilian)
	
# Activate the siren and check that the civilians have stopped 
# whilst the villain continues driving.
police.activate_siren()
assert not any([civilian.is_driving for civilian in civilians])
assert villain.is_driving

# Deactivate the siren and check that all cars are driving again.
police.deactivate_siren()
assert all([civilian.is_driving for civilian in civilians])
assert villain.is_driving
```

[1] Gamma, E. et al. 1994. *Design patterns: elements of reusable object-oriented software.* Boston: Addison Wesley.