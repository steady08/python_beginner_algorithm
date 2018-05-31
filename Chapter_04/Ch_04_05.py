import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def carpet1(x, y, r):
    if r > 1:
        carpet1(x - 2 * r, y + 2 * r, r / 3)
        carpet1(x - 2 * r, y, r / 3)
        carpet1(x - 2 * r, y - 2 * r, r / 3)
        carpet1(x, y + 2 * r, r / 3)
        carpet1(x, y - 2 * r, r / 3)
        carpet1(x + 2 * r, y + 2 * r, r / 3)
        carpet1(x + 2 * r, y, r / 3)
        carpet1(x + 2 * r, y - 2 * r, r / 3)

        rect = Rectangle((x-r/6, y-r/6), r/3, r/3, color='blue')
        ax.add_patch(rect)


def carpet2(x, y, r):
    if r > 1:
        carpet2(x - 2 * r, y + 2 * r, r / 2)
        carpet2(x - 2 * r, y, r / 2)
        carpet2(x - 2 * r, y - 2 * r, r / 2)
        carpet2(x, y + 2 * r, r / 2)
        carpet2(x, y - 2 * r, r / 2)
        carpet2(x + 2 * r, y + 2 * r, r / 2)
        carpet2(x + 2 * r, y, r / 2)
        carpet2(x + 2 * r, y - 2 * r, r / 2)

        rect = Rectangle((x - r / 6, y - r / 6), r / 3, r / 3, color='blue')
        ax.add_patch(rect)


def carpet3(x, y, r):
    if r > 1:
        carpet3(x - r, y + r, r / 2)
        carpet3(x + r, y + r, r / 2)
        carpet3(x - r, y - r, r / 2)
        carpet3(x + r, y - r, r / 2)

        rect = Rectangle((x - r / 6, y - r / 6), r / 3, r / 3, color='blue')
        ax.add_patch(rect)


if __name__ == '__main__':
    fig, ax = plt.subplots(1, 1)
    carpet1(0, 0, 60)
#    carpet2(0, 0, 50)
#    carpet3(0, 0, 100)
    ax.autoscale_view()
    plt.show()
