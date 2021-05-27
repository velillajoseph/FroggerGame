import random, time


def create_row(l:int):
	res = []
	for i in range(l):
		if random.randint(0,2) == 1:
			res.append('===')
		else:
			res.append('   ')
	return res

def move(matr:list):
	for i in range(len(matr)):
		if (i+2) % 2 == 0:
			matr[i] = matr[i][1:] + matr[i][:1]
		else:
			matr[i] = matr[i][-1:] + matr[i][:len(matr)-1]
	return matr

def print_fild(pg, pl,x, y):
	print('---'*10)
	tmp = pg[:]
	tmp.append(pl)
	for i in range(len(tmp)):
		for j in range(len(tmp[i])):
			if i == y and j == x:
				print(' @ ', end='')
			else:
				print(tmp[i][j],end='')
		print('\n')

def collision(pl,x,y):
	if y >= len(pl):
		return False
	if pl[y][x] == '===':
		return True
	return False

def main():
	score = 0
	size = 10
	playground = [create_row(size) for i in range(size)]
	player = ['   ' for i in range(size)]
	x = 5
	instruction = 'w-up, s-down, a-left, d-right, e-end game'
	y = size 
	print(instruction)
	while True:
		print_fild(playground, player, x, y)
		comm = input()
		if comm.lower() == 'e':
			break
		elif comm.lower() == 'w':
			if y > 0:
				y -= 1
		elif comm.lower() == 's':
			if y < size:
				y +=1
		elif comm.lower() == 'd':
			if x < size-1:
				x += 1
		elif comm.lower() == 'a':
			if x > 0:
				x -= 1
		if y == 0:
			score += 10
			x = 5
			y = size
		if collision(playground, x, y):
			print('game ower')
			print('your score is {}'.format(score))
			break
		playground = move(playground[:])


while True:
	comm = input('want to start a new game? y/n ')
	if comm.lower() == 'n':
		break
	elif comm.lower() == 'y':
		main()
	else:
		print('invalid input')
		continue
