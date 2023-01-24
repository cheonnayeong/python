# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

marks = [90, 25, 67,  45, 80]
name = ['강민석', '김강민','김병찬', '김영준', ' 노가현', '박수빈', '박정빈', '배유정', '유성욱','윤동현','이근호','잉채우','천나영','하현재','한지수']
number = 0


for mark in marks:
	number = number +1
	if mark < 60: continue
	print(f"%d번 학생 축하합니다. 합격입니다")
		
for name in name:
	print(name, end=". ")
