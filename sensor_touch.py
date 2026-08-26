"""Force/touch sensor readings and wait-for-press helpers."""

from pybricks.tools import wait, StopWatch

from robot import robot
import config


def _sensor_or_raise():
    if robot.touch_sensor is None:
        raise RuntimeError("No touch/force sensor configured. Set TOUCH_SENSOR_PORT in config.py.")
    return robot.touch_sensor


def get_force():
    """Return the force currently applied to the sensor, in newtons."""
    return _sensor_or_raise().force()


def get_travel_mm():
    """Return how far the sensor's button has been pushed in, in mm."""
    return _sensor_or_raise().distance()


def is_pressed(force_threshold=None):
    """True if the sensor is pressed with at least `force_threshold`
    newtons (defaults to config.TOUCH_DEFAULT_FORCE_N)."""
    threshold = force_threshold if force_threshold is not None else config.TOUCH_DEFAULT_FORCE_N
    return _sensor_or_raise().pressed(threshold)


def is_touched():
    """True if the sensor detects any contact at all, even below the
    force threshold used by is_pressed()."""
    return _sensor_or_raise().touched()


def wait_for_press(force_threshold=None, timeout_ms=None):
    """Block until the sensor is pressed. Returns True if pressed, False
    if `timeout_ms` elapsed first."""
    watch = StopWatch()
    while not is_pressed(force_threshold):
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
    return True


def wait_for_release(force_threshold=None, timeout_ms=None):
    """Block until the sensor is no longer pressed. Returns True if
    released, False if `timeout_ms` elapsed first."""
    watch = StopWatch()
    while is_pressed(force_threshold):
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
    return True
