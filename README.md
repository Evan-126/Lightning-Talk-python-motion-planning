# Lightning-Talk-python-motion-planning

# Path & Motion Planning in Python

This repository demonstrates Python-based grid and map path planning using the **python_motion_planning** library. It provides modular examples for discrete environments and supports multiple planners including A* and RRT.

---

## Features

- **Grid and map-based motion planning**
- **Discrete obstacle placement** (custom points, rectangles, circles)
- **Visual animation** of computed paths
- Supports multiple algorithms:
  - **A\*** (graph search)
  - **Rapidly-Exploring Random Tree (RRT)** (sampling-based search)
- **Modular design** for easy experimentation and extension

---

## Requirements

- **Python >= 3.6**
- `python_motion_planning` v2.0.dev1

**Recommended install method:** [conda](https://docs.conda.io/en/latest/)

```
conda create -n pmp python=3.10
conda activate pmp
```

Then install the package:

```
pip install python-motion-planning==2.0.dev1

```

---

## How to Run

1. **Clone or download this repo.**
2. **Ensure all dependencies are installed.**
3. **Run your desired script** (see Code Overview) using Python:

```
import python_motion_planning as pmp
```
# Create a grid-based environment (51x31 cells)
```
env = pmp.Grid(51, 31)
obstacles = env.obstacles
```
# Add obstacles (discrete points)
```
for i in range(10, 21):
obstacles.add((i, 15))
for i in range(15):
obstacles.add((20, i))
for i in range(15, 30):
obstacles.add((30, i))
for i in range(16):
obstacles.add((40, i))
env.update(obstacles)
```
# Plan with A*
```
planner = pmp.AStar(start=(5, 5), goal=(45, 25), env=env)
cost, path, expand = planner.plan()
planner.plot.animation(path, str(planner), cost, expand)
```
# Create a map (rectangle + circle obstacles)
```
env = pmp.Map(51, 31)
obs_rect = [
    [14, 12, 8, 2],
    [18, 22, 8, 3],
    [26, 7, 2, 12],
    [32, 14, 10, 2]
]
obs_circ = [
    [7, 12, 3],
    [46, 20, 2],
    [15, 5, 2],
    [37, 7, 3],
    [37, 23, 3]
]
env.update(obs_rect=obs_rect, obs_circ=obs_circ)
```
# Plan with RRT
```
planner = pmp.RRT(start=(18, 8), goal=(37, 18), env=env)
cost, path, expand = planner.plan()
planner.plot.animation(path, str(planner), cost, expand)
```


- **Grid Environment:** Instantiates a 2D grid; obstacles are specified via point coordinates.
- **Map Environment:** Allows rectangular and circular obstacles for more complex layouts.
- **Planning Algorithms:** Plug-and-play planners, including A* for discrete search and RRT for sampling-based exploration.
- **Visualization:** Plots and animates the planned path.

---

## Parameters

**Planners generally accept:**
- `start`: `(x, y)` tuple for starting position
- `goal`: `(x, y)` tuple for goal
- `env`: environment instance (grid or map)

**Environment setup:**
- For `Grid`, use `.obstacles` to add discrete points.
- For `Map`, supply `obs_rect` and `obs_circ` lists with obstacle parameters.

---

## Output

- **Animated visualization** of the computed path
- **Route details:** path, cost, and node expansion

---

## About the Library

`python_motion_planning` offers implementations for a variety of classic path planning algorithms used in robotics and automation, including:
- A*, Dijkstra, Theta*, RRT, RRT*
- Advanced planner support (JPS, D*, LPA*, Voronoi, etc.)
- 2D simulation and visualization tools

More details and documentation:
- [Documentation](https://ai-winter.github.io/python_motion_planning/)
- [Original repository](https://github.com/ai-winter/python_motion_planning)

---

## License

Distributed under the **GNU GPL-3.0 License**.

---




