f = open("input1.txt", "r")
nums = list()
con = 0
freq = list()
for line in f:
    nums.append(int(line.replace("\n", "").replace("+", "")))
for num in nums:
    con += num
con = 0
freq = {con}
flag = True
while flag:
    for line in nums:
        con += line
        if con in freq:
            print(con)
            flag = False
            break
        freq.add(con)
