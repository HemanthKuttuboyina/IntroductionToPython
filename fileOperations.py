items = ["milk","eggs","bread"]
with open("shopping.txt","w",encoding="utf-8") as f:
    id = 1
    for item in items:
        f.write(str(id)+". "+item +"\n")
        id+=1
with open("shopping.txt",encoding="utf-8") as f:
    # line =
    # for l in line:
    #     print(line)
    print(f.read())