password = 'a123456'
x = 3
while x <= 3 and x >= 1:
	pwd = input('請輸入密碼: ')
	if pwd == 'a123456':
		print('登入成功')
		break
	else:
		x = x-1
		print('密碼錯誤! 還有', x, '次機會')
		if x == 0:
			print('此帳號已鎖定')
			break
