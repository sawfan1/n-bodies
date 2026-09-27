N-body simulation in pygame

The bodies have individual positions, velocities, and masses. The function in `helpers.py` help to determine a unique radius and color for each selection of mass.

The physics is Newtonian (Newton's Law of Gravitation) but the attractive forces get stronger with distance after the bodies are seperated a certain distance. The bodies reflect off of the window walls as well (the velocity components are negated: multiplied with -1 so that the colliding bodies move the opposite way)

I use the `pygame-ce` version of pygame which is supported on Python 3.14. That's it really.
