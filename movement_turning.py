"""Turning movements: in-place turns, absolute heading turns, arcs with a
specified radius, and pivot turns around a single wheel.

All go through DriveBase with gyro correction enabled (see robot.py), so
turns land on the commanded angle instead of drifting with wheel slip.

Sign convention (matches DriveBase, and the hub's IMU heading()):
    Positive angle / turn_rate = clockwise, viewed from above (turns right).
    Negative angle / turn_rate = counterclockwise (turns left).
For arc()/pivot_turn, a positive radius means the circle's center is to the
robot's right; negative means the center is to the robot's left.
"""

from pybricks.parameters import Stop

from robot import robot
import config


def turn_in_place(angle_deg, then=Stop.HOLD, wait=True):
    """Rotate in place by `angle_deg` degrees relative to the robot's
    current heading. Positive turns right (clockwise), negative turns left.
    """
    robot.drive_base.turn(angle_deg, then=then, wait=wait)


def turn_to_heading(target_heading_deg, then=Stop.HOLD, wait=True):
    """Rotate in place to an absolute heading in degrees, as reported by
    the hub's IMU (0 = the heading when the gyro was last reset/started).
    Use this instead of turn_in_place when you know where you want to point
    rather than how far you want to rotate from wherever you currently are.
    """
    robot.drive_base.turn(target_heading_deg, then=then, wait=wait, absolute=True)


def turn_with_radius(radius_mm, angle_deg=None, distance_mm=None, then=Stop.HOLD, wait=True):
    """Drive an arc along a circle of `radius_mm`, for either `angle_deg`
    degrees of rotation or `distance_mm` of travel along the arc (give
    exactly one of the two).

    Positive radius curves to the right (circle center to the right of the
    robot), negative curves to the left. A very large radius approximates a
    gentle curve; radius_mm == AXLE_TRACK_MM / 2 pivots exactly around one
    wheel (see pivot_turn for a convenience wrapper).
    """
    if (angle_deg is None) == (distance_mm is None):
        raise ValueError("turn_with_radius: pass exactly one of angle_deg or distance_mm")
    robot.drive_base.arc(radius_mm, angle=angle_deg, distance=distance_mm, then=then, wait=wait)


def pivot_turn(angle_deg, pivot="right", then=Stop.HOLD, wait=True):
    """Turn in place around one wheel, keeping it (approximately)
    stationary while the other wheel swings around it.

    pivot="right" keeps the right wheel planted (left wheel does the
    moving); pivot="left" keeps the left wheel planted. `angle_deg` uses the
    same sign convention as turn_in_place: positive = clockwise/right,
    negative = counterclockwise/left, regardless of which wheel is planted.
    """
    radius = config.AXLE_TRACK_MM / 2
    if pivot == "right":
        robot.drive_base.arc(radius, angle=angle_deg, then=then, wait=wait)
    elif pivot == "left":
        robot.drive_base.arc(-radius, angle=angle_deg, then=then, wait=wait)
    else:
        raise ValueError("pivot_turn: pivot must be 'right' or 'left'")
