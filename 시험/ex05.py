#인생 시계
#인생을 하루로 보았을때 나의 사간은?

age = int(input("당신의 나이는? :"))

hour = (age * 18) // 60
min = (age * 18) % 60

print("당신의 시간은", hour, "시", min, "분 입니다.")
print(f"당신의 시간은 {hour}시 {min}분 입니다")