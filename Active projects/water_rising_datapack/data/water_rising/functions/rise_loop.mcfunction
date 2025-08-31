# Water rising loop (runs every 10 seconds while active)

# Only operate while active (state 2) and while Y <= 309
execute if score $state wr_state matches 2 if score $y wr_y matches ..309 run function water_rising:raise_water
execute if score $state wr_state matches 2 if score $raised wr_raised matches 30.. if score $y wr_y matches ..309 run function water_rising:raise_water

# Reschedule if still active (200t) and not at max height
execute if score $state wr_state matches 2 if score $y wr_y matches ..309 run schedule function water_rising:rise_loop 200
