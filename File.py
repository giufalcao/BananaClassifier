# -*- coding: utf-8 -*-
import os
import cv2 as cv
import Picture
import numpy
import xlwt


def save_picture(imagem):
    path = 'C:/Users/lucas/PycharmProjects/teste/Imagens'
    cv.imwrite(os.path.join(path, 'img_segmentation.jpg'), imagem)


def delete_picture():
    if os.path.exists('C:/Users/lucas/PycharmProjects/teste/Imagens/img_segmentation.jpg'):
        os.remove('C:/Users/lucas/PycharmProjects/teste/Imagens/img_segmentation.jpg')


def percent(controle):
    num = controle + 1

    img = cv.imread('C:/Users/lucas/PycharmProjects/teste/Imagens/modelo0' + str(num) + '.jpg')

    will_seg = crop_img(img)
    segment = cv.threshold(will_seg, 155, 255, cv.THRESH_BINARY)

    total = len(segment) * len((segment[0]))

    pixels_yellow = (total - Picture.get_other_pixels())

    percentYellow = float(pixels_yellow) / total
    return percentYellow


def histogram_result():
    more_picture = True
    cont = 1
    cont_model = 0

    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(u'Segmentação')
    worksheet.write(0, 0, u'N de Ordem')
    worksheet.write(0, 1, u'Porcentagem')

    while more_picture:
        worksheet.write(cont, 0, cont)
        worksheet.write(cont, cont, percent(cont_model))
        cont_model = cont_model + 1

        if cont_model == 8:
            more_picture = False
    workbook.save('Amostragem.xls')


def crop_img(img):
    croppedImage = ''
    banana_cascade = cv.CascadeClassifier('C:/Users/lucas/PycharmProjects/teste/Xml/banana_classifier.xml')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    bananas = banana_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in bananas:
        croppedImage = img[y:y + h, x:x + w]
        break

    return croppedImage
