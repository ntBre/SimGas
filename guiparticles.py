import sys
sys.path.append("/Users/brentwestbrook/PyModules")
from graphics import *
import random

class Random_box:
	
	def __init__(self, num_particles = 100):
		self.particles = num_particles
		self.left_particles = num_particles
		self.win = GraphWin("Simulation Box", 500, 250)

	def make_graphics(self):
		for i in range(self.left_particles):
			circ = Circle(Point(random.randint(10,240), random.randint(10,240)), 10)
			circ.draw(self.win)
		for i in range(self.particles - self.left_particles):
			circ = Circle(Point(random.randint(260,490), random.randint(10,240)), 10)
			circ.draw(self.win)
		left_rect = Rectangle(Point(0,0), Point(250, 250))
		right_rect = Rectangle(Point(250,0), Point(500, 250))
		left_rect.draw(self.win)
		right_rect.draw(self.win)

	def increment_time(self):
		r = random.random()
		if r <= self.left_particles/self.particles:
		    self.left_particles = self.left_particles - 1
		else:
		    self.left_particles = self.left_particles + 1
        
	def run_simulation(self, sim_time = 1000):
		i = 0
		while i < sim_time - 1:
			self.make_graphics()	
			time.sleep(2)
			self.increment_time()
			i = i + 1
		self.win.getMouse()

sim1 = Random_box(5)
sim1.run_simulation(5)
