"""Direct access to the hub's built-in IMU (gyro + accelerometer).

The drivebase movements in movement_straight.py / movement_turning.py
already use the gyro internally via DriveBase.use_gyro(True) — you don't
need anything from this file just to drive straight or turn accurately.
Use these functions when a mission needs the raw heading or motion state
directly, e.g. to check the robot settled before reading a sensor, or to
log/debug heading drift.
"""

from pybricks.tools import wait, StopWatch

from robot import robot


def heading():
    """Current heading in degrees. Positive is clockwise from whatever
    heading was 0 when the gyro was last reset (see reset_heading)."""
    return robot.hub.imu.heading()


def reset_heading(angle=0):
    """Reset the IMU heading to a known value (typically 0 at the start of
    a run, right after placing the robot on the mat).

    DriveBase blocks resetting the heading while gyro-assisted driving is
    active, so this briefly disables use_gyro, resets, and re-enables it.
    """
    robot.drive_base.use_gyro(False)
    robot.hub.imu.reset_heading(angle)
    robot.drive_base.use_gyro(True)


def angular_velocity(axis=None):
    """Current rotation rate in degrees/second. Pass an Axis (e.g.
    Axis.Z) for a single axis, or leave as None for the (x, y, z) vector.
    """
    return robot.hub.imu.angular_velocity(axis) if axis is not None else robot.hub.imu.angular_velocity()


def is_stationary():
    """True if the hub has been physically still for about a second."""
    return robot.hub.imu.stationary()


def wait_until_stationary(timeout_ms=None):
    """Block until the robot is stationary, e.g. right after placing it on
    the mat, to make sure the gyro has settled before a run starts.
    Returns True if it settled, False if `timeout_ms` elapsed first.
    """
    watch = StopWatch()
    while not is_stationary():
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
    return True
