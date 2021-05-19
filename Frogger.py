
from graphics import *

frogger=GraphWin('Frogger', 700,500)
square=Rectangle(Point(0,0),Point(700,500))
square.setOutline("black")
square.setFill('black')
square.draw(frogger)

road1=Line(Point(350,500),Point(350,0))
road1.setOutline('white')
road1.setWidth(2)
road1.draw(frogger)


road2=Line(Point(400,500),Point(400,0))
road2.setOutline('white')
road2.setWidth(2)
road2.draw(frogger)


road3=Line(Point(450,500),Point(450,0))
road3.setOutline('white')
road3.setWidth(2)
road3.draw(frogger)


road4=Line(Point(500,500),Point(500,0))
road4.setOutline('white')
road4.setWidth(2)
road4.draw(frogger)


road5=Line(Point(550,500),Point(550,0))
road5.setOutline('white')
road5.setWidth(2)
road5.draw(frogger)

road6=Line(Point(600,500),Point(600,0))
road6.setOutline('white')
road6.setWidth(2)
road6.draw(frogger)

road7=Line(Point(650,500),Point(650,0))
road7.setOutline('green')
road7.setWidth(2)
road7.draw(frogger)

car1=Circle(Point(375,250),15)
car1.setFill('white')
car1.draw(frogger)

car2=Circle(Point(425,250),15)
car2.setFill('white')
car2.draw(frogger)

car2=Circle(Point(475,250),15)
car2.setFill('white')
car2.draw(frogger)

car3=Circle(Point(525,250),15)
car3.setFill('white')
car3.draw(frogger)

car4=Circle(Point(575,250),15)
car4.setFill('white')
car4.draw(frogger)

car5=Circle(Point(625,250),15)
car5.setFill('white')
car5.draw(frogger)

Frog=Rectangle(Point(310,230),Point(340,275))
Frog.setFill('green')
Frog.setOutline('Red')
Frog.draw(frogger)




def main():


    input("press enter to quit: ")
main() 