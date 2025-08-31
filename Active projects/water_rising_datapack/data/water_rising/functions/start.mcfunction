# Start grace via trigger or op
scoreboard players set $state wr_state 1
scoreboard players set $timer wr_timer 6000
scoreboard players set $raised wr_raised 0
scoreboard players set $y wr_y 62
bossbar set water_rising:grace visible true
bossbar set water_rising:grace value 6000

# Set world border when starting
worldborder center 8 8
worldborder set 48

tellraw @a [{"text":"[Water Rising] ","color":"aqua"},{"text":"Grace period started (5:00)","color":"white"}]
