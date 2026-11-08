"""Right team's attachment configuration for the shared hub/chassis.

The hub has only 2 attachment motor ports (C/D), shared between the right
team's and the left team's attachments -- only one team's gear train can
be physically mounted on them at a time. This module builds
robot.front_attachment/robot.back_attachment with the right team's gear
ratios; lib_robot_left.py is the mirror image for the left team.

Call activate() at the top of every right-team mission, before touching
robot.front_attachment/back_attachment (or the right_team_* aliases) --
it's a no-op if they're already active, and otherwise tears down whatever
the left team's module had built there first.

IMPORTANT: activate() only changes which gear ratio the software uses for
distance/degree math. It can't swap the physical attachment hardware for
you -- mount the right team's attachment on the hub BEFORE selecting a
right-team mission from the menu.
"""

import gc

import lib_config as config
from lib_robot import robot, make_motor


def activate():
    """Make robot.front_attachment/back_attachment the right team's
    motors (built with the right team's gear ratios). Safe to call every
    time a right-team mission starts -- does nothing if already active.
    """
    if robot.active_attachment_team == "right":
        return

    # Drop whatever's currently built on ports C/D (e.g. the left team's
    # Motor objects) and let the garbage collector actually release them
    # before building new ones on the same ports -- Pybricks won't let a
    # port back a second live Motor object.
    robot.front_attachment = None
    robot.back_attachment = None
    gc.collect()

    robot.front_attachment = make_motor(
        config.FRONT_ATTACHMENT_MOTOR_PORT,
        config.FRONT_ATTACHMENT_MOTOR_DIRECTION,
        config.RIGHT_TEAM_FRONT_ATTACHMENT_GEARS,
    )
    robot.back_attachment = make_motor(
        config.BACK_ATTACHMENT_MOTOR_PORT,
        config.BACK_ATTACHMENT_MOTOR_DIRECTION,
        config.RIGHT_TEAM_BACK_ATTACHMENT_GEARS,
    )
    robot.right_team_front_attachment = robot.front_attachment
    robot.right_team_back_attachment = robot.back_attachment
    robot.left_team_front_attachment = None
    robot.left_team_back_attachment = None
    robot.active_attachment_team = "right"
