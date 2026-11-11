"""Single-slot mission selector for the shared hub -- right team's and
left team's missions, in one menu, one program, one hub slot.

  1,2,3 = mission_right_team_1/2/3.mission   (right robot)
  4,5,6,7 = mission_left_team_1.mission_1/2/3/4  (left robot)

(mission_right_team_skip.mission, mission_left_team_1.mission_5, and
mission_left_team_1.testing exist but aren't wired into this menu --
ask if you want any of them added as additional keys.)

The hub only has 2 attachment motor ports (C/D), shared between the two
teams' attachments -- see lib_robot_right.py / lib_robot_left.py. Picking
a mission from either range calls that team's activate() first, which
(re)builds robot.front_attachment/back_attachment with the right gear
ratio for that team, tearing down whichever team's motors were built
there before. activate() only updates the SOFTWARE's gear-ratio math --
it can't swap the physical attachment hardware, so mount the matching
team's attachment on the hub before picking a mission for it.

Shows a menu on the hub matrix; you pick a mission with the Bluetooth
button and it runs. Upload only this file as your main program, plus
every `lib_*.py` file and `mission_right_team_*.py`/`mission_left_team_1.py`
as extra files, in the same Pybricks Code project.
"""

import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.tools import hub_menu

from lib_movement_stopping import stop_all
from mission_right_team_1 import mission as mission_1R
from mission_right_team_2 import mission as mission_2R
from mission_right_team_3 import mission as mission_3R
from mission_left_team_1 import (
    mission_1 as mission_1L,
    mission_2 as mission_2L,
)

# hub_menu() only accepts single-character options (it shows one character
# at a time on the hub's 5x5 matrix) -- two-character keys raise
# ValueError: Invalid argument on the real hub.
MISSIONS = {
    "1": mission_1R,
    "2": mission_2R,
    "3": mission_3R,
    "4": mission_1L,
    "5": mission_2L,
}

# The order hub_menu() cycles through on the hub matrix. MicroPython (the
# hub's runtime) doesn't guarantee dict keys iterate back out in the order
# they were written -- unlike desktop CPython -- so MISSIONS.keys() can
# come out scrambled (e.g. "1","7","3","2",...) even though the dict
# literal above is written in order. Spell the display order out
# explicitly instead of relying on dict iteration order.
MISSION_KEYS = ("1", "2", "3", "4", "5")

assert set(MISSION_KEYS) == set(MISSIONS.keys()), (
    "MISSION_KEYS and MISSIONS have drifted apart -- update both together"
)


def run_mission_selector():
    """Show '1'-'7' on the hub matrix (1-3 = right team, 4-7 = left
    team); Bluetooth button cycles, center (the selection made by
    hub_menu) runs the chosen mission. Loops back to the menu after each
    mission finishes instead of letting the program end, so the hub shows
    this menu again rather than falling back to its own pre-launch
    program-picker screen.
    """
    while True:
        selected = hub_menu(*MISSION_KEYS)
        MISSIONS[selected]()
        # Release to coast right away: a mission can leave the drivebase
        # actively HOLDing its last heading (e.g. drive_straight()'s
        # default), and with gyro correction on, an active hold fights any
        # tilt/rotation the gyro senses -- including being picked up by
        # hand between missions, which otherwise spins the wheels. Coast
        # regardless of what the mission itself left running.
        stop_all()


if __name__ == "__main__":
    run_mission_selector()
