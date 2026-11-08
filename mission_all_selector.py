"""Single-slot mission selector covering both teams' missions.

Combines the right team's 3 missions (`mission_right_team_1.py`..`_3.py`)
and the left team's 5 missions (`mission_left_team_1.py`'s `mission_1`..
`mission_5`) into ONE program, so all 8 missions share a single hub slot
instead of eight. Shows a menu on the hub matrix; you pick a mission with
the Bluetooth button and it runs.

Set `lib_config.ACTIVE_TEAM` to match whichever team's attachment gear
train is physically mounted on this hub before picking a mission -- each
mission function checks it and refuses to run otherwise (see
`lib_config.require_active_team`).

Upload only this file as your main program (plus every `lib_*.py` file and
the `mission_right_team_*.py`/`mission_left_team_1.py` files it imports
from, as extra files in the same Pybricks Code project).
"""

import dev_stub  # noqa: F401  (desktop-only pybricks stub; no-op on the hub)

from pybricks.tools import hub_menu

import lib_config as config
from mission_right_team_1 import mission as mission_1R
from mission_right_team_2 import mission as mission_2R
from mission_right_team_3 import mission as mission_3R
from mission_left_team_1 import mission_1 as mission_1L, mission_2 as mission_2L, mission_3 as mission_3L, mission_4 as mission_4L, mission_5 as mission_5L

# hub_menu() only accepts single-character options (it shows one character
# at a time on the hub's 5x5 matrix) -- "1R"/"2L"-style two-character keys
# raise ValueError: Invalid argument on the real hub. Plain digits, right
# team first then left team, matches the convention in mission_selector.py
# and mission_left_selector.py. Keys stay the same whichever team is
# active, so a given mission's button digit never changes.
_RIGHT_TEAM_MISSIONS = {
    "1": mission_1R,
    "2": mission_2R,
    "3": mission_3R,
}
_LEFT_TEAM_MISSIONS = {
    "4": mission_1L,
    "5": mission_2L,
    "6": mission_3L,
    "7": mission_4L,
    "8": mission_5L,
}

# Only one team's attachment gear train can be physically mounted (and
# therefore only one team's missions can run correctly) at a time -- see
# lib_config.ACTIVE_TEAM and lib_robot.py. Rather than showing all 8
# missions and relying on require_active_team() to reject a mismatched
# pick after the fact, only ever show the active team's missions, so a
# mismatched mission can't be selected from this menu in the first place.
MISSIONS = _RIGHT_TEAM_MISSIONS if config.ACTIVE_TEAM == "right" else _LEFT_TEAM_MISSIONS


def run_mission_selector():
    """Show the active team's mission keys on the hub matrix (1-3 = right
    team, 4-8 = left team -- whichever set matches lib_config.ACTIVE_TEAM);
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
