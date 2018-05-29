import matplotlib.pyplot as plt

pixel_step = 0.5


def recursive_line(x1, y1, x2, y2):
    if -pixel_step <= x1-x2 <= pixel_step and -pixel_step <= y1-y2 <= pixel_step:
        pass
    else:
        plt.plot([(x1+x2)/2], [(y1+y2)/2], 'bo')
        recursive_line(x1, y1, (x1+x2)/2, (y1+y2)/2)
        recursive_line(x2, y2, (x1+x2)/2, (y1+y2)/2)


if __name__== '__main__':
    recursive_line (10, 10, 600, 350)
    plt.show()
