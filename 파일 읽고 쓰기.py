f = open("새파일2.txt", 'r', encoding="UTF-8")
line = f.readline() #한줄씩 읽어오늘 함수
print(line)
f.close()