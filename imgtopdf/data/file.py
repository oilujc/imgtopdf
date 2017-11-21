import os, sys
from os import listdir
from fpdf import FPDF
from os.path import isfile, join
from .validaciones import Validaciones
from .static import Static


class File():
	def __init__(self):
		Static._bienvenida()
		self._fpdf = FPDF()

	def obtenerDirectorioImagenes(self,ruta = '.'):
		dirs = listdir(ruta)

		fin = False

		while fin != True:
			try:
				os.system("cls")

				acc = self.listarImagenes(ruta, dirs)

				if acc:

					opc = Static._menuAccionesImgTrue()

					if opc == 1:
						nombre = str(input("Ingrese el nombre del archivo PDF: "))
						self.convertImagenes(nombre, ruta, dirs)

					elif opc == 2:
						pass

					elif opc == 3:
						fin = True
					else:
						print("Debes seleccionar una opcion valida")

				else:
					opc = Static._menuAccionesImgFalse()

					if opc == 1:
						pass
					elif opc == 2:
						fin = True
					else:
						print("Debes seleccionar una opcion valida")

			except Exception as e:

				print("Error %s"%(e))

	def convertImagenes(self,nombre, ruta, dirs):
		dicc = Validaciones._listarImagenes(ruta ,dirs)
		for index, imagen in dicc.items():

			self._fpdf.add_page()
			self._fpdf.image(imagen,20,20,170,170)
			print("%s, añadido al archivo"%(index))

		arch = nombre + ".pdf"
		self._fpdf.output(arch, "F")
		print("Hecho")
		input("Continuar...")

	def listarImagenes(self, ruta, dirs):
		print("IMAGENES")
		dicc = Validaciones._listarImagenes(ruta ,dirs)

		for index, imagen in dicc.items():
			print("%s || %s"%(index, imagen))

		if "Respuesta" in dicc:
			return False
		else:
			return True
		