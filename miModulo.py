#mandado a llamar por Python manual.py en la sección Módulos y paquetes
def miFuncion():
	print "una función"

def miOtraFuncion():
	print "otra función"
	
class miClase:
	def __init__(self):
		print "una clase"

print "un módulo"	#la primera ejecución de alguna función de este módulo ejecuta esto

if __name__=='__main__':
#atributo name: si es importado es el nombre del archivo, si es ejecución directa es main
	print 'Se mostrará si no es importado'
