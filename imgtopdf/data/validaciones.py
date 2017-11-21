from .extensiones import Extensiones

class Validaciones():
	
	@classmethod
	def _validarRuta(self):
		print("Ingrese una ruta valida:")
		ruta = input(">>> ")

		if ruta == "" or ruta.isspace():
			print("Debes ingresar una ruta valida")

		else:
			return ruta

	@classmethod
	def _validarImagenes(self, img):
		exist = 0
		for extensiones in Extensiones.lista:
			if extensiones.lower() in img:
				exist = 1

		return exist

	@classmethod
	def _listarImagenes(self, ruta, dirs):

		dicc = {}
		cont = 0
		var = ""

		if dirs != "" or ruta.isspace():
			for imgs in dirs:

				img = Validaciones._validarImagenes(imgs)

				if img:
					cont += 1
					var = ruta + "\\" + imgs
					dicc[imgs] = var

				var = ""

		if cont == 0:
			resp = "No hay imagenes en este directorio"
			dicc["Respuesta"] = resp
			return dicc

		else:
			return dicc
				



		
