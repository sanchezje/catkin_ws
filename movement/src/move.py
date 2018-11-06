#!/usr/bin/env python
import math
import copy
import rospy
from std_msgs.msg import Twist, PoseStamped, Pose, PoseWithCovariance
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion
import tf
import tf.transformations import euler_from_quaternion



class Robot:

    def __init__(self):
        """"
        Set up the node here

        """
        px
        py
        theta

    def nav_to_pose(self, goal):
        # type: (PoseStamped) -> None
        """
        This is a callback function. It should extract data from goal, drive in a striaght line to reach the goal and
        then spin to match the goal orientation.
        :param goal: PoseStamped
        :return:
        """


    def drive_straight(self, speed, distance):
        """
        Make the turtlebot drive shraight
        :type speed: float
        :type distance: float
        :param speed: speed to drive
        :param distance: distance to drive
        :return:
        """




    def rotate(self, angle):
        """
        Rotate in place
        :param angle: angle to rotate
        :return:
        """
        # check starting Odometry
        # figure out which way to turn
        # while odom < start_angle + theta
        #   turn
        #   send 



    def odom_callback(self, msg):

        """
        update the state of the robot
        :type msg: Odom
        :return:
        """

        px = data.pose.pose.position.x
        py = data.pose.pose.position.y
        quat = data.pose.pose.orientation
        q = [quat.x, quat.y, quat.z, quat.w]
        roll, pitch, yaw = euler_from_quaternion(q)




if __name__ == '__main__':
  pass
