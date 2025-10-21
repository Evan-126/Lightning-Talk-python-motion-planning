import python_motion_planning as pmp

# creates a grid based environment: 51 cells wide and 31 cells tall
env = pmp.Grid(51, 31)
# initializes the set of obstacles (initially empty)
obstacles = env.obstacles

# adds custom obstacles to the grid
for i in range(10, 21):
    obstacles.add((i, 15))
for i in range(15):
    obstacles.add((20, i))
for i in range(15, 30):
    obstacles.add((30, i))
for i in range(16):
    obstacles.add((40, i))
    
# updates the grid environment with new obstacles
env.update(obstacles)

# creates a planner with designated start and goal cells
planner = pmp.AStar(start=(5, 5), goal=(45, 25), env=env)   
cost, path, expand = planner.plan()                        
planner.plot.animation(path, str(planner), cost, expand)    


# creates a 2D map that is 51 cells wide and 31 cells tall
env = pmp.Map(51, 31)

# list of rectangular obstacles [x position, y position, width, height]
obs_rect = [
    [14, 12, 8, 2],
    [18, 22, 8, 3],
    [26, 7, 2, 12],
    [32, 14, 10, 2]
]

# list of circular objects: [x center, y center, radius]
obs_circ = [
    [7, 12, 3],
    [46, 20, 2],
    [15, 5, 2],
    [37, 7, 3],
    [37, 23, 3]
]

# updates the environment to include the obstacles
env.update(obs_rect=obs_rect, obs_circ=obs_circ)

# creates Rapidly-Exploring Random Tree planner
planner = pmp.RRT(start=(18, 8), goal=(37, 18), env=env)    
cost, path, expand = planner.plan()                        
planner.plot.animation(path, str(planner), cost, expand)
