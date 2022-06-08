# Bug0-Obstacle-Avoidance-Agent
A simple ROS implementation of a Bug0 obstacle avoidance robot agent.

### How to Run
Run the file with "python3 stage_mover.py <x coordinate> <y coordinate>", 
inputting the target coordinates of where the bug should move.

Ex.

"python3 stage_mover.py 15 -10"

### How it works
  
Built on the ROS Noetic framework, we use the publisher/subscriber framework to get telemetry data from the simulated lidar sensor, and when it hits an object, we move along the wall in whichever direction is most open until we are able to move towards our target point again.
