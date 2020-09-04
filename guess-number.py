import random
start = input('請決定隨機數字範圍開始值: ')
end  = input('請決定隨機數字範圍結束值: ')
start = int(start) #字串轉數字
end = int(end) #字串轉數字
r = random.randint(start,end) #randint只能用數字，而且前者一定要比後者大
count = 0
while True:
	count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r :
		print('恭喜答對')
		print('這是你猜的第', count, '次')
		break
	elif num < r:
		print('比答案小')
	elif num > r:
		print('比答案大')
	print('這是你猜的第', count, '次')
