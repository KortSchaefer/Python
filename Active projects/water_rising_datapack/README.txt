Water Rising Datapack (Java 1.20+)
=================================

Installation
------------
1) Copy the `water_rising_datapack` folder into your world's `datapacks/` directory.
2) Start the world (or run /reload).
3) You should see a load message in chat.

What it does
------------
- Defines a 3×3 chunk flood area centered at (0,0) (X:-16..31, Z:-16..31).
- Places a horizontal water layer at the current flood Y level across that area at a configurable interval.
- Uses an invisible armor stand marker at (0,Y,0) to track the water level.
- Grace period: 5 minutes (6000 ticks) before water starts rising; shows a bossbar countdown.
- Players standing in water receive Wither II while in water.
- Forceloads the 3×3 chunk area.

Commands
--------
Player trigger:
- /trigger wr_start set 1  → Start the 5-minute grace period.

Operator functions:
- /function water_rising:start           → Start grace manually.
- /function water_rising:stop            → Stop the flood and hide bossbars.
- /function water_rising:set_start_here  → Move the water marker to your current Y at (0,0).
- /function water_rising:help            → Show this help prompt.

Scoreboards (config)
--------------------
- wr_state:   0=idle, 1=grace, 2=active
- wr_timer:   internal timer for grace and rise interval
- wr_interval: interval in ticks between rises (default 200 = 10s)
  To change interval: `/scoreboard players set $interval wr_interval <ticks>`

Bossbars
--------
- water_rising:grace – shows remaining grace ticks (max 6000)
- water_rising:level – shows current marker Y (value is Y)

Notes
-----
- By default, water fill replaces only air. You can adjust the fill to replace other blocks in `raise_water.mcfunction`.
- The area is forceloaded via `forceload add -1 -1 1 1` which covers the 3×3 chunks.
