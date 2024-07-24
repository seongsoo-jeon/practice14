#GPA管理システム


GPA = {}
while True:

    sub, gpa = input().split(",")
    gpa = int(gpa)
    if sub not in GPA:
        GPA[sub] = [gpa]
    else:
        GPA[sub].append(gpa)

    print(GPA)

