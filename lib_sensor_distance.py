"""Ultrasonic distance sensor readings and wait-for-object helpers."""

from pybricks.tools import wait, StopWatch

from lib_robot import robot
import lib_config as config


def _sensor_or_raise():
    if robot.distance_sensor is None:
        raise RuntimeError("No distance sensor configured. Set DISTANCE_SENSOR_PORT in config.py.")
    return robot.distance_sensor


def read_distance_mm():
    """Return the measured distance in millimeters. Returns
    config.DISTANCE_NO_OBJECT_MM (2000) if nothing is detected."""
    return _sensor_or_raise().distance()


def object_detected(within_mm):
    """True if an object is detected within `within_mm` millimeters."""
    return read_distance_mm() <= within_mm


def wait_for_object(within_mm, timeout_ms=None):
    """Block until an object is detected within `within_mm`. Returns True
    if detected, False if `timeout_ms` elapsed first."""
    watch = StopWatch()
    while not object_detected(within_mm):
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
    return True


def wait_for_clear(beyond_mm=None, timeout_ms=None):
    """Block until no object is detected within `beyond_mm` (defaults to
    just past the sensor's "no object" reading). Returns True if it
    cleared, False if `timeout_ms` elapsed first."""
    threshold = beyond_mm if beyond_mm is not None else config.DISTANCE_NO_OBJECT_MM
    watch = StopWatch()
    while read_distance_mm() < threshold:
        if timeout_ms is not None and watch.time() >= timeout_ms:
            return False
        wait(10)
    return True
