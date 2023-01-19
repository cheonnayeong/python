marks = [90,25,67,45,80]
number = 0

for mark in marks:
    number += 1

    if mark >= 60:
        print(f"{number}학생은 {mark}점으로 합격힙니다")
        print("{}학생은 {}점으로 합격입니다.".format(number, mark))

    else:
        print("{number}학생은 {mark}점으로 불합격입니다")