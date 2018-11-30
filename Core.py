import Picture as pt
import Threshold as ts
import Histograma as ht
import File as fl


def show_menu():
    controle = True
    option = 0

    while (controle != False):
        print 'Informe sua Resposta!'
        print '1 - Obter Imagem a partir da WebCan'
        print '2 - Carregar uma imagem'
        print '3 - Sair'
        option = input()

        if option == 1:
            picture_retorn = pt.get_picture_web()
            ht.plot_histogram(picture_retorn)
            picture_segmentation = ts.adaptive_segmentation(picture_retorn)
            fl.save_picture(picture_segmentation)
            pt.status_banana(picture_segmentation)
            # fl.histogram_result()

        elif option == 2:
            picture_retorn = pt.get_picture()
            ht.plot_histogram(picture_retorn)
            picture_segmentation = ts.adaptive_segmentation(picture_retorn)
            fl.save_picture(picture_segmentation)
            pt.status_banana(picture_segmentation)
            #fl.histogram_result()

        elif 1 > option > 3:
            controle = True
        else:
            controle = False


def main():
    fl.delete_picture()
    show_menu()


if __name__ == '__main__':
    main()
