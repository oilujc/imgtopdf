
class Static():

	@staticmethod
	def _bienvenida():
		print("Bienvenido a JPG to PDF")
		print("Created By: Julio Martinez")

	@staticmethod
	def _menuAccionesImgFalse():
		print("--ACCIONES--")
		print("1) Cambiar directorio")
		print("2) Salir")
		opc = int(input(">>> "))
		return opc

	@staticmethod
	def _menuAccionesImgTrue():
		print("--ACCIONES--")
		print("1) Convertir imagenes a pdf")
		print("2) Cambiar directorio")
		print("3) Salir")
		opc = int(input(">>> "))
		return opc