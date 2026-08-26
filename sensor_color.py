"""Color sensor readings: color detection, reflection (light) intensity,
and simple wait-for conditions used for line/mat detection.

Every function takes an optional `sensor` argument defaulting to
robot.left_color_sensor; pass robot.right_color_sensor to use the second
sensor if your robot has one configured in config.py.
"""

from pybricks.tools import wait, StopWatch

from robot import robot


def _sensor_or_default(sensor):
    chosen = sensor if sensor is not None else robot.left_color_sensor
    if chosen is None:
        raise RuntimeError("No color sensor configured. Set LEFT_COLOR_SENSOR_PORT "
                            "(or pass a sensor explicitly) in config.py.")
    return chosen


def read_color(sensor=None):
    """Return the detected Color (e.g. Color.RED, Color.WHITE, Color.NONE)."""
    return _sensor_or_default(sensor).color()


def read_reflection(sensor=None):
    """Return reflected light intensity as a percentage (0-100)."""
    return _sensor_or_default(sensor).reflection()


def read_ambient(sensor=None):
    """Return ambient light intensity as a percentage (0-100)."""
    return _sensor_or_default(sensor).ambient()


def is_color(color, sensor=None):
    """True if the sensor currently detects the given Color."""
    return read_color(sensor) == color


def wait_for_color(color, sensor=None, timeout_ms=None):
    """Block until the sensor detects `color`. Returns True if it did,
    False if `timeout_ms` elapsed first (None waits forever)."""
    watch = StopWatch()
    while not is_color(color, sensor):
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
    return True


def wait_for_reflection(threshold, above=True, sensor=None, timeout_ms=None):
    """Block until reflection crosses `threshold` (percent).

    above=True waits for reflection() >= threshold (e.g. leaving a dark
    line onto a lighter surface); above=False waits for reflection() <=
    threshold (e.g. arriving at a dark line). Returns True if the
    condition was met, False if `timeout_ms` elapsed first.
    """
    watch = StopWatch()
    while True:
        value = read_reflection(sensor)
        if above and value >= threshold:
            return True
        if not above and value <= threshold:
            return True
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
