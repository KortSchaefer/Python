# Transition from grace to active
scoreboard players set $state wr_state 2
bossbar set water_rising:grace visible false
bossbar set water_rising:level visible true

# Sync level bossbar with marker Y
execute store result bossbar water_rising:level value run scoreboard players get $y wr_y
tellraw @a [{"text":"[Water Rising] ","color":"aqua"},{"text":"Grace over. Water is rising.","color":"white"}]

# Reset interval timer
scoreboard players set $timer wr_timer 0

# Start rise loop in 10 seconds (200t) and clear any previous
schedule clear water_rising:rise_loop
schedule function water_rising:rise_loop 200 replace

# Schedule rewards to begin in 10 minutes (12000t), then repeat every minute
schedule function water_rising:rewards/start 12000 replace
schedule function water_rising:rewards/warn 10800 replace
