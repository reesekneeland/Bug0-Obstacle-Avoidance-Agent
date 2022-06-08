# Bug0-Obstacle-Avoidance-Agent
A simple ROS implementation of a Bug0 obstacle avoidance robot agent.

### How to Run
1. Start **roscore** in a terminal.
2. In another terminal, navigate to the directory containing the world file. In the sample, the file is called bug-test.world.
3. Type the command **rosrun stage_ros stageros bug-test.world**. This will bring up stage with a map with polygonal/non-polygonal obstacles.
4. Run the file with **python3 stage_mover.py (x coordinate) (y coordinate)**, inputting the target coordinates of where the bug should move.

Ex.

"python3 stage_mover.py 15 -10"

### Background
The insect-inspired Bug algorithms attempt to mimic the motion of bugs to create robot navigation algorithms. There are variants of this algorithm, and our focus for this project would be the Bug-0 version. Specifically, the Bug-0 algorithm attempts to navigate to a goal location by following a straight-line path from its current position to the goal. The robot is assumed to have limited local sensing only, so it is not aware of a (a) global map, or (b) obstacles along the path unless it is very close and directly in its path. When a robot encounters an obstacle, it attempts to go around it, until there is free space along the straight line from its position to the goal; at that time, the robot starts to navigate towards the goal along this line. The Bug-0 algorithm thus attempts to:
1. head towards goal,
2. follow obstacles until you can head towards the goal again, and
3. continue until goal is reached.

### How it works
  
Built on the ROS Noetic framework, we use the publisher/subscriber framework to get telemetry data from the simulated lidar sensor, and when it hits an object, we move along the wall in whichever direction is most open until we are able to move towards our target point again.
