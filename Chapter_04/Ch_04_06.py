import math
import random
import matplotlib.pyplot as plt


def fixed_tree(x1, y1, angle, depth, order):
    if order > 0:
        x2 = x1 + (math.cos(math.radians(angle)) * depth)
        y2 = y1 + (math.sin(math.radians(angle)) * depth)
        plt.plot([x1, x2], [y1, y2], 'b.-')
        fixed_tree(x2, y2, angle - 30, depth * 0.8, order - 1)
        fixed_tree(x2, y2, angle + 30, depth * 0.8, order - 1)


def random_tree(x1, y1, angle, depth, order):
    if order > 0:
        x2 = x1 + (math.cos(math.radians(angle)) * depth)
        y2 = y1 + (math.sin(math.radians(angle)) * depth)
        plt.plot([x1, x2], [y1, y2], 'b.-')

        right_angle = random.randint(0, 40)
        left_angle = random.randint(0, 40)
        depth_scale = random.uniform(0.7, 0.9)

        random_tree(x2, y2, angle - right_angle, depth * depth_scale, order - 1)
        random_tree(x2, y2, angle + left_angle, depth * depth_scale, order - 1)


if __name__ == '__main__':
    order = 10
    fixed_tree(100, 100, 90, 70, order)
#   random_tree(100, 100, 90, 70, order)
    plt.show()
