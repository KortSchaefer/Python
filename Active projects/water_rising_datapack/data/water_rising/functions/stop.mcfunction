# Stop flood
scoreboard players set $state wr_state 0
bossbar set water_rising:grace visible false
bossbar set water_rising:level visible false
schedule clear water_rising:rise_loop
tellraw @a [{"text":"[Water Rising] ","color":"aqua"},{"text":"Stopped","color":"white"}]
