import cv2 as cv2


def adaptive_segmentation(imagem):
    _, threshold = cv2.threshold(imagem, 155, 255, cv2.THRESH_BINARY)

    cv2.imshow("Img", imagem)
    cv2.imshow("Binary threshold", threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return threshold
