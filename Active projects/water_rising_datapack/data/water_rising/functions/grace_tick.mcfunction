# Grace countdown
scoreboard players remove $timer wr_timer 1
execute store result bossbar water_rising:grace value run scoreboard players get $timer wr_timer

# When hits 0, start active
execute if score $timer wr_timer matches ..0 run function water_rising:begin_active
