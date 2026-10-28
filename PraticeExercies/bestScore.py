scores = [12,17,9,15,14,20]
bestScore = scores[0]
Position = 1
for pos,score in enumerate(scores,start=1):
    if bestScore < score:
        bestScore = score
        Position = pos
print(f"Best Score:{bestScore} Student #{pos}")
