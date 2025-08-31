# Give one random reward to each player if active; then reschedule in 60s (1200t)

# Only operate while active (state 2)
execute if score $state wr_state matches 2 as @a run loot give @s loot water_rising:reward
execute if score $state wr_state matches 2 run schedule function water_rising:rewards/start 1200
