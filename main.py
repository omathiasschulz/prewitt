from Prewitt import Prewitt

# realiza a geração das imagens
prewitt = Prewitt('Fig1.ppm')
prewitt.generate()
prewitt = Prewitt('Fig2.ppm')
prewitt.generate()
prewitt = Prewitt('Fig4.ppm')
prewitt.generate()
prewitt = Prewitt('FigDollar.tif')
prewitt.generate()
