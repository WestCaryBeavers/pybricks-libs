"""Left team's attachment configuration for the shared hub/chassis.

The hub has only 2 attachment motor ports (C/D), shared between the right
team's and the left team's attachments -- only one team's gear train can
be physically mounted on them at a time. This module builds
robot.front_attachment/robot.back_attachment with the left team's gear
ratios; lib_robot_right.py is the mirror image for the right team.

Call activate() at the top of every left-team mission, before touching
robot.front_attachment/back_attachment (or the left_team_* aliases) --
it's a no-op if already active, and otherwise tears down whatever the
right team's module had built there first.

Tearing down calls .close() on the old Motor objects -- Pybricks' own
documented way to free a port so a new Motor can be built on it, added
specifically for this "removable attachment" use case (pybricks-
micropython 3.3.0b1, see
https://docs.pybricks.com/en/stable/pupdevices/motor.html). An earlier
version of this function instead dropped every Python reference and
called gc.collect(), hoping the garbage collector would release the
port as a side effect -- that worked once but then raised EBUSY on a
later switch, since nothing here ever confirmed the port was actually
freed. .close() is explicit and doesn't depend on GC timing or reference
bookkeeping, so use it instead.

IMPORTANT: activate() only changes which gear ratio the software uses for
distance/degree math. It can't swap the physical attachment hardware for
you -- mount the left team's attachment on the hub BEFORE selecting a
left-team mission from the menu.
"""

import lib_config as config
from lib_robot import robot, make_motor


def activate():
    """Make robot.front_attachment/back_attachment the left team's
    motors (built with the left team's gear ratios). Safe to call every
    time a left-team mission starts -- does nothing if already active.
    """
    if robot.active_attachment_team == "left":
        return

    # Explicitly release whatever's currently built on ports C/D (e.g.
    # the right team's motors) before building new ones there.
    if robot.front_attachment is not None:
        robot.front_attachment.close()
    if robot.back_attachment is not None:
        robot.back_attachment.close()
    robot.front_attachment = None
    robot.back_attachment = None
    robot.right_team_front_attachment = None
    robot.right_team_back_attachment = None
    robot.left_team_front_attachment = None
    robot.left_team_back_attachment = None

    robot.front_attachment = make_motor(
        config.FRONT_ATTACHMENT_MOTOR_PORT,
        config.FRONT_ATTACHMENT_MOTOR_DIRECTION,
        config.LEFT_TEAM_FRONT_ATTACHMENT_GEARS,
    )
    robot.back_attachment = make_motor(
        config.BACK_ATTACHMENT_MOTOR_PORT,
        config.BACK_ATTACHMENT_MOTOR_DIRECTION,
        config.LEFT_TEAM_BACK_ATTACHMENT_GEARS,
    )
    robot.left_team_front_attachment = robot.front_attachment
    robot.left_team_back_attachment = robot.back_attachment
    robot.active_attachment_team = "left"
