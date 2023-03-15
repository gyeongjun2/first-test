coffee = 10
money = 300

while money:
    print("커피 나왔습니다.")
    coffee = coffee - 1
    print("남은 커피 수량 %d" %coffee)
    if coffee==0:
        print("커피 매진")
        break
        