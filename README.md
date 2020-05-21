# BaalKiller
Tiny bot for Idling to rule the gods

Disclaimer: This whole thing is a giant mess as I'm learning how to structure code properly and learn new methods as I go a long.
Can lack severe optimization.

This is a bot I'm working on for a idle game called Idling to Rule the Gods.
It's used as a learning excercise on how to automate some complex processes.
I'm using basic image recognition to find points of interest, timer system to keep track of next actions
and straight up brute forced coordinates

Working module:
Dungeon and Campaign module is good and stable. Can track active dungeons and campaigns, collect their rewards and start new ones.
Lacking easy way to config dungeon teams / no config file. Only a default creation method

Divinity module is somewhat working, it's got the basics down. 
It can check if it's created, if not, create itself and then check how many clones we have available 
and then put them all on "gain" and "conversion" upgrades (half on each) and 1/20th on "capacity" upgrade

There's currently only a nrdc_loop available for easy access with predefined dungeons running 
(volcano, team_1, depth_2, 16 rooms, difficulty 5)
(water, team_2, depth_2, 18(+2 for libraries) rooms, difficulty 3)
(forest, team_3, depth_1, 6 rooms, difficulty 8)
