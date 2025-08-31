# Set starting flood height to executor's Y (clamped) and center remains 8,8
execute store result score $y wr_y run data get entity @s Pos[1] 1
# Clamp to supported range 62..309
execute if score $y wr_y matches ..61 run scoreboard players set $y wr_y 62
execute if score $y wr_y matches 310.. run scoreboard players set $y wr_y 309

# Update bossbar
execute store result bossbar water_rising:level value run scoreboard players get $y wr_y
tellraw @s [{"text":"[Water Rising] ","color":"aqua"},{"text":"Start height set.","color":"white"}]
