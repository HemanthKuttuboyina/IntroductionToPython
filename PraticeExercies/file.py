with open("score.txt", encoding="utf-8") as f:
    data = []

    for i in f:
        # print(i.split(","))
        val = i.strip("\n").split(",")
        # print(val)
        try:
            data.append(int(val[1]))
        except:
            print("None")
print(sum(data)/len(data))