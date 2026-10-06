##a = 9
##b = 2

##print("a =", a)
##print("b =", b)

##print("a // b=", a // b)
##print("a % b =", a % b)
##print("a ** b =", a ** b)

##a = 9
##a += 3
##print("a += 3 :", a)

##a = 9
##a -= 3
##print("a -= 3 :", a)

##a= 9
##a *= 3
##print("a *= 3 :", a)

##a = 9
##a /= 3
##print("a /= 3 :", a)

##a = 9
##a //= 3
##print("a //= 3 :", a)

##a = 9
##a %= 3
##print("a %= 3 :", a)

##a = 9
##a **= 3
##print("a **= 3 :", a)

##a = 9
##a = 2

##print(a == b)
##print(a != b)
##print(a > b)
##print(a >= b)
##print(a < b)
##print(a <= b)

##a = 9
##b = 2

##print((a > 100) and (b > 10))
##print((a>100) or (b > 10))
##print(not(a > 100))

##S1, S2, S3 = "100", "100.123", "999999999999999999999999"
##print(int(S1) + 1, float(S2) + 1, int(S3) + 1)

##money, c500, c100, c50, c10 = 0, 0, 0, 0, 0
##money = int(input("교환할 돈은 얼마?"))

##c500 = money //500
##money = money % 500

##c100 = money // 100
##money = money % 100

##c50 = money // 50
##money = money % 50

##c10 = money // 10
##money = money % 10

##print("500원짜리 : ", c500, "개")
##print("100원짜리 : ", c100, "개")
##print("50원짜리 : ", c50, "개")
##print("10원짜리 : ", c10, "개")
##print("바꾸지 못한 잔돈 ==> ", money, "원")

##money = int(input("교환할 돈은 얼마?"))

##m10000 = money // 10000
##money = money % 10000

##m5000 = money // 5000
##money = money % 5000

##m1000 = money // 1000
##money = money % 1000

##print("10000원짜리 : ", m10000, "장")
##print("5000원짜리 : ", m5000, "장")
##print("1000원짜리 : ", m1000, "장")
##print("남은 돈 : ", money, "원")

##a = 200
##if a < 100:
##    print("100보다 작군요.")
##    print("거짓이므로 이 문장은 안 보이겠죠?")

##print("프로그램 끝")

##a = int(input("정수를 입력하세요 :"))
##if a % 2 == 0:
##    print("짝수를 입력했군요.")
##else:
##    print("홀수를 입력했군요.")


##a = 75

##if a > 50:
##    if a < 100:
##        print("50보다 크고 100보다 작군요.")
##    else:
##        print("와~~ 100보다 크군요")
##else:
##    print("에고~ 50보다 작군요.")

##score = int(input("점수를 입력하세요 :"))

##if score >= 90:
##    print("A")
##else:
##    if score >= 80:
##        print("B")
##    else:
##        if score >= 70:
##            print("C")
##        else:
##            if score >= 60:
##                print("D")
##            else:
##                print("F")
##print("학점입니다. ^^")

score = int(input("점수를 입력하세요 :"))
if score >= 95:
    print("A+")
elif score >= 90:
    print("A0")
elif score >= 85:
    print("B+")
elif score >= 80:
    print("B0")
elif score >= 75:
    print("C+")
elif score >= 70:
    print("C0")
elif score >= 65:
    print("D+")
elif score >= 60:
    print("D0")
else:
    print("F")

print("학점입니다. ^^")



    