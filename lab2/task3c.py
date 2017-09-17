startTime = (6*60*60) + (52*60)
traverseTime = (2*((8*60) + 15)) + (3*((7*60) + 12))
reachTime = startTime + traverseTime
reachTimeHours = int(reachTime / 3600)
reachTimeMinutes = int((reachTime % 3600)/60)
reachTimeSeconds = (reachTimeMinutes % 60)


print(reachTimeHours,":", reachTimeMinutes, ":", reachTimeSeconds)
