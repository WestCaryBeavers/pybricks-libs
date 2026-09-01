"""Small math helpers shared by the movement, sensor, and control modules."""


def normalize_angle(angle_deg):
    """Wrap an angle in degrees to the range [-180, 180)."""
    return ((angle_deg + 180) % 360) - 180


def clamp(value, low, high):
    """Clamp `value` to the inclusive range [low, high]."""
    if value < low:
        return low
    if value > high:
        return high
    return value


def sign(value):
    """Return -1, 0, or 1 depending on the sign of `value`."""
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0
