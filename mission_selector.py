"""Single-slot mission selector for the right-team robot.

This robot's codebase defines 4 missions, one `mission()` function per
`mission_right_team_1.py`..`mission_right_team_4.py` file. Rather than
uploading each as its own program (and burning a separate hub slot per
mission, with only 5 slots total on the hub), this file is the ONE program
you upload: it shows a menu on the hub matrix, you pick a mission with the
Bluetooth button, and it runs.

Upload only this file as your main program (plus every `lib_*.py` file and
the `mission_right_team_*.py` files it imports from, as extra files in the
same Pybricks Code project) -- that's a single hub slot covering all 4
missions.
"""

import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.tools import hub_menu

import lib_config as config
from mission_right_team_1 import mission as mission_1
from mission_right_team_2 import mission as mission_2
from mission_right_team_3 import mission as mission_3
from mission_left_team_1 import mission_1 as mission_4, mission_2 as mission_5, mission_3 as mission_6

_RIGHT_TEAM_MISSIONS = {
    "1": mission_1,
    "2": mission_2,
    "3": mission_3,
}
_LEFT_TEAM_MISSIONS = {
    "4": mission_4,
    "5": mission_5,
    "6": mission_6,
}

# Only one team's attachment gear train can be physically mounted (and
# therefore only one team's missions can run correctly) at a time -- see
# lib_config.ACTIVE_TEAM and lib_robot.py. Only ever show the active
# team's missions, so a mismatched mission can't be selected from this
# menu in the first place.
MISSIONS = _RIGHT_TEAM_MISSIONS if config.ACTIVE_TEAM == "right" else _LEFT_TEAM_MISSIONS


def run_mission_selector():
    """Show the active team's mission keys on the hub matrix (1-3 = right
    team, 4-6 = left team -- whichever set matches lib_config.ACTIVE_TEAM);
    Bluetooth button cycles, center (the selection made by hub_menu) runs
    the chosen mission. Loops back to the menu after each mission finishes
    instead of letting the program end, so the hub shows this menu again
    rather than falling back to its own pre-launch program-picker screen.
    """
    while True:
        selected = hub_menu(*MISSIONS.keys())
        MISSIONS[selected]()


if __name__ == "__main__":
    run_mission_selector()
