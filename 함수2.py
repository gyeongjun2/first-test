print("life","is","too","short")

for i in range(10):
    print(i, end=' ') #end=' ' : 간격을 안바꾸고 띄어쓰기로 쓰는것

# 파일 읽고 쓰기 w, r, 
f = open("새파일.txt",'w', encoding="UTF-8")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()

f = open("새파일2.txt", 'r', encoding="UTF-8")
line = f.readline() #한줄씩 읽어오늘 함수
print(line)
f.close()