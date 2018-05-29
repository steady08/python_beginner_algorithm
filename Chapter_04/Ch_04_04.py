import matplotlib.pyplot as plt
import math


radius = 5
step = 0.4


def create_circle():
    circle = plt.Circle((0,0), radius= radius, fill=False)
    return circle


def show_shape(patch):
    ax = plt.gca()
    ax.add_patch(patch)
    plt.axis('scaled')


def recur_fill(x, y, pixel_list):
    if x > radius or x < -radius:
        return
    else:
        y_ref = math.sqrt(radius*radius - x*x)

    if y < -y_ref or y > y_ref:
        return
    else:
        plt.plot([x], [y], 'bo')
        pixel_list.append([x, y])

        if not [x-step, y] in pixel_list:
            recur_fill(x-step, y, pixel_list)

        if not [x+step, y] in pixel_list:
            recur_fill(x+step, y, pixel_list)

        if not [x, y-step] in pixel_list:
            recur_fill(x, y-step, pixel_list)

        if not [x, y+step] in pixel_list:
            recur_fill(x, y+step, pixel_list)


if __name__ == '__main__':
    c = create_circle()
    show_shape(c)
    pixel_list = []
    recur_fill(0, 0, pixel_list)
    plt.show()
