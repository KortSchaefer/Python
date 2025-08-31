# Active rising logic

# Progress timer
scoreboard players add $timer wr_timer 1

# When timer reaches interval, rise
execute if score $timer wr_timer >= $interval wr_interval run function water_rising:raise_water
# After 30 layers, raise a second block each interval
execute if score $timer wr_timer >= $interval wr_interval if score $raised wr_raised matches 30.. run function water_rising:raise_water
# Reset timer
execute if score $timer wr_timer >= $interval wr_interval run scoreboard players set $timer wr_timer 0
