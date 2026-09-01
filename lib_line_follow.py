"""Single-sensor edge line following.

Mount one color sensor at the boundary between a dark line and the lighter
mat background. This steers the robot to keep the sensor straddling that
boundary by comparing its reflection() reading against a target midpoint
value and feeding the error into a PID loop that adjusts DriveBase's
turn_rate.

Which way the robot needs to correct depends on which side of the line the
sensor is mounted on. If the robot oscillates or drives away from the line
instead of tracking it, set `edge` to the other side (or negate
config.LINE_FOLLOW_KP).
"""

from lib_robot import robot
import lib_config as config
from lib_pid_controller import PID


def follow_line_for_distance(distance_mm, speed=None, edge="right", sensor=None,
                              target_reflection=None):
    """Follow a line for a straight-line distance of `distance_mm` mm.

    edge="right" assumes the line is to the robot's right (sensor mounted
    on the right side of the line, seeing more white = drifted right, so
    the robot should steer further right to increase turn_rate... use
    edge="left" if your sensor is mounted on the other side and the robot
    steers the wrong way.
    """
    _follow_line(
        stop_condition=lambda: abs(robot.drive_base.distance()) >= abs(distance_mm),
        speed=speed, edge=edge, sensor=sensor, target_reflection=target_reflection,
    )


def follow_line_until(condition_fn, speed=None, edge="right", sensor=None,
                       target_reflection=None):
    """Follow a line until `condition_fn()` returns True (e.g. another
    sensor detects an intersection or an object)."""
    _follow_line(
        stop_condition=condition_fn,
        speed=speed, edge=edge, sensor=sensor, target_reflection=target_reflection,
    )


def _follow_line(stop_condition, speed, edge, sensor, target_reflection):
    drive_base = robot.drive_base
    chosen_sensor = sensor if sensor is not None else robot.left_color_sensor
    if chosen_sensor is None:
        raise RuntimeError("No color sensor configured for line following. Set "
                            "LEFT_COLOR_SENSOR_PORT (or pass a sensor explicitly) in config.py.")

    drive_speed = speed if speed is not None else config.LINE_FOLLOW_SPEED
    target = target_reflection if target_reflection is not None else config.LINE_FOLLOW_EDGE_REFLECTION
    direction = 1 if edge == "right" else -1
    if edge not in ("right", "left"):
        raise ValueError("edge must be 'right' or 'left'")

    pid = PID(
        config.LINE_FOLLOW_KP, config.LINE_FOLLOW_KI, config.LINE_FOLLOW_KD,
        integral_limit=50, output_limits=(-150, 150),
    )
    pid.reset()
    drive_base.reset()

    while not stop_condition():
        error = chosen_sensor.reflection() - target
        turn_rate = direction * pid.update(error)
        drive_base.drive(drive_speed, turn_rate)

    drive_base.stop()
