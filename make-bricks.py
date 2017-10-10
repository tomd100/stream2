def make_bricks(small, big, goal):
  if goal > (small + (big * 5)):
    return False
    
  if big > 0:
    divVal = int(goal / 5)
    addVal = goal - (5 * divVal)
    if addVal > small:
      return False
    else:
      return True
  
  if goal > small:
    return False
  else:
    return True
  
