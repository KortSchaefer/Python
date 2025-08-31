# Water Rising - load

# Scoreboards
scoreboard objectives add wr_state dummy
scoreboard objectives add wr_timer dummy
scoreboard objectives add wr_interval dummy
scoreboard objectives add wr_raised dummy
scoreboard objectives add wr_y dummy
scoreboard objectives add wr_start trigger

# Enable trigger for all players
scoreboard players enable @a wr_start

# Defaults
scoreboard players set $interval wr_interval 200
scoreboard players set $state wr_state 0
scoreboard players set $raised wr_raised 0
scoreboard players set $y wr_y 62

# Bossbars
bossbar add water_rising:grace "Grace Period"
bossbar set water_rising:grace max 6000
bossbar set water_rising:grace visible false
bossbar set water_rising:grace color blue
bossbar set water_rising:grace style notched_20

bossbar add water_rising:level "Water Level"
bossbar set water_rising:level max 309
bossbar set water_rising:level visible false

# Forceload 3x3 chunks (-1..1)
forceload add -1 -1 1 1

# No marker entity needed; using scoreboard-driven Y

# Help
tellraw @a [{"text":"[Water Rising] ","color":"aqua"},{"text":"Loaded. Use /trigger wr_start set 1","color":"white"}]
