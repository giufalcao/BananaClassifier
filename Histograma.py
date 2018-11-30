import cv2 as cv
from matplotlib import pyplot as plt


def plot_histogram(imagem):
    color = ('r', 'g', 'b')
    for i, col in enumerate(color):
        histr = cv.calcHist([imagem], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()