import random


def round_up(grades):
    up_grades = []
    for grade in grades:
        if (grade % 5) > 2:
            up_grades.append((grade//5 + 1)*5)
        else:
            up_grades.append(grade)
    return up_grades


grades = []
for i in range(0,20):
    grades.append(random.randint(0,100))

print(grades)
print(round_up(grades))

