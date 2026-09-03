from pybricks.tools import hub_menu



# Display letters or numbers on the hub matrix
selected = hub_menu("1", "2", "3", "4")

if selected == "1":
    from mission_right_team_1 import mission as mission_right_1
    mission_right_1()
elif selected == "2":
    from mission_left_team_1 import mission as mission_left_1
    mission_left_1()
