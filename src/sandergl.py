"""
  Capstone Project.  Code written by Garrett Sanders.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()
    forward_for_n_seconds(3, 20)


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()


def run_test_go_stop():
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()

    robot.go(50, 25)
    time.sleep(2)
    robot.stop()

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)


    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())


def forward_for_n_seconds(time_n, duty_cycle):
    """Sets up the function for the robot to move forward for N seconds."""

    robot = rb.Snatch3rRobot

    robot.go(duty_cycle, duty_cycle)
    while True:
        x = time.time()
        if x + time_n == time.time():
            break


main()
