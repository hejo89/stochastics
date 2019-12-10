""" depicts grid with uniformly distributed points, which makes the number of points per square 
approximately poisson distributed. Pressing h shows histogramm for number of points per square."""

#!/usr/bin/python3
from collections import defaultdict
import random
from math import sqrt
import arcade
import matplotlib.pyplot as plt

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000
COLOR_LINE = (255, 255, 255)
BALL_RADIUS = 4
COLOR_BALL = (255, 100, 255)
class Poisson_points(arcade.Window):
    def __init__(self, nr_of_bombs, grid_size, depiction):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.d = defaultdict(int)
        self.depiction = depiction
        self.grid_size = grid_size
        self.points = []
        self.nr_of_bombs = nr_of_bombs
        self.count = 0

    def update(self, dt):
        if self.depiction == "all bombs":
            while self.count <= self.nr_of_bombs:
                self.new_bomb = [random.choice(range(SCREEN_HEIGHT)), random.choice(range(SCREEN_WIDTH))]
                self.points.append(self.new_bomb)
                self.count += 1
                self.d[(self.new_bomb[0] // (SCREEN_HEIGHT / self.grid_size), self.new_bomb[1] // (SCREEN_WIDTH / self.grid_size))] += 1

        if self.depiction == "current bomb":
            self.points = [random.choice(range(SCREEN_HEIGHT)), random.choice(range(SCREEN_WIDTH))]

    def on_draw(self):
        self.color_ball = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        arcade.start_render()

        if self.depiction == "all bombs":
            for _ in self.points:
                arcade.draw_circle_filled(_[0], _[1], BALL_RADIUS, self.color_ball)

        if self.depiction == "current bomb":
            arcade.draw_circle_filled(self.points[0], self.points[1], BALL_RADIUS, self.color_ball)
        if self.grid_size <= 100:
            for _ in range(self.grid_size + 1):
                arcade.draw_line(0, SCREEN_HEIGHT * _ / self.grid_size, SCREEN_WIDTH ,SCREEN_HEIGHT * _ / self.grid_size, COLOR_LINE)
                arcade.draw_line(_ / self.grid_size * SCREEN_WIDTH, 0, _ / self.grid_size * SCREEN_WIDTH ,SCREEN_HEIGHT, COLOR_LINE)


    def on_key_press(self, key, modifiers):
        if self.depiction == "all bombs" and key == arcade.key.H:
            bar_width = max(1, int(sqrt(sqrt(self.nr_of_bombs / self.grid_size**2))))
            tmp = list(self.d.values()) + [0] * (self.grid_size**2 - len(self.d))
            print(tmp)
#            plt.hist(tmp, density = True, bins=range(int(min(tmp)), int(max(tmp)) + 1, 1), align = "left", rwidth = 0.5)
#            plt.hist(tmp, rwidth = 1)
#            plt.show()
            plt.hist(tmp, bins=range(int(min(tmp)), int(max(tmp)) + 1, 1), align = "left", rwidth = 0.5, density = True)
            # plt.hist(tmp, density = True, rwidth = 1)
            plt.show()
        if key == arcade.key.P:
            print(len(self.d))
        if key == arcade.key.F:
            self.set_fullscreen(not self.fullscreen)
            self.set_viewport(0, SCREEN_WIDTH, 0, SCREEN_HEIGHT)

        if key == arcade.key.ESCAPE:
            arcade.close_window()

if __name__ == "__main__":
    # Poisson_points(1000000, 1000, "all bombs")
    # Poisson_points(22500, 150, "all bombs")
#    Poisson_points(535, 24, "current bomb")  
    Poisson_points(10**3, 24, "all bombs")  
#    Poisson_points(50035, 24, "all bombs")  

    arcade.run()
