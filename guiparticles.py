import sys
sys.path.append("/Users/brentwestbrook/PyModules")
from graphics import *
import random

class Random_box:
	
	def __init__(self, num_particles = 100):
		self.particles = num_particles
		self.left_particles = num_particles
		self.particle_list = [0 for i in range(self.particles)]
		self.left_circ_list = []
		self.right_circ_list = []
		self.win = GraphWin("Simulation Box", 500, 250)

	def make_graphics(self):
		for i in range(self.left_particles):
			circ = Circle(Point(random.randint(10,240), random.randint(10,240)), 10)
			circ.draw(self.win)
			self.left_circ_list.append(circ)
		for i in range(self.particles - self.left_particles):
			circ = Circle(Point(random.randint(260,490), random.randint(10,240)), 10)
			circ.draw(self.win)
			self.right_circ_list.append(circ)
		left_rect = Rectangle(Point(0,0), Point(250, 250))
		right_rect = Rectangle(Point(250,0), Point(500, 250))
		left_rect.draw(self.win)
		right_rect.draw(self.win)

	def run_simulation2(self, sim_time = 1000):
		self.make_graphics()
		for i in range(sim_time):
			time.sleep(1)
			rand = int(random.random() * self.particles)
			if self.particle_list[rand] == 1:
				self.particle_list[rand] = 0
				if len(self.right_circ_list) > 0:
					right_part = random.randint(0,len(self.right_circ_list)-1)
					self.right_circ_list[right_part].move(-240, 0)
					self.left_circ_list.append(self.right_circ_list[right_part])
					del self.right_circ_list[right_part]
			else:
				left_part = random.randint(0, len(self.left_circ_list)-1)
				self.left_circ_list[left_part].move(240, 0)
				self.right_circ_list.append(self.left_circ_list[left_part])
				del self.left_circ_list[left_part]
				self.particle_list[rand] = 1
		self.win.getMouse()

sim1 = Random_box(5)
sim1.run_simulation2(20)
