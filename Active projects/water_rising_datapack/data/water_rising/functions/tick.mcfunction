# Water Rising - tick

# Handle player trigger to start
execute as @a[scores={wr_start=1..}] run function water_rising:start
scoreboard players set @a[scores={wr_start=1..}] wr_start 0

# Keep bossbars assigned to all players each tick
bossbar set water_rising:grace players @a
bossbar set water_rising:level players @a

# Apply wither to players on any water contact (feet or head)
execute as @a if predicate water_rising:in_contact_with_water run effect give @s wither 1 1 true
# Clear wither immediately once out of water
execute as @a unless predicate water_rising:in_contact_with_water run effect clear @s wither

# If in grace (state 1), countdown
execute if score $state wr_state matches 1 run function water_rising:grace_tick

# Rising handled by scheduled loop once active
