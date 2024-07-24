# GPA管理システム

GPA = {}

def select_option():
    print("1. 成績入力 2. 成績一覧 3.終了")
    opt = int(input("貴方の入力："))
    return opt

def opt_1st(GPA):
    sub, gpa = input().split(",")
    gpa = int(gpa)
    if sub not in GPA:
        GPA[sub] = [gpa]
    else:
        GPA[sub].append(gpa)

def opt_2nd(GPA):
    print("ーーーーーーーーーーーーーーーーーーー")
    for i in GPA:
        print(i, ":", sum(GPA[i]) / len(GPA[i]))
    print("ーーーーーーーーーーーーーーーーーーー")

while True:

    option = select_option()

    if option == 1:
        opt_1st(GPA)

    elif option == 2:
        opt_2nd(GPA)

    else:
        break
