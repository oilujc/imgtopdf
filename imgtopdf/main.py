import os, sys
from data.file import File
from data.validaciones import Validaciones


def main():
	pdf = File()
	ruta = Validaciones._validarRuta()
	pdf.obtenerDirectorioImagenes(ruta)



if __name__ == '__main__':
	main()