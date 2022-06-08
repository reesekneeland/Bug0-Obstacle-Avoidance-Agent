# Bug0-Obstacle-Avoidance-Agent
A simple ROS implementation of a Bug0 obstacle avoidance robot agent.

### How to Run
1. Start **roscore** in a terminal.
2. In another terminal, navigate to the directory containing the world file. In the sample, the file is called bug-test.world.
3. Type the command **rosrun stage_ros stageros bug-test.world**. This will bring up stage with a map with polygonal/non-polygonal obstacles.
4. Run the file with **python3 stage_mover.py <x coordinate> <y coordinate>**, inputting the target coordinates of where the bug should move.

Ex.

"python3 stage_mover.py 15 -10"

### How it works
  
Built on the ROS Noetic framework, we use the publisher/subscriber framework to get telemetry data from the simulated lidar sensor, and when it hits an object, we move along the wall in whichever direction is most open until we are able to move towards our target point again.
