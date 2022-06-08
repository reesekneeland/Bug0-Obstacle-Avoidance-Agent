#!/usr/bin/env python3
"""
 * ROSCPP demo publisher.
 * Sends twist messages for controlling a robot base.
"""

import rospy
import sys
from math import sqrt, pow, atan2, pi
from std_msgs.msg import String
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler


class Bug0():
    def __init__(self, t_x, t_y):
        self.t_x = t_x
        self.t_y = t_y
        print("target: ",t_x,t_y)
        self.x = self.y = self.z = self.roll = self.pitch = self.yaw = 0.0
        rospy.init_node("stage_mover", anonymous=True)
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        self.odom = rospy.Subscriber("/odom", Odometry, self.get_odom)
        self.scan = rospy.Subscriber("/base_scan", LaserScan, self.get_scan)
        self.rate = rospy.Rate(10)
        self.blocked = False
        self.direction = False

    def get_odom (self, msg):
        global roll, pitch, yaw
        orientation_q = msg.pose.pose.orientation
        positions = msg.pose.pose.position
        # print(msg)
        self.x = float(positions.x)
        self.y = float(positions.y)
        orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        self.roll, self.pitch, self.yaw = euler_from_quaternion (orientation_list)
    
    def get_scan(self, msg):
        scanList = msg.ranges
        # print(len(scanList))
        for i in range(len(scanList)):
            if scanList[i] < 0.5:
                rightScan = sum(scanList[0:len(scanList)//2])
                leftScan = sum(scanList[(len(scanList)//2):len(scanList)])
                self.blocked = True
                if(leftScan>rightScan):
                    self.direction = True
                else:
                    self.direction = False
                break
        else:
            self.blocked = False

    def euclidean_distance(self):
        return sqrt(pow((self.t_x - self.x), 2)+pow((self.t_y - self.y), 2))
    
    def angle(self):
        tangle = atan2(self.t_y - self.y, self.t_x - self.x)
        return tangle

    
    def angularvel(self):
        yawngle = self.yaw
        vec = 4 * (self.angle() - yawngle)
        return vec

    def linearvel(self):
        return 2 * (self.euclidean_distance())
    
    def move(self):
        com = Twist()

        # Standard way to run ros code. Will quit if ROS is not OK, that is, the master is dead.
        while not rospy.is_shutdown():
            while self.euclidean_distance() >= 1.0:
                if(self.blocked):
                    if(self.direction):
                        com.angular.z = 0.85
                        com.linear.x = 0.15
                    else:
                        com.angular.z = -1
                        com.linear.x = 0
                else:
                    com.linear.x = self.linearvel()
                    com.angular.z = self.angularvel()
                com.linear.y = 0
                com.linear.z = 0
                    
                com.angular.x = 0
                com.angular.y = 0

                self.cmd_vel_pub.publish(com)
                self.rate.sleep()
                print("target reached!")
            com.linear.x = 0
            com.angular.z = 0
            rospy.spin()

if __name__ == "__main__":
   x = Bug0(float(sys.argv[1]), float(sys.argv[2]))
   x.move()
