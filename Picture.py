# -*- coding: utf-8 -*-
import cv2 as cv
import numpy as np
from PIL import Image
from tabulate import tabulate


def get_picture_web():
    key = 0
    banana_cascade = cv.CascadeClassifier('C:/Users/lucas/PycharmProjects/teste/Xml/banana_classifier.xml')
    cap = cv.VideoCapture(0)

    while True:
        _, frame = cap.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        banana = banana_cascade.detectMultiScale(gray, 1.4, 6)
        for (x, y, w, h) in banana:
            cv.rectangle(frame, (x, y), (x + w, y + w), (0, 255, 0), 2)
            roi_color = frame[y:y + h, x:x + w]

        cv.imshow("WebCam Imagem", frame)
        key = cv.waitKey(1)

        if key == 27:
            break

    cap.release()
    cv.destroyAllWindows()
    return roi_color


def get_picture():
    croppedImage = None
    banana_cascade = cv.CascadeClassifier('C:/Users/lucas/PycharmProjects/teste/Xml/banana_classifier.xml')
    img = cv.imread("C:/Users/lucas/PycharmProjects/teste/Imagens/modelo03.jpg")
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    bananas = banana_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in bananas:
        croppedImage = img[y:y + h, x:x + w]
        break

    cv.imshow('img', croppedImage)
    key = cv.waitKey(0)
    cv.destroyAllWindows()
    return croppedImage


def get_other_pixels():
    photo = Image.open('C:/Users/lucas/PycharmProjects/teste/Imagens/img_segmentation.jpg')  # your image
    photo = photo.convert('RGB')
    cont = 0

    width = photo.size[0]  # define W and H
    height = photo.size[1]

    for y in range(0, height):  # each pixel has coordinates
        row = ""
        for x in range(0, width):
            RGB = photo.getpixel((x, y))
            R, G, B = RGB  # now you can use the RGB value
            if R == 0 and G == 0 and B == 0:
                cont = cont + 1
    return cont

def status_banana(picture):
    letra = ''
    total = len(picture) * len((picture[0]))

    # Yellow pixels in image
    pixels_yellow = (total - get_other_pixels())

    # percentage of pixels yellow
    percentYellow = float(pixels_yellow) / total

    if 0.44 <= percentYellow:
        print tabulate([['Banana Madura!'], ['Total of pixels', total*10], ['Total of pixel close to yellow', pixels_yellow*10],
                    ['Percentage of pixels close to yellow', percentYellow]])

    else:
        print tabulate([['Está banana não está madura!'], ['Total of pixels', total * 10],
                        ['Total of pixel close to yellow', pixels_yellow * 10],
                        ['Percentage of pixels close to yellow', percentYellow]])