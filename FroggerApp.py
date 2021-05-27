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
