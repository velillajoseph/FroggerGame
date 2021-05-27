from graphics import *
import random, sys

class Enemy(Image):

	def run(self, dx):
		self.move(dx, 0)
		self.respawn()

	def respawn(self):
		x = self.getAnchor().getX()
		if x < -100:
			self.move(936,0)
		elif x > 836:
			self.move(-936,0)

class Friend(Image):

	def respawn(self):
		x = self.getAnchor().getX()
		y = self.getAnchor().getY()
		dx = x - 46*(random.randint(2,15))+23
		dy = y - 46*(random.randint(7,8))+23
		self.move(-dx, -dy)

	def colision(self, other):
		xs = self.getAnchor().getX()
		ys = self.getAnchor().getY()
		xo = other.getAnchor().getX()
		yo = other.getAnchor().getY()
		ws = self.getWidth()
		hs = self.getHeight()
		wo = other.getWidth()
		ho = other.getHeight()
		if (abs(xs - xo) < (ws + wo)/2) and (abs(ys - yo) < (hs + ho)/2):
			return True

class Frog(Image):

	def up(self, d):
		y = self.getAnchor().getY()
		if y - d < 69:
			return
		self.move(0, -d)
	def down(self, d):
		y = self.getAnchor().getY()
		if y + d > 575:
			return
		self.move(0, d)
	def right(self, d):
		x = self.getAnchor().getX()
		if x + d > 713:
			return
		self.move(d, 0)
	def left(self, d):
		x = self.getAnchor().getX()
		if x - d < 23:
			return
		self.move(-d, 0)
	def respawn(self):
		x = self.getAnchor().getX()
		y = self.getAnchor().getY()
		dx = x - 46*(random.randint(2,15))+23
		dy = y - 575
		self.move(-dx, -dy)
	def colision(self, other):
		xs = self.getAnchor().getX()
		ys = self.getAnchor().getY()
		xo = other.getAnchor().getX()
		yo = other.getAnchor().getY()
		ws = self.getWidth()
		hs = self.getHeight()
		wo = other.getWidth()
		ho = other.getHeight()
		if (abs(xs - xo) < (ws + wo)/2) and (abs(ys - yo) < (hs + ho)/2):
			return True

def game_over(win):
	txt = Text(Point(736/2, 598/2),'GAME OWER\n Play again?\nY / N')
	txt.setTextColor(color_rgb(200, 25, 25))
	txt.setSize(30)
	txt.setFace('helvetica')
	txt.draw(win)
	while True:
		key = win.checkKey()
		if key == 'y':
			txt.undraw()
			return
		if key == 'n':
			sys.exit()
		update(30)

def main():

	#variable declaration
	step = 46
	speed = 0.7
	lives = 3
	score = 0
	per_lives = 0
	max_score = 0
	cars_left = ('sprites/car_1_l.png', 'sprites/car_2_l.png', 'sprites/car_3_l.png')
	cars_right = ('sprites/car_1_r.png', 'sprites/car_2_r.png', 'sprites/car_3_r.png')
	water_left = ('sprites/long_tree.png', 'sprites/midl_tree.png',
					'sprites/short_tree.png', 'sprites/tortl_l.png')
	water_right = ('sprites/long_tree_r.png', 'sprites/midl_tree_r.png',
					'sprites/short_tree_r.png', 'sprites/tortl_r.png')
	frogs_r = 'sprites/frog_r.png'
	frogs_l = 'sprites/frog_l.png'
	winner_x_y = []
	finish = []
	homes = []
	cars = []
	waters = []
	frogs = []
	#creating window
	win = GraphWin('Frogger', 736, 598)
	win.setBackground(color_rgb(173, 216, 230))
	#start screen
	logo = Image(Point(736/2, 200), 'logo.png')
	logo.draw(win)
	start_btn = Image(Point(736/2, 500), 'play-button.png')
	start_btn.draw(win)
	win.getMouse()
	#creating text fields for:
	#pause text
	pause = Text(Point(736/2, 598/2),'PAUSE')
	pause.setTextColor(color_rgb(200, 25, 25))
	pause.setSize(30)
	pause.setFace('helvetica')
	#lives text
	txt_l = Text(Point(50, 23),'L {}'.format(lives))
	txt_l.setTextColor(color_rgb(120, 100, 0))
	txt_l.setSize(20)
	txt_l.setFace('helvetica')
	txt_l.draw(win)
	#score text
	txt_s = Text(Point(736/2-100, 23),'SCORE {}'.format(score))
	txt_s.setTextColor(color_rgb(120, 100, 0))
	txt_s.setSize(20)
	txt_s.setFace('helvetica')
	txt_s.draw(win)
	#max score
	txt_m = Text(Point(736-200, 23),'HI SCORE {}'.format(max_score))
	txt_m.setTextColor(color_rgb(120, 100, 0))
	txt_m.setSize(20)
	txt_m.setFace('helvetica')
	txt_m.draw(win)
	#location rendering
	for i in range(16):
		if (i+3) % 3 == 0:
			winner_x_y.append((46*i+23,46*1+23))
			finish.append(Image(Point(*winner_x_y[-1]), 'sprites/yard_f.png'))
			finish[-1].draw(win)
		else:
			Image(Point(46*i+23,46*1+23), 'sprites/yard_d.png').draw(win)
		Image(Point(46*i+23,46*2+23), 'sprites/water.png').draw(win)
		Image(Point(46*i+23,46*3+23), 'sprites/water.png').draw(win)
		Image(Point(46*i+23,46*4+23), 'sprites/water.png').draw(win)
		Image(Point(46*i+23,46*5+23), 'sprites/water.png').draw(win)
		Image(Point(46*i+23,46*6+23), 'sprites/yard_u.png').draw(win)
		Image(Point(46*i+23,46*7+23), 'sprites/yard_d.png').draw(win)
		Image(Point(46*i+23,46*8+23), 'sprites/road.png').draw(win)
		Image(Point(46*i+23,46*9+23), 'sprites/road.png').draw(win)
		Image(Point(46*i+23,46*10+23), 'sprites/road.png').draw(win)
		Image(Point(46*i+23,46*11+23), 'sprites/road.png').draw(win)
		Image(Point(46*i+23,46*12+23), 'sprites/yard_u.png').draw(win)

	#creation and rendering of game objects
	#player objekt
	player = Frog(Point(46*(random.randint(2,15))+23, 575), 'sprites/frog.png')
	#fly object
	bee = Friend(Point(46*(random.randint(2,15))+23, 46*(random.randint(6,7))+23), 'sprites/bee.png')
	bee.draw(win)
	#objects of cars, turtles and trees
	for i in range(4):
		if (i+1) % 2 == 0:
			cars.append(Enemy(Point(-100, 46*(11-i)+23), random.choice(cars_right)))
			waters.append(Enemy(Point(-100, 46*(5-i)+23), random.choice(water_right)))
		else:
			cars.append(Enemy(Point(836, 46*(11-i)+23), random.choice(cars_left)))
			waters.append(Enemy(Point(836, 46*(5-i)+23), random.choice(water_left)))
		cars[i].draw(win)
		waters[i].draw(win)
	for i in range(2):
		if (i+1) % 2 == 0:
			frogs.append(Enemy(Point(-100, 46*6+23), frogs_r))
		else:
			frogs.append(Enemy(Point(836, 46*7+23), frogs_l))
		frogs[i].draw(win)
	player.draw(win)
	#event loop
	while True:
		key = win.checkKey()
		#check if the pause or exit key is pressed
		if key == 'space':
			pause.draw(win)
			while win.checkKey() != 'space':
				update(10)
				pass
			pause.undraw()
		if key == 'Escape':
			sys.exit()
		#frames per second
		update(30)
		#loops of movement of enemy objects
		for i in range(4):
			if (i+1) % 2 == 0:
				cars[i].run(speed*(i+1))
				waters[i].run(speed*(i+1))
				if player.colision(waters[i]):
					player.right(speed*(i+1))
			else:
				cars[i].run(-speed*(i+1))
				waters[i].run(-speed*(i+1))
				if player.colision(waters[i]):
					player.left(speed*(i+1))

		for i in range(2):
			if (i+1) % 2 == 0:
				frogs[i].run(speed*(i+1))
			else:
				frogs[i].run(-speed*(i+2))
		#checking the keystrokes to control the hero
		if key == 'Up':
			player.up(step)
		elif key == 'Down':
			player.down(step)			
		elif key == 'Right':
			player.right(step)
		elif key == 'Left':
			player.left(step)
		#checking collisions of the main character with other objects
		for el in cars + frogs:
			if player.colision(el):
				lives -= 1
				if lives < 0:
					lives = 3
					score = 0
					game_over(win)
					for home in homes:
						home.undraw()
					homes = []
				player.respawn()
		y = player.getAnchor().getY()
		if y > 100 and y < 299:
			died = True
			for el in waters:
				if player.colision(el):
					died = False
			if died:
				lives -= 1
				if lives < 0:
					lives = 3
					score = 0
					for home in homes:
						home.undraw()
					homes = []
					game_over(win)
				player.respawn()

		for i in range(len(finish)):
			if player.colision(finish[i]):
				empty = True
				for hom in homes:
					if player.colision(hom):
						empty = False
				if empty:
					score += 100
					homes.append(Image(Point(*winner_x_y[i]), 'sprites/frog_f.png'))
					homes[-1].draw(win)
					if max_score < score:
						max_score = score
					speed += 0.5
				else:
					lives -= 1

					if lives < 0:
						lives = 3
						score = 0
						for home in homes:
							home.undraw()
						homes = []
						game_over(win)
				player.respawn()
		for el in frogs:
			if bee.colision(el):
				bee.respawn()
		if player.colision(bee):
			per_lives += 1
			if per_lives >= 10:
				lives += 1
				per_lives = 0
			score += 10
			if max_score < score:
				max_score = score
			bee.respawn()
		if len(homes) >= 6:
			lives += 1
			for home in homes:
				home.undraw()
			homes = []
			score += 500
			if max_score < score:
				max_score = score
		#updating text fields
		txt_l.setText('L {}'.format(lives))
		txt_s.setText('SCORE {}'.format(score))
		txt_m.setText('HI SCORE {}'.format(max_score))		
	
	win.close()

main()
