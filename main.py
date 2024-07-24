#GPA管理システム


GPA = {}
while True:
    print("1. 成績入力 2. 成績一覧")
    option = int(input("貴方の入力："))

    if option == 1:
        sub, gpa = input().split(",")
        gpa = int(gpa)
        if sub not in GPA:
            GPA[sub] = [gpa]
        else:
            GPA[sub].append(gpa)

    else:
        print("ーーーーーーーーーーーーーーーーーーー")
        for i in GPA:
            print(i, ":", sum(GPA[i])/len(GPA[i]))
        print("ーーーーーーーーーーーーーーーーーーー")
