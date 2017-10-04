# Simulations

## Artificial Life

A collection of code modelling biological phenomena that intrigue me. Most are implemented using FTDT simulations (Forward-Euler).

#### `reactionDiffusion`:
Simulation of Reaction-Diffusion Equations. The red reacts into blue naturally, and the blue reacts into red by clicking and dragging the black pointer.
![reaction diffusion](https://github.com/dyth/Simulations/blob/master/images/reaction_diffusion.png)

#### `pacemaker.py`: `heart.py`
Synchronisation of neurons over time. This curious phenomenon was described in Sync, by Steven Strogatz.
![pacemaker](https://github.com/dyth/Simulations/blob/master/images/heart.png)

* `vonneumann.py`: self-replicating code.

#### `traffic.py`:
There is an expression `You wait a long time for a London Bus, and then two come along`. In order to prove the validity of the statement, this is a model of traffic patterns. In the graph below, red dots are buses, blue dots are cars and the 'street' the vehicles move along is toroidal -- meaning that there is a conservation of the number of buses and cars.
![bus](https://github.com/dyth/Simulations/blob/master/images/bus.png)

#### `CrowdSimulator1.jar`:
A crowd simulator of predator and prey moving around a 2D world of food and traps. Run using `java World`.

#### `conwayLife.py`:
Pygame implementation.
![game](https://github.com/dyth/Simulations/blob/master/images/game_of_life.png)
