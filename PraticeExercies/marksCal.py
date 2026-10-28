studentAnswers = ["a","b","a","c","b","b"]
actualAnswers = ["b","a","a","c","b","c"]
score = 0
for st,act in zip(studentAnswers,actualAnswers):
    if st == act:
        score += 1
print(f"Total Score : {score}/{len(actualAnswers)}")