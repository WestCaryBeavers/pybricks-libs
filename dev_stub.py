"""Desktop-only stub for the `pybricks` package.

Not needed on the robot: the real Pybricks runtime already provides
`pybricks`, so importing this module there is a harmless no-op. It exists so
mission files can be run and sanity-checked with a normal desktop `python3`
interpreter, where `pybricks` doesn't exist.

This file must stay MicroPython-safe at module scope (no `from __future__
import ...`, no unconditional imports of CPython-only modules like `types`)
because the Pybricks compiler bundles it onto the hub too, since it's
imported unconditionally by the mission files. The `types`/`sys` imports
below are deferred into the branch that only runs when the real `pybricks`
package is absent, so nothing CPython-specific ever executes on the hub.

Usage: add a single line before any `pybricks` import in a file you want to
run standalone on a desktop machine:

    import dev_stub  # noqa: F401
    from pybricks.parameters import Stop, Color, Button
    ...

No sys.path setup or PYTHONPATH is required — this only relies on Python's
normal rule that a script's own directory is importable, so it works with
plain `python3 some_mission.py` run from anywhere.
"""

def _install():
    try:
        import pybricks  # noqa: F401
        return
    except ImportError:
        pass

    import sys
    import types

    pybricks_pkg = types.ModuleType("pybricks")
    pybricks_pkg.__path__ = []
    sys.modules["pybricks"] = pybricks_pkg

    def _make_enum(name, members):
        enum_type = type(name, (), {"__slots__": ()})
        for member in members:
            setattr(enum_type, member, member)
        return enum_type

    parameters = types.ModuleType("pybricks.parameters")
    parameters.Port = _make_enum("Port", ["A", "B", "C", "D", "E", "F"])
    parameters.Direction = _make_enum("Direction", ["CLOCKWISE", "COUNTERCLOCKWISE"])
    parameters.Axis = _make_enum("Axis", ["X", "Y", "Z"])
    parameters.Button = _make_enum("Button", ["LEFT", "CENTER", "RIGHT"])
    parameters.Color = _make_enum(
        "Color",
        [
            "RED",
            "GREEN",
            "BLUE",
            "YELLOW",
            "ORANGE",
            "CYAN",
            "MAGENTA",
            "WHITE",
            "BLACK",
            "PURPLE",
            "BROWN",
            "PINK",
        ],
    )
    parameters.Stop = _make_enum("Stop", ["COAST", "BRAKE", "HOLD"])
    sys.modules["pybricks.parameters"] = parameters

    tools = types.ModuleType("pybricks.tools")

    def wait(ms):
        return None

    class StopWatch:
        def time(self):
            return 0

    tools.wait = wait
    tools.StopWatch = StopWatch
    sys.modules["pybricks.tools"] = tools

    hubs = types.ModuleType("pybricks.hubs")

    class PrimeHub:
        def __init__(self, *args, **kwargs):
            self.buttons = types.SimpleNamespace(pressed=lambda: [])
            self.light = types.SimpleNamespace(on=lambda *args, **kwargs: None)
            self.speaker = types.SimpleNamespace(beep=lambda *args, **kwargs: None)
            self.imu = types.SimpleNamespace(
                heading=lambda *args, **kwargs: 0,
                reset_heading=lambda *args, **kwargs: None,
                angular_velocity=lambda *args, **kwargs: (0, 0, 0),
                stationary=lambda *args, **kwargs: True,
            )

    hubs.PrimeHub = PrimeHub
    sys.modules["pybricks.hubs"] = hubs

    pupdevices = types.ModuleType("pybricks.pupdevices")

    class Motor:
        def __init__(self, *args, **kwargs):
            self._angle = 0

        def run_target(self, *args, **kwargs):
            return None

        def run_angle(self, *args, **kwargs):
            return None

        def run_until_stalled(self, *args, **kwargs):
            return 0

        def reset_angle(self, *args, **kwargs):
            return None

        def hold(self, *args, **kwargs):
            return None

        def brake(self, *args, **kwargs):
            return None

        def stalled(self):
            return False

    class ColorSensor:
        def __init__(self, *args, **kwargs):
            pass

    class UltrasonicSensor:
        def __init__(self, *args, **kwargs):
            pass

    class ForceSensor:
        def __init__(self, *args, **kwargs):
            pass

    pupdevices.Motor = Motor
    pupdevices.ColorSensor = ColorSensor
    pupdevices.UltrasonicSensor = UltrasonicSensor
    pupdevices.ForceSensor = ForceSensor
    sys.modules["pybricks.pupdevices"] = pupdevices

    robotics = types.ModuleType("pybricks.robotics")

    class DriveBase:
        def __init__(self, *args, **kwargs):
            self._distance = 0

        def settings(self, *args, **kwargs):
            return (0, 0, 0, 0)

        def use_gyro(self, *args, **kwargs):
            return None

        def straight(self, *args, **kwargs):
            return None

        def turn(self, *args, **kwargs):
            return None

        def arc(self, *args, **kwargs):
            return None

        def drive(self, *args, **kwargs):
            return None

        def reset(self, *args, **kwargs):
            self._distance = 0
            return None

        def stop(self, *args, **kwargs):
            return None

        def distance(self):
            return self._distance

    robotics.DriveBase = DriveBase
    sys.modules["pybricks.robotics"] = robotics


_install()
