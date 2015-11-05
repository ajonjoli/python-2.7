# -*- coding: utf-8 -*-
#la primera línea permite usar caracteres especiales: acentos y ñ en comentarios y cadenas
# Python Manual de Python PEP8

# #!/usr/local/bin/python # shellbang, hashbang, sharpbang (para Linux)
# # indica al OS que el script se ejecuta utilizando el interprete dado por la dirección
# python archivo.py -i eggs -o bacon	es para llamar al archivo .pry y ejecutarlo con sus parámetros de entrada

#para usar sentencias python en C
#include <Python.h>
#Py_Initialize();
#PyRun_SimpleString("x=brave+sir+robin");

#para abrir un archivo file.py dentro de python
#import file	carga el archivo .py
#print file.var	usa una variable del interior del archivo

#from file import var	copia la variable del interior del archivo
#print var				la usa fuera (solo en el 1er uso calcula la variable del interior de su archivo)

#Tkinter GUI extensi on

#Reserved words
# and		def		exec		if		not		return
# assert	del		finally		import	or		try
# break		elif	for			in		pass	while
# class		else	from		is		print
# continue	except	global		lambda	raise

# python statements - Sentencias en Python
# assignment	curly, moe, larry = 'good', 'bad', 'ugly'
# calls			stdout.write('jajaja')
# print			print 'The Killer', joke
# if/elif/else	if 'python' in text: print text
# for/else		for x in mylis: print x
# while/else	while 1: print 'hello'
# pass			while 1: pass
# break,continue		while 1: if not line: break
# try/except/finally	try: action() except: print 'action error'
# raise			raise endSearch, location	#trigger exception
# import,from	imprt sys; from sys import stdin
# def,return	def f(a, b, c=1, *d): return a+b+c+d[0]
# class			class subclass: staticData=[]
# global		def function(): global x,y; x= 'new'
# del			del data[k]; del data[i:j]; del obj.attr
# exec			exec 'import '+modName in gdict, ldict	#ejecuta cadenas de código
# assert		assert x > y	#debugging checks

#	PRINT imprime un mensaje
print "hola mundo"
print 'hola a ti'

# funcionacomo getch() espera ingresar un [enter]
#raw_input()

#TIPOS DE DATOS
# números: enteros 3, flotantes 15.2, complejos 7+5j
# enteros: int 16, long 23L, octal 014, hexadec 0x3A
# reales: float 23.62, cientif 0.1e-3 =0.1x10^-3, complex 2.1+7.8js
a=23
print a
a=None	#None es el valor nulo null, vacía el contenido de la variable (como declaración)
print a
# cadenas string: "hola mundo" 'luis ortiz'
# cadena unicode u'jajaja' cadena raw r'jajaja'
# comillas triples ''' ''' """ """ respeta el formato editado
b="hola"
print u'áü'	# cadena tipo Unicode, permite símbolos avanzados
print r'\t'	# cadena cruda, no transforma los \
print '''Hola Sr.   Luis   .
     Bienvenido!
	a
	este
	mundo'''
#booleanos bool: True, False
c=False
c=True
print c

#conversiones de tipos de datos
x=345678
print str(x)	#convierte a cadena
x='tomato'
print list(x)	#convierte a lista
print tuple(x)	#convierte a tupla
x=2.73141516
print int(x)	#convierte a entero, trunca
print long(x)	#convierte a long, trunca
x=4
print float(x)		#convierte a flotante 4.0
print complex(x,0)	#convierte a complejo 4+0j
x=235690
print hex(x)	#convierte decimal a hexadecimal
print oct(x)	#convierte decimal a octal
x='H'
x=ord(x)	#convierte a ASCII una cadena de solo 1 caracter
x=chr(x)	#convierte a cadena de 1 caracter un código ASCII

print 'numbers:', 3.141, 1234, 999L, 3+4j
print 'strings:','spam',"guido's"
print 'lists:', [1, [2, 'three'], 4]
print 'tuples:',(1,'spam',4,'U')
print 'dictionaries:', {'food':'spam', 'taste':'yum'}
#print 'files:' text=open('eggs','r'),read()

# TYPE indica el tipo de dato
print type(a)
print type(b)

#dir() muestra las variables creadas hasta ahora
print dir()

#OPERADORES MATEMÁTICOS
# + suma - resta
print 3+4
print 5-2
# * multiplica ** exponente
print 2*6
print 2**6 # 2^6
# / división // división entera % módulo
print 3.0/2
print 3.0//2	#devuelve flotante truncado
print 3/2	# división de enteros es igual a división entera
print 3//2
print 7%3

#OPERADORES DE BIT
# & and | or ^ xor ~ not
# << desplazamiento izq >> desplazamiento der

#OPERADORES LÓGICOS
# and or not
# == != < > <= >=

#OPERADORES DE CADENAS
ff='roma'
gg='humo'
# + concatenador
print ff+gg
# * multiplicador
print ff*3

#OPERADOR DE LISTAS
#* splat operator: transforma una lista en una serie de argumentos
#func(*[3,4,5])	=equivale= func(3,4,5)

# x or y, x and y, not x
# lambda args: expression
# <, <=, >, >=, ==, <>, !=
# is, is not	identity test
# in, not in	membership
# x | y, x ^ y, x & y, ~x
# x << y, x >> y
# x+y, x-y
# x*y, x/y, x%y
# +x, -x
# x[i], x[i:j], x.y, x(...)	indexing,slicing,qualification,function calls
# (...), [...], {...}, '...'	tuple, list, dictionary, string


#caracteres especiales \
# \n newline \t newtab
print '\n'
print '\t xxx'
#raw_input()

#COLECCIONES DE DATOS
#LISTAS (arrays)
li=[22, True, "una lista", [1, 2]]	#puede contener distintos tipos de datos, incluso listas
li0=li[0]	#acceder a un elemento
print li[3][0]	#acceder a un elemento de sublista (matriz)
li[1]='jajaja'		#cambiar un elemento
print li
print li[-1], li[-2]	#acceder a elemento con índice de fin a inicio

la=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print la[2:7]	#2,3,4,5,6 acceder a partición [ini:fin] entra ini y no entra fin
print la[6:13:2]	#6,8,10,12 acceder a partición [ini:fin:jump]
print la[::3]	#si se omiten es [0,-1,1]
la[1:4]=[True]	#puede incluso modificar el tamaño de la lista
print la

#listas multidimencionales matrices matriz matrix
#mprof=[[0]*4]*8	#no funciona, si cambio un subdato se cambia en cada sublista
for i in range(len(8)):
	mprof[i]=[0]*4	#en cada elemento de los 8 de la lista, meter una sublista de 4
mprof=[[0]*4 for i in range(len(8))]	#con comprensión de listas es más corto
mprof=[[0 for j in range(len(4))] for i in range(len(8))]	#the same but longer

# L1=[]	empty list
# L2=[0,1,2,3]	4 items, indexes 0 to 3
# L3=['abc',['def','ghi']]	nested sublist
# L2[i], L3[i][j]		index
# L2[i:j]	slice
# len(L2)	length
# L1+L2	concatenate
# L2*3	repeat
# for x in L2	iteration
# 3 in L2		membership
# L2.append(4)	grow
# L2.sort()		sort
# L2.index(1)		search
# L2.reverse()	reverse
# del L2[k]		shrinking
# L2[i:j]=[]		shrinking
# L2[i]=1			index assigment
# L2[i:j]=[4,5,6]	slice assigment
# range(4),xrange(0,4)	make lists/tuples of integers

#las listas tienen funciones de modificación

#TUPLAS
#aplican las reglas de las listas, excepto al definirlas son paréntesis
tu=('la', 11, 22, True, False, 'je')
tu2= 'la', 11, 22, True, False, 'je'	#el verdadero operador es , no ()
ta= (12,)	#es una tupla, ta=(12) es un entero

print tu[1], tu[1:4]	#se particionan como las listas
print tu2[1::2]

#no modificables
ti=tu[1:5]
#tu[1]=True	produce error

#a diferencia de las listas, no contienen funciones de modificación
#sus elementos y tamaño no se pueden modificar
#por ser más básicas ocupan menos espacio en memoria que las listas

# ()	empty tuple
# t1=(0,)		1item tuple
# t2=(0,1,2)	3items tuple
# t2=0,1,2	another 3items tuple
# t3=('abc',('def','ghi'))	nested tuples
# t1[i],t3[i][j]	index
# t1[i:j]		slice
# len(t1)		length
# t1+t2		concatenate
# t2*3		repeat
# for x in t2	iteration
# 3 in t2		membership

#Los string también son secuencias como las listas y tuplas
c="hola mundo"
print c[::2]
print c[1]

# s1=''	empty string
# s2="spam's"	double quotes
# block="""....""" triple-quoted blocks (comentario documentación)
# s1+s2	concatenate
# s2*3	repeat
# s2[i]	index
# s2[i:j]	slice
# len(s2)	length
# 'a %s parrot' % 'dead'	string formatting
# for x in s2		iteration
# 'm' in s2		membership

#DICCIONARIOS matrices asociativas: colecciones que relacionan una clave y un valor
#name={clave0: valor0, clave1: valor1, clave2: valor2...}
#las claves son inmutables, por ello solo permiten nums, strings, boolean, tuplas
dic0={1: 'Victreebell', 2: 'Vileplume', 3: 'Voltorb', 4: 'Vulpix'}
dicA=dict(a=1, b=2, c=3)	#otra forma de crear lleno un diccionario
print dic0[2]	#se accede a los elementos por su clave

#permiten modificaciones
dic0[1]='Vaporeon'
print dic0
#no permiten particiones porque no son secuencias, son mapeos

# d1={}	empty dictionary
# d2={'spam':2,'eggs':3}	2items dictio
# d3={'food':{'ham':1,'eggs':2}}	nesting dictio
# d2['eggs'],d3['food']['ham']	indexing by key
# d2.has_key('eggs')		membership test
# d2.keys()			keys list
# d2.values()		values list
# d2.items()		(keys, values) tuples list
# len(d1)			length (num of stored items)
# d2[key]=new		adding, changing
# del d2[key]		deleting

#CONTROL DE FLUJO
print '\n'
#CONDICIONALES
#if <condicion>: <then>
#if <condicion>:
#	<then>
#	<then>
#if <condicion>: <then>; <then>; <then>
fa="euskera"
if fa=='euskera':
	print 'eus'
	print 'kera'

#else	if <condicion>: <then> else: <then>
if fa=='quechua':
	print 'que'+'chua'
else:
	print 'eus'+'kera'

#elif	if <condicion>: <then> elif <condicion>: <then> else: <then>
nume=1
if nume==0:
	print 'cero'
elif nume==1:
	print 'uno'
elif nume==2:
	print 'dos'
else:
	print 'tres'
print 'fue el número'

#compacto A if C else B Operador ternario
paredo='par' if nume%2 ==0 else 'impar'
print paredo
print 'par' if nume%2 ==0 else 'impar'

#switch no existe, se construye con un diccionario

#BUCLES
#while (condicion): (then)
while nume<=5:
	print 'baco '+str(nume)
	nume=nume+1

#break sale del bucle
while True:		#bucle infinito
	entrada= raw_input('> ')	#lo qe escriba el usuario
	if entrada=='bye':
		break		#sale al escribir 'bye'
	else:
		print entrada

#continue sale de la iteración
while nume<15:
	nume=nume+1
	if nume%3==0:
		continue
	print nume

#for elem in secuen: (then)
secuencia=['uno','dos','tres','four','five']
for i in secuencia:	#el iterador i se copia a un espacio temporal
	i=i*2	#si se modifica solo cambia dentro del ciclo, al reempezar ciclo i sigue su orden iterador ya dado
	print i
	#para modificar el iterador usar range(len()) o while

#Optimize for loop
#Only optimize the innermost loop
#An implied loop in map() is faster
#Avoid calling functions inside
#Local vars are faster than global vars, including functions
#Try map(), filter(), reduce() built-in functions
#built-in funcs with code are faster than for loops with code but these are faster than map() with lambda func


#FUNCIONES functions
print '\n'
#def mi_funcion(param1, param2): (body) return (var)
def imprime(dat1, dat2):
	"""documentación de la función imprime
	que se muestra cuando se pide help
	print param1 y print param2"""
	print dat1
	print dat2

imprime('data',3.14)
imprime(dat2='casi',dat1='angel')

def multiword(word='ja',vez=1):	# (param=default)
	print (word+' ')*vez

multiword('hola')	#('hola',1)
multiword('banco',4)
multiword(vez=3)	#('ja',3)

def suma(sum1, *otro):	# *otro es una tupla de número de elementos variable
#suma todos menos el primero
	tota=0
	for val in otro:
		tota=tota+val
	print tota

suma(1)
suma(1, 2)
suma(1,2,3,4)

def varios(para1, para2, **otros):	# **otros es un diccionario de número de elementos variable
	for i in otros.items():	#función de diccionario items: convierte en lista de sus elementos
		print i

varios(1,2, tercero=3)	#clave=tercero valor=3
varios(1,2, lunes='lun', martes='mar', miercoles='mie')

def suma2(a,b):
	return a+b	#devuelve 1 valor
print suma2(4,5)

def sumayresta(a,b):
	return a+b, a-b	#devuelve una tupla con los 2 valores
print sumayresta(6,2)	#muestra tupla con valores
c,d=sumayresta(6,2)
print c,d	#muestra los valores asignados

def f(x,y):
	x=x+3
	y.append(23)	#coloca al final de lista
	print x, y	#ambos cambian dentro

x=22
y=[22]
f(x,y)
print x, y	#x no cambia fuera, y sí cambió

#Operaciones matemáticas
print abs(-42)	#abs valor absoluto
print pow(2,4)	#pow potencia =2**4
print pow(2,4,2)	#3er parámetro es módulo
print range(5)	#del 0 al 4
print range(4,9)	#del 4 al 8
print range(0,31,3)	#del 0 al 30 de 3 en 3
print range(3,-3,-1)	#del 3 hacia atrás al -2
print min(5,2,6,7,3,9)	#regresa el menor de una secuencia: tupla
print min([3,5,8,5,1])	#:lista
print max(5,2,6,7,3,1)	#regresa el mayor de una secuencia: tupla
print [1,2,3].index(max(1,2,3))	#position of max
print max([3,5,8,5,1])	#:lista
print max(set([1,2,3,3,4,2]), key=[1,2,3,3,4,2].count)	#mode moda de una secuencia
print cmp(3,4)	#compara 2 valores x e y: x<y:=-1, x=y:=0, x>y:=1
print round(4.5555,3)	#redondea a 3 decimales, por default 0 decimales, los .5 se alejan del 0
print sum([2,4,5])	#suma todos los valores de una lista

#Built-in Functions
print repr([3,4,5])		#devuelve representación tipo cadena de un valor

# OOP Python orientado a objetos
print '\n'
# Clase
class Coche:
	"""Documentación de la clase"""
	def __init__(self, gasolina):	#constructor: se ejecuta al crear un objeto de la clase
		self.gasolina=gasolina	#self = this. de java
		print "Tenemos", gasolina, "litros"
	
	def arrancar(self):
		if self.gasolina>0:
			print "Arranca"
		else:
			print "No arranca"
	
	def conducir(self):
		if self.gasolina>0:
			self.gasolina-=1
			print "Quedan", self.gasolina, "litros"
		else:
			print "No se mueve"

#Objeto: instancia de clase
mivocho=Coche(3)	#de clase Coche con parámetro gasolina=3

#uso de atributos y métodos
print mivocho.gasolina	#atributo gasolina
mivocho.arrancar()
mivocho.conducir()	#and after 3-1
mivocho.conducir()	#and after 2-1
mivocho.conducir()	#and after 1-1
mivocho.conducir()	#doesn't move
mivocho.arrancar()
print mivocho.gasolina

#Herencia
class Instrumento:	#superclase
	Insax= 123	#atributo de clase, puede accederse y manipularse por todas sus instancias
	def __init__(self,precio):
		print "you can play"
		self.precio=precio
		Instrumento.Insax = 456
	
	def tocar(self):
		print "We play music"
	
	def romper(self):
		print "Eso lo pagas tú: $",self.precio

#subclase de instrumento
class Drums(Instrumento):
	pass	#nothing happens

class Guitar(Instrumento):
	def __init__(self,precio):
		Instrumento.__init__(self,precio)	#llamar método de superclase superclass.method(self,args)
		print "with strings"				#y agregarle sentencias

guitarra1=Guitar(40)

#Herencia múltiple
class Terrestre:
	def desplazar(self):
		print "El animal anda"

class Acuatico:
	def desplazar(self):
		print "El animal nada"

class Cocodrilo(Terrestre,Acuatico):	#en métodos iguales predomina el primero
	pass

coco=Cocodrilo()
coco.desplazar()	#predomina Terrestre

#Polimorfismo
def mover(animal):	#definimos función mover
	animal.desplazar()	#usa función desplazar que contiene código distinto en Terrestre y Acuatico

nemo=Acuatico()
nemo.desplazar()
mover(nemo)

venado=Terrestre()
venado.desplazar();	#a través de clase
mover(venado)		#a través de función con polimorfismo

#Encapsulamiento
class InfoPersonal:
	def publico(self):
		print "Esto es público"
	def __privado(self):
		print "Esto es privado"

Luis=InfoPersonal()
Luis.publico()
#Luis.privado() #esto produce error
Luis._InfoPersonal__privado()	#truco para entrar a función privada ._class__function

# getters y setters, encapsulamiento de atributos
class Weekday(object):	#para volverlo del tipo avanzado 3.0 se manda heredar de la clase object
	def __init__(self):
		self.__dia="domingo"
	def getdia(self):
		return self.__dia
	def setdia(self,dia):
		if dia=="domingo" or dia=="lunes" or dia=="martes" or dia=="jueves" or dia=="viernes":
			self.__dia=dia
		else:
			print "Error"
	dia=property(getdia,setdia)	#oculta los getters y setters en el uso

miweekday=Weekday()
print miweekday.getdia()
miweekday.setdia("jueves")
print miweekday.getdia()

miweekday.dia="martes"	#usan dia=property...
print miweekday.dia		#usa dia=property...

#métodos especiales
#__init__(self,args)
#inicializador, se ejecuta al crear el objeto

#__new__(cls,args)
#método 3.0, se ejecuta antes del _init_, es un constructor de la clase, no del objeto,
#por tanto su parámetro es cls, la clase

#__del__(self)
#método destructor, se ejecuta al borrar el objeto

#__str__(self)
#crea una cadena que representará al objeto
#se utiliza al usar print [obj] o str(obj)

#__cmp__(self,otro)
#se utiliza al usar operadores de comparación con objetos
#devuelve negativo si el obj es menor, 0 si iguales, positivo si mayor
#si no está definido la comparación lanza excepción
#== y != comprueba si son el mismo objeto, mismo id

#__len__(self)
#se utiliza al checar la longitud del objeto, como len(obj)

#Manipuladores de atributos de objetos: getters, setters
# hasattr(obj, attrn)		#devuelve 1 si el objo tiene al atributo attrn, else 0
# x=getattr(obj, attrn, default)	#getter: devuelve el atributo attrn de obj, si no existe devuelve default o AttributeError
# delattr(obj,attrn)		#borra el atributo attrn de obj, si no existe devuelve AttributeError
# setattr(obj,attrn,val)	#setter: asigna a val el atributo attrn de obj, si no lo soporta TypeError (cree o cambie el atributo)

#Métodos de los objetos básicos
#Diccionarios de datos

print '\n'
#Métodos de los objetos
#Diccionarios
dic1={1:'Algebra' ,2:'Biology', 3:'Chemistry', 4:'Statistics', 5:'Economics'}
#x.get(k,d)	muestra el valor en k, si no hay muestra d
print dic1[3]
print dic1.get(2)
print dic1.get(6,'algo')
#x.has_key(k) true si la clave existe, else false
print 1 in dic1
print dic1.has_key(1)
print dic1.has_key(6)
#x.items() muestra todas las claves y sus valores como una lista de tuplas
print dic1.items()
#x.keys() muestra una lista de las claves
print dic1.keys()
#x.values()
print dic1.values()
#x.pop(k,d)	borra la clave k del diccionario y devuelve su valor, si no hay muestra d
print dic1.pop(1)
print dic1.pop(7,'no borra nada')
print dic1.items()

#Cadenas
S='esta es una sentencia escrita en una cadena de python.'
#len(string) cuenta el número de caracteres que contiene
print len(S)
#x.count(sub,start,end)	cuenta las apariciones de sub en x,
#start y end definen la porción de x donde buscar
print S.count('es') #start=0
print S.count('es',2)
print S.count('una',7,30)
#x.find(sub,start,end)	devuelve la posición en que encontró sub en x o -1
#start y end definen la porción de x donde buscar pero no el inicio del índice
print S.find('una'),S.find('es'),S.find('ese')
print S.find('una',6),S.find('es',2)
print S.find('una',10,40)
#x.join(seq)	devuelve la concatenación de los símbolos en seq separadas por x
Op='+'
print Op.join('12345678')
#x.partition(sep)	devuelve una tupla con 3 elementos: subcad antes de sep, 1a aparición de sep, subcad del resto
#si no aparece: cadena,vacío,vacío
print S.partition('una')
#x.replace(old,new,cont)	devuelve cadena donde reemplaza todas las old por new, cont indica el máximo de ocurrencias a reemplazar
print S.replace('python','pitón')
print S.replace('una','jajaja',1)
#x.split(sep,maxsplit)	devuelve una lista con las subcad en que se divide x por sep,cont indica el máximo de divisiones a hacer
print S.split() #divide por default por whitespaces y \n
print S.split('una')
print S.split('es',2)
#x.splitlines() divide la cadena con separador \n
print S.upper(), S.lower()	#mayúsculas minúsculas

import string
#atof(string)	convierte '3.14' a flotante
print string.atof('3.14')
#atoi(string, base)	convierte '4' a entero de base (10 por default)
print string.atoi('4')
#atol(string,base)	convierte '555000' a long integer de base (10 por default)
print string.atol('555000')

#capitalize(st)	vuelve mayúscula la inicial
print string.capitalize('tomato and jones')
#capwords(st)	vuelve mayúscula cada inicial de palabra
print string.capwords('tomato, pepper, jones')
#expandtabs(st,tabsize)	cada tabulación en st la cambia a tamaño tabsize
#lower(st), upper(st)	devuelve st con todo en minúsculas/mayúsculas
#swapcase(st)	devuelve st con cada minúsucla convertida a mayúscula y viceversa

#find(s,sub,start,end)	regresa la posición de la 1a aparición de sub en s, o -1 si no está
print string.find('now is the time','is')
#rfind(s,sub,start,end)	(like find) devuelve la posición de la última aparición de sub en s
#index(s,sub,start,end)	(like find) pero devuelve ValueError exception si no está
#rindex(s,sub,start,end)	(like rfind) pero devuelve ValueError exception si no está
#count(s,sub,start,end)		devuelve el número de apariciones de sub en s
print string.count('now is the time','i')
#replace(st,old,new,maxsplit)	devuelve st donde cada aparición de old se reemplaza por new hasta maxsplit veces
print string.replace('now is the time',' ','-')
#split(s,sep,maxsplit)	divide s usando separador sep, con los separados se forma una lista hasta maxsplit separados
print string.split('now is the time')
#join(list,sep,maxsplit)	une en una cadena una secuencia de cadenas insertando sep entre cada una hasta maxsplit elementos
print string.join(['now','is','the','time'],'*')
print string.join('now is the time','+')	#una cadena es una lista de caracteres

#lstrip(s), rstrip(s), strip(s)	corta los espacios en blanco a la izquierda/derecha/ambos de s
print string.strip('     before and after     ')
#ljust(s,width), rjust(s,width), center(s,width)
#corre s hacia la izq/der/centro y rellena al otro lado con espacios hasta completas width caracteres

#quita todos los espacios en blanco extra de una cadena
thestring='     hola     mundo      '
thestring=string.strip(string.join(string.split(thestring)))
thestring=''.join(sentence.split())

#Listas
L1=['Monera','Protista','Fungi','Plantae','Animalia']
#len(list) cuenta el número de elementos que contiene
print len(L1)
#x.append(obj)	añade obj al final de x (procedimiento)
L1.append('Viruses')
print L1
#x.count(value)	devuelve las veces que está value en x
#print L1.count('Plantae')
L2=[2,3,[5,7],5,[7,9,11],7,9,11,13]
print L2.count(7)
#x.extend(iterable) añade los elementos de iterable a x
L1.extend('Viruses')
print L1
#x.index(value,start,stop)	devuelve la posición de 1a ocurrencia de value en x
#start y stop definen porción donde buscar
L3=[2,3,5,2,3,5,5,7,9,7,9,5,3,2]
print L3.index(5),L3.index(7)
print L3.index(3,5)	#start=5
print L3.index(5,6,10)	#stop=10
#x.insert(index,obj)	inserta obj en la posición index, arrimando los siguientes a la derecha
L1.insert(3,'eucariontes')
print L1
#x.pop(index)	devuelve el valor en posición index y lo saca de la lista
print L1.pop()
print L1.pop(10)
#x.remove(value)	elimina la 1a ocurrencia de value en x
L1.remove('i')
L1.remove('e')
print L1
#x.reverse()	invierte la lista (trabaja en la lista original)
L1.reverse()
print L1
#x.sort(cmp=None, key=None, reverse=False)	ordena la lista
#cmp es una función que tome de parámetros x,y (-1=x<y, 0=x=y, 1=x>y)
#key es una función que toma cada elemento y devuelve una clave a usar al comparar en su lugar
#reverse boolean que invierte la lista al final del ordenamiento
#print L1.sort()
L1.sort()
print L1

#Programación Funcional
print '\n'
#Funciones de orden superior: manejar funciones como valores,
#haciendo posible pasar funciones como parámetros o devolver funciones como resultado
def saludar(lang):
	def saludar_es():	#definición de funciones
		print 'Hola'
	def saludar_en():
		print 'Hello'
	def saludar_fr():
		print 'Salut'
	lang_func={'es': saludar_es, 'en': saludar_en, 'fr': saludar_fr}	#diccionario
	return lang_func[lang]	#devuelve función formada por el diccionario

f=saludar('es')	#f contiene función saludar_es
f()	#invocamos saludar_es()
saludar('fr')()	#invocación directa: () params de saludar, ()params de saludar_fr

#Iteraciones de orden superior
#map(función, seq, seq...) mapea, aplica una función sobre cada elemento de una secuencia
#devuelve una lista con el resultado de aplicar la función
#si se pasan n secuencias, la función debe pedir n parámetros
def sqared(n):
	return n ** 2
l4=[1,2,3,4,5,6,7,8]
print map(sqared,l4)

#filter(función, seq) filtra, verifica que los elementos de seq cumplan una condición
#devuelve una secuencia con los elementos que cumplen la condición
def paredo(n):
	return (n%2.0==0)
print filter(paredo,l4)

#reduce(función,seq, inicial) aplica función a todos los elementos de seq (par por par)
#devuelve un solo valor
#inicial es el primer valor a operar con el primer elemento y luego sucesivamente
def multi(x,y):
	return x*y
print reduce(multi,l4)

#Funciones lambda
#lambda sirve para crear funciones anónimas (sin nombre) en línea. Solo tienen un uso inmediato y no pueden ser referenciadas.
#están restringidas a solo una EXPRESIÓN (devuleve un valor, x=_expres_) y nunca pueden devolver False.
#se construyen: lambda param1, param2, param3: código
print filter(lambda n: n%2.0==0, l4)	#meter lambda a un parámetro
print reduce(lambda x, y: x*y, l4)

lala=lambda x: x+10	#meter lambda a una variable
print 'lambda',lala(21)

def suma_definida (n):
	return lambda x: x+n	#meter lambda a un return
f=suma_definida(2)	#x=2, x=5
g=suma_definida(5)
print f(23),g(23)	#n=23
print suma_definida(11)(22)	#x=11, n=22

#Map, Filter y Reduce perderán importancia.
#filter será parte del módulo functools
#map y filter serán desaconsejables por las list comprehensions

#Comprensión de listas. tomada de Haskell, permite crear listas de otras listas.
#expresión de modificación de cada elemento, una o más for y algun if
#[expresión for* variable in lista if* condición]
print [n**2 for n in l4]	#convertir a cuadrado
#l4=[n**2 for n in l4]
print [n for n in l4 if n%2.0==0]	#filtrar solo los pares
#l4=[n for n in l4 if n%2.0==0]
l=[0,1,2,3]
m=['a','b']
n=[s*v for s in m for v in l if v>0]	#=a*2
print n
# recorrer una matriz matrix
for i,j in ((i,j) for i in range(len(rows)) for j in range(len(cols)) ):
#no permite devolver más de un valor, si se requiere agrupe en tuplas
print [b for a,b in [(x,x+1) for x in range(15)]]	#también sirve para x.items() de diccionarios
print [(x-1,y) for x in [1,2,3,4] for y in [3,4,5,6] if x!=y and x!=4 and y!=5]
#comprehension tuple: no existen, pero un equivalente se crea así
a=tuple(a for a in range(4))
#generar diccionarios con comprensión de listas
dic={k: k+2 for k in range(4)}	#las claves son 1,2,3,4 y los valores 3,4,5,6

#Expresiones generadoras. No devuelven lista sino un generador, función que genera un valor a la vez cada que se piden.
#Funcionan como comprensión de listas excepto que utilizan paréntesis en vez de corchetes.
#Yield en lugar de return devuelve el sig valor
#Siempre es posible: lista=list(mi_gen) generar una lista de un generador
l5=(n**2 for n in l4)
print l5.next()	#= next(l5)
print next(l5)	#ejecutan el generador para el sig valor
print list(l5)	#generar una lista de un generador

def mi_gen1 (n,m,s):
	while (n<=m):
		yield n
		n += s
x=mi_gen1(0,5,1)
for n in mi_gen1(0,5,1):
	print n	#conforme se piden

#Decoradores: Función que recibe como param una función y devuelve otra función.
def addo(x,y):
	return x+y
def resto(x,y):
	return x-y
def apply(funca,x,y):	#función con otra función como parámetros
	return funca(x,y)
print 'dec',apply(addo,2,2)
print 'dec',apply(resto,5,2)

def mi_deco1(func):
	def nueva(*args):	#crea una func
		print "Llama a función", func.__name__	#función decorada
		retorno=func(*args)
		return retorno
	return nueva	#la devuelve

#Sintaxis: @fun2_qe_decora @función1_qe_decora def función_a_decorar: código
#así, siempre que se llame a a imp se llama a la versión decorada
@mi_deco1
def imp (cad):
	print cad,'a'
imp('hola')	#función ya decorada

#Sintaxis: función_qe_decora(función_a_decorar)(params_a_decorar)
mi_deco1(imp)('kako')	#decoración por una sentencia, en este caso función ya decorada 2 veces
imp('lalala')	#sin decorasión en sentencia, en este caso versión decorada

#EXCEPCIONES try except
print '\n'

#ejemplo que produce error
def division(x,y):
	return x/y
try:
	print division(3,0)
except:
	print 'No se puede dividir entre cero'

try:
	num=int('3a')
	print no_existe
#sólo entrará a un solo except, el primero que concuerde
except NameError:
	print 'La variable no existe'
except ValueError:	#éste es el caso,
	print 'El valor no es un número'
except (NameError, ValueError):	#una tupla de varios casos de error
	print 'Ocurrió un error'
except:
	print 'Tuvo un error que no previne en los anteriores'
else:	#ejecuta solo si no entró a ningun except
	print 'No hubo errores y puedo hacer esto'
finally:	#ejecuta siempre, entre a excepts o no
	print 'Uso para trabajos de limpieza'

class MiError(Exception):	#clase que hereda de clase Exception
	def __init__(self,valor):
		self.valor=valor
	def __str__(self):
		return 'Error '+str(self.valor)	#imprime cadena

try:
	resultado=21
	if resultado>20:
		raise MiError(33)	#provocar MiError a fuerza
except MiError, e:	#si cae en MiError: (except MiError as e)
	print e,'aaaa'	#e es el parámetro de MiError valor
#MiE(33)->MiE as e->_init_(valor)->return 'E'+.valor

#Excepciones disponibles Built-in Exceptions. except name_except:
#BaseException: superclase padre
#Exception(BE): superclase de las que no son de salida
#GeneratorExit(Exc): pide salir de un generador
#StandardError(Exc): superclase de las que no salen del intérprete
#ArithmeticError(SE): superclase de errores aritméticos
#FloatingPointError(AE): error en operación de coma flotante
#OverflowError(AE): resultado que tuve overflow
#ZeroDivisionError(AE): el 2o operando de una división o módulo es 0
#AssertionError(SE): falló la condición de un assert
#AttributeError(SE): no encontró atributo
#EOFError(SE): intentó leer más allá del fin de archivo
#EnvironmentError(SE): superclase de errores de I/O
#IOError(EE): error en operación de I/O
#OSError(EE): error en llamada a sistema
#WindowsError(OSE): error en llamada a sistema Windows
#ImportError(SE): no se encuentra el módulo que se quería importar
#LookupError(SE): superclase de errores de acceso
#IndexError(LE): el índice está fuera del rango posible
#KeyError(LE): clave no existe
#MemoryError(SE): no queda memoria suficiente
#NameError(SE): no se encontró ningun elemento con ese nombre
#UnboundLocalError(NE): nombre no asociado a ninguna variable
#ReferenceError(SE): objeto no tiene referencia hacia él
#RuntimeError(SE): error en tiempo de ejecución no especificado
#NotImplementedError(RE): método o función no implementado
#SyntaxError(SE): superclase de errores sintánticos
#IndentationError(SE): error en indentación
#TabError(IE): error debido a mezcla de espacios y tabs
#SystemError(SE): error interno de intérprete
#TypeError(SE): tipo de argumento no apropiado
#ValueError(SE): valor de argumento no apropiado
#UnicodeError(VE): superclase de errores por Unicode
#UnicodeDecodeError(UE): error al decodificar unicode
#UnicodeEncodeError (UE): error al codificar unicode
#UnicodeTranslateError (UE): error al traducir unicode
#StopIteration(Exc): indica final de iterador

#Warning(Exc): superclase de avisos
#DeprecationWarning(W): superclase de avisos sobre características obsoletas
#FutureWarning(W): semántica de construcción cambiará en un futuro
#ImportWarning(W): posibles errores al importar
#PendingDeprecationWarning(W): características que serán obsoletas pronto
#RuntimeWarning(W): comportamiento dudoso en tiempo de ejecución
#SyntaxWarning(W): sintaxis dudosa
#UnicodeWarning(W): problemas relacionados con Unicode, posibles problemas de conversión
#UserWarning(W): superclase avisos creados por programador
#KeyboardInterrupt(BE): programa fue interrumpido por user
#SystemExit(BE): petición de intérprete para terminar ejecución

#MÓDULOS y PAQUETES librerías y paqueterías packages
print '\n'
#MÓDULOS agrupan funciones
#importar un módulo: import <nombre_sin_extensión>
#el módulo importado debe estar en la misma carpeta o marcará ImportError
import this	#easter egg
import miModulo
import miMod as mm	#dar alias para trabajar el módulo importado
import os, sys, time #importación múltiple: os:
#funcionalidad relativa al OS, sys: funcionalidad relativa al intérprete Python, time: funciones para fecha y hora
#usar funciones del módulo module.funcion()
miModulo.miFuncion()
miModulo.miOtraFuncion()
mm.mimiFunc()	#llamar con alias
print time.asctime()	#da la fecha y hora
print sys.path	#direcciones donde buscará los módulos pedidos: actual y de sistema
#usar solo una función del módulo importado: from <module> import <función>
from time import asctime
print asctime()	#ya no requiere module.
#from time import *	#mala práctica, importar todas las funciones de otro módulo

#PAQUETES PACKAGES agrupan módulos, son tipos especiales de módulos
#se crea una carpeta, se insertan dentro los módulos
#se crea dentro un archivo __init__.py que normalmente es vacío
#importación
#<import> <paqete>.<subpaqete>.<modulo>
#from <paqete>.<subpaqete>.<modulo> import <funcion>
#from <paqete>.<subpaqete> import <modulo>	(esto produce)
#uso de funciones
#<paqete>.<subpaqete>.<modulo>.<funcion>()
#<modulo>.<funcion>()	(produce esto)
#Se pueden consultar paquetes en http://pypi.python.org/

execfile('file.py') #ejecuta el script con la dirección file.py

#Entrada/Salida Input/Output

#Entrada estándar: raw_input
#raw_input('pregunta')	el parámetro es una cadena a usar para pedir al usuario que escriba
#y devuelve una cadena con los caracteres introducidos hasta el Enter
nombre='LuEd'
#nombre=raw_input('Cómo te llamas? ')
print 'Encantado, '+nombre
#si requerimos un entero
edad=2.5
try:
	#edad=raw_input('Cuántos años tienes? ')
	dias=int(edad)*365	#convierte a enteros para usarlo en operación
	print 'Has vivido '+str(dias)+' días'	#convierte a cadena para usar en concatenación
except ValueError:
	print 'Esto no es un número'
#input es más compleja, lee la cadena y la evalúa como si fuera código Python, debe tratarse con cuidado

#parámetros en línea de comando, al llamar al programa
#python editor.py hola.txt
#se importa el módulo sys, que contiene la lista sys.argv
#sys.argv[0] contiene el nombre del programa, sys.argv[1] contendrá el 1er parámetro y así
import sys
if len(sys.argv)>1:
	print 'abriendo '+sys.argv[1]
else:
	print 'indiqe el nombre de archivo a abrir'

#Salida estándar: print
#print 'cadena'	imprime el contenido de la cadena en una línea
#para que el sig print se imprima en la misma línea se coloca una coma al final
for i in range(4):
	print i,
print 'hola','mundo'	#coma, separa cadenas por un espacio
print 'hola'+'mundo'	#adición+ concatena cadenas como estén
print 'hola',34,5.999	#coma no requiere convertir tipos
print 'hola '+str(34)+' '+str(5.999)	#+ requiere convertir a cadena todo str(x)
#formateo de valores
#Formatos y especificadores
# %s: cadena,	%d: entero,	%o: octal,	%x: hexadecimal,	%f:	flotante
print 'Hola %s' % 'mundo'	#toma mundo y lo pasa al lugar %s convertido a string
print '%s %s' % ('Hola','mundo')	#para pasar varias variables se forman en tupla
#si se añaden números al formato indica mínimo de caracteres
print '%10s mundo' % 'Hola'	#añade espacios a la izqierda hasta ser 10 chars
print '%-10s mundo' % 'Hola'	#añade espacios a la derecha hasta ser 10 chars
#si se añade un punto y cantidad indica decimales a mostrar
from math import pi
print '%.5f' % pi	#pi con 5 decimales
#si se añade un punto y cantidad indica número de caracteres a mostrar
print '%.6s' % 'hola mundo'

#Archivos. objetos tipo file creados con la función open.
#variable=open("dirección",modo_acceso,tamaño_buffer)
#variable donde se deposita el objeto tipo file
#dirección relativa o absoluta
#opcional el modo de acceso (default: modo lectura)
#	r: read only, debe existir o lanza excepción IOError, posición al inicio.
#	w: write only, si no existe se crea, si existe lo sobreescribe. posición al inicio.
#	a: append, write only, si existe empieza a escribir al final, si no existe lo crea. No cambia lo ya escrito antes de abrir.
#	b: binary, trabaja con el contenido en binario (rb, wb, ab)
#	+: permite lectura y escritura al mismo tiempo (r+, w+, a+)
#		r+: lectura y escritura, posición al inicio.
#		w+: lectura y escritura, posición al inicio, permite leer lo ya escrito y también lo borra al abrir
#		a+: lectura y escritura, posición al final, no cambia lo ya escrito antes de abrir y a la vez lo puede leer.
#	U: universal newline, trabaja con saltos de línea compatibles e incompatibles al OS
#opcional el tamaño de buffer con un entero en bytes
fl=open('C:/Documents and Settings/ajqnjqli/Escritorio/archivo.txt','r+')	#crea archivo.txt
#fl2=open('nuevoarchi.txt','w+')	#en este caso, lo guarda en C:/ArchdeProg/Notepad++/ o desde el acceso que se ejecute este py
print fl

#Lectura de archivos. File read
#f.read(n) devuelve una cadena con el contenido del archivo o los n bytes tamaño máximo a leer
parte=fl.read(8)
completo=fl.read(13)	#leyó el resto
print parte
print completo
#f.readline() devuelve una cadena con el contenido de la sig línea del archivo hasta Enter
while True:
	linea=fl.readline()
	if not linea:
		break
	print linea,	#el Enter está incluido en la lista, si hace otro será doble Enter
#f.readlines() devuelve una lista con todas las líneas del archivo.

#Escritura de archivos
#f.write('cadena') escribe en el archivo 'cadena'
fl.seek(0,2)	#moverse al final del archivo
fl.write('hola mundo de archivos\n')
fl.write('hola mundo de archivos\n')
fl.write('linea 3\n')
#f.writelines(lista)	escribe en el archivo líneas de cadenas establecidas en una lista, cada elemento debe contener su '\n'

#Mover posición en archivo
#f.seek(num)	se desplaza a una posición num lugares hacia adelante desde el principio.
#f.seek(n,from)	o puede ser desplazamiento relativo con from: 0 es inicio (default), 1 pos actual, 2 final; incluso desplazamiento negativo
#f.tell()	devuelve un entero con la distancia en bytes desde el inicio del archivo.

#al terminar de trabajar con cada archivo se debe cerrar con close
fl.close()
print fl	#avisa que el archivo no está abierto por el programa
#fl2.close()

#copia todo el contenido de un archivo a otro
#f = open("origen.txt")
#g = open("destino.txt","w")
#linea = f.readline()
#while linea != "":
#	g.write(linea)
#	linea = f.readline()
#g.close()
#f.close()

#Files
# outvar=open('/tmp/spam','w')	crea un archivo para escribirle
# invar=open('data','r')			abre un archivo para leerle
# S=invar.read()		lee todo el archivo dentro de una cadena
# S=invar.read(N)		lee N bytes
# S=invar.readline()	lee la sig línea, incluido el marcador de fin de línea
# L=invar.readlines()	lee todo el archivo en una lista de cadenas (cada cadena=1 línea con su \n)
# outvar.write(S)		escribe la cadena S en el archivo
# outvar.writelines(L)	escribe todas las cadenas en la lista L en el archivo (ya debe tener cada elemento su '\n')
# outvar.close()		cierra archivo manualmente

#Pickle Module: convierte objetos en string
#import pickle	primero se manda a llamar al módulo Pickle
#pickle.dump(obj,file)	el contenido de obj se escribe en el archivo file abierto para escribir convertido en string
#obj=pickle.load(file)	el contenido de file abierto para leer, se guarda en el objeto obj

#Expresiones Regulares: patrones que describen cadenas de caracteres
import re
#módulo regular expressions, tiene el objeto RegexObject cuyos métodos son match,search,split...
#y tiene funciones atajo que crean RegexObject internos automáticos
#estas funciones verifican si una cadena sigue un patrón dado por una expresión regular

#re.compile('regexp',flags)	método base del módulo, compila un patrón en un objeto RegexObject,
#que puede ser usado para sus métodos match() y search()
prog=re.compile('.a.a')
result=prog.match('baba')
# == result=re.match('.a.a','baba') pero crear manualmente el RegexObject prog permite usarlo again

#elementos básicos de expresiones regulares
#.	cualquier caracter excepto newline
#^	inicio de cadena
#$	fin de cadena
#*	0 o más ocurrencias de lo predecesor
#+	1 o más ocurrencias de lo predecesor
#|	lo anterior o lo siguiente
#\w	cualqier alfanumérico
#\d	cualqier digito decimal
#toma	la cadena toma

#re.match(regexp,cadena,flags) comparar si una cadena se ajusta exactamente a un patrón regexp
if re.match('python','python'):	#1er regexp la 'cadena'
	print 'python\t',
if re.match('.ython','jython'):	#el . indica cualquier caracter una vez, excepto \n
	print '.ython\t',
if re.match('...\.','abc.'):	#tres caracteres y el punto, \ indica que no se tome como patrón
	print '....\t',
if re.match('python|jython|cython','python'):	# el | indica OR, alguna de las 3 opciones nada más
	print 'una|otra\t',
if re.match('(p|j|c)ython','cython'):	#cualquiera de los 3 caracteres, () indican grupo secuencial
	print '(p|j|c)\t',
if re.match('[pjc]ython','jython'):	#cualquiera de los 3 caracteres, [ ] indican conjunto de caracteres
	print '[pjc]\t',
if re.match('py[0-9]','py5'):	# el - indica rango, del 0 al 9
	print '[0-9]\t',
if re.match('py[a-f]','pyb'):	#python y cualquier minúscula de a hasta f
	print '[a-f]\t',
if re.match('py[0-9a-zA-Z]','pyx'):	#cualquier digito o letra MAY o min
	print '[0-9a-zA-Z]\t',
if re.match('py[.,]','py.'):	#un punto o una coma, sin \
	print '[.,]\t',
if re.match('py[^0-9a-z]','pyT'):	# el ^ indica NOT, cualqier caracter excepto dígito o minúscula
	print '[^0-9a-z]\t',
#secuencias especiales
# '\d' un dígito =[0-9]
# '\D' cualqier caracter excepto dígitos =[^0-9]
# '\w' cualqier caracter alfanumérico =[a-zA-Z0-9_]
# '\W' cualquier caracter NO alfanumérico =[^a-zA-Z0-9_]
# '\s' cualquier caracter en blanco. =[ \t\n\r\f\v]
# '\S' cualquier caracter que no sea espacio en blanco =[^ \t\n\r\f\v]
if re.match('py\d','py3'):
	print '/d\t',
if re.match('py[ab]+','pyabababab'):	#el + indica que puede estar 1 o más veces
	print '[ab]+\t',
if re.match('py[ab]*','py'):	# el * indica que puede estar 0 o más veces
	print '[ab]*\t',
if re.match('py[xa]?','pyxa'):	# el ? indica opción, puede estar 0 ó 1 vez
	print '[xa]?\t',
if re.match('pyo{3}','pyooo'):	# las {} indican el número de veces exacto que se espera aparezca
	print 'o{3}\t',	#{3,8} de 3 a 8 veces, {,8} de 0 a 8 veces, {3,} 3 ó más veces.
if re.match('^http','http:/google.com'):	# el ^ indica que debe estar al principio
	print '^http\t',
if re.match('\w*com$','wwwgooglecom'):	# el $ indica que debe estar al final
	print 'com$'
#si el regexp no concuerda con la cadena, regresa None, o si lo encuentra un objeto tipo MatchObject
#MatchObject tiene los métodos start y end que devuleven las posiciones de inicio y fin de la subcadena reconocida
#y los métodos group y groups que acceden a los grupos que propiciaron el reconocimiento de la cadena
#group sin params devuelve el grupo 0, la subcadena reconocida
mo=re.match('http://+\net','http://mundogeek.net')
#print mo.group()
#groups devuelve una lista con todos los grupos excepto el grupo 0
	
#Módulo re
#flags de re, se colocan en el param opcional flags y pueden usarse varios separados por |
#re.DEBUG:	muestra información de la compilación
#re.IGNORECASE: no importan las mayúsculas o minúsculas (re.I)
#re.VERBOSE: ignora los espacios y comentarios en la cadena de la regexp (comment #...) (re.X)
#re.DOTALL: el . también incluye al \n newline (re.S)
#re.MULTILINE: el ^ verifica cada inicio de línea (\nx), el $ busca cada fin de línea (x\n) (re.M)
#re.UNICODE:	permite el Unicode en \w, \b, \d (re.U)

#re.search('regexp','cadena',flags) a diferencia de match, busca que cualquier subcadena se ajuste
#su método start no será siempre 0 como en el caso de match, crea MatchObject
if re.search('com$','www.google.com'):	# el $ indica que debe estar al final
	print 's:com$\t',
if re.search('a{2,4}?','pyaaaaaaa'):	#con el ? en lugar de buscar primero 4 as, busca 2 as antes
	print 'a{2,4}?\t',
if re.search('Isaac (?=Asimov)','Isaac e Isaacarina leen a Isaac Asimov'):	#solo si después va Asimov
	print '?=asimov\t',
if re.search('Isaac (?!Asimov)','Isaac e Isaacarina leen a Isaac Asimov'):	#solo si después NO va Asimov
	print '?!asimov\t'

#re.findall('regexp','cadena') devuelve una lista con las subcadenas que cumplieron el patrón
print re.findall('.a','cccbaccccbaccccbaccc')
#re.finditer('regexp','cadena') devuelve un iterador a usar para consultar los distintos MatchObject

#re.split('regexp','cadena',int,flags) divide la cadena máximo en int (opcional)
#usando el patrón como punto de separación, devuelve una lista con las subcadenas
#si no encuentra el patrón, no divide
print re.split('\W+','Words, words, words.')	#borra los espacios, o los regexp de la lista resultante

#re.sub('regexp','cadnare','cadena',int,flags)	sustituye en una cadena cada que encuentra el patrón
#por el contenido de cadnare, int opcional indica máximo de sustituciones.
print re.sub('amor','Edhu','amor, nunca dejarás de ser amor')
#re.subn('regexp','cadnare','cadena',int,flags)	lo mismo que sub pero devuelve una tupla
#una tupla que contiene ('cadena nueva',número de subs hechos)

#Al llamar a estos métodos se crea un nuevo objeto tipo re.RegexObject
#que representa la expresión regular con métodos del mismo nombre que las funciones (split,sub) del módulo.
#Si usaremos un mismo patrón varias veces es mejor crear un objeto RegexObject
#y llamar nosotros a sus métodos, para evitar que el intérprete cree un objeto por cada búsqueda
#Para crear un objeto RegexObject se usa la función compile (de re.) al que se pasa de param la cadena 'regexp' y opcional unos flags
#la clase RegexObject contien los sig métodos y atributos:
#search('cad',inicio,fin)	(=re.search) inicio y fin marcan sus posiciones en la búsqueda
#match('cad',inicio,fin)	(=re.match) inicio y fin marcan sus posiciones en la búsqueda
#split('cad',int)	findall('cad',inicio,fin)	finditer('cad',inicio,fin)
#sub('cadrep','cad',int)	#subn('cadrep','cad',int)
#flags: atributo, las banderas levantadas
#groups: número de grupos capturados por el patrón
#groupindex:	diccionario de grupos capturados por el patrón
#pattern:	patrón regexp con que se usó su compile()

#re.MatchObject: donde se arrojan los resultados de búsqueda, siempre tiene valor boolean True
#si la búsqueda no encontró nada no se crea
#matcha=re.search(...)
#if matcha:
#	procesamiento a MatchObject
#Métodos y atributos:
#group(index,index...)	devuelve 1 ó más subgrupos producto de la búsqueda
#	si pedimos 1 grupo devuelve una cadena, si pedimos más devuelve una tupla
#groups()	devuelve una tupla con todos los subgrupos de la búsqueda
#start(grupo), end(grupo)	devuelve el índice del inicio y fin de la subcadena encontrada
#span(grupo)	devuelve una tupla (m.start(g), m.end(g))
#inicio, fin	atributos, posiciones de inicio y fin de la subcadena encontrada
#lastindex, lastgroup	atributos, índice y nombre del último grupo capturado
#re	atributo, patrón con que se buscó match y search
#string	atrib, cadena sobre la que buscar el patrón

#Módulo OS, comunicación con sistema operativo, shell script
import os
#getcwd()	devuelve una cadena con la dirección actual de trabajo
print os.getcwd()
#listdir(path)	devuelve una lista con todos los archivos y carpetas en la dirección path
print os.listdir(os.getcwd())
#mkdir(path,mode)	crea un directorio path con modo mode
os.mkdir('nevacarp')
#remove(path), unlink(path)	borra un ARCHIVO path específico
#rmdir(path)	borra un DIRECTORIO path
os.rmdir('nevacarp')
#rename(src,dest)	cambia el nombre a un archivo src por dest
#chown(path,uid,gid)	cambia el ownerID a uid y groupID a gid de un archivo con dirección path
#chmod(path,mode)	cambia los permisos de un archivo con dirección path. mode es un modo numérico de permisos (0644=rw owner, r everyone)
#system(command)	ejecuta el comando shell en un subshell, el valor de regreso es el de la sentencia
os.system('dir')

#atributos de módulo os
#os.name	versión actual de la interfaz del OS (posix,nt,dos,mac,ce,java)
print os.name
#os.error	clase usada cuando las llamadas en el módulo os provoqen errores.
#contiene 2 variables: errno: número de error, strerror: cadena de mensaje explicando el fallo
#os.environ	diccionario con las variables de ambiente del shell de donde se llamó a python

#palabras reservadas a usar en path
#curdir		di-rección actual
#pardir		dirección del padre
#sep		caracter que separa carpetas en path (/ en Unix, \ DOS, : Mac)
#altsep		caracter separador alterno si lo hay (/ DOS y Windows únicos)
#pathsep	caracter que separa componentes (: Unix, ; DOS Windows)

#módulo os.path
#split(ph)	divide el directorio ph en una tupla (camino a la carpeta, archivo) =(dirname(ph),basename(ph))
print os.path.split(os.getcwd())
#join(ph1,ph2..)	concatena cadenas que representan partes de un path
#exists(ph)		true si path existe
#isfile(ph), isdir(ph), islink(ph)		true si ph es un archivo/carpeta/enlace
#samefile(p,q)	true si ambos paths p y q van al mismo archivo

#módulo shutil	para copiar archivos sin permisos especiales
import shutil
#copyfile(src,dest)	hace una copia de src y la llama dest (copiado binario)
#copymode(src,dest),copystat(src,dest)	copia los permisos de src en dest, o permisos y utime de src en dest

#Ordenamiento
#sorted: crea una nueva lista de los elementos ordenados y deja la secuencia intacta, trabaja en listas, tuplas, diccionarios
ja=sorted((4,6,3,2,1))
ja=sorted((4,6,3,2,1), reverse=True)
#las tuplas no se modifican, para ordenarlas se hace una lista copia y ésta se ordena
tupla=(47,63,15,84,5,37,24,71)
listcop=list(tupla)
listcop.sort()
print listcop
#los diccionarios no se ordenan, para ordenarlos se hace una lista copia con las llaves del diccionario
diccio5={4:'abeja',1:'barco',7:'condor',2:'delta',6:'esfera'}
keys=diccio5.keys()
keys.sort()
#print keys
for key in keys:
	print key,diccio5[key]
#ordenamientos especiales: ordenar cadenas sin importar mayús/minús
def sincaseSort(a,b):	#se hace una función de comparación que tome 2 argumentos (de 2 en 2)
	a,b=string.lower(a),string.lower(b)
	return cmp(a,b)		#y devuelva -1, 0, 1 correspondiente a a<b, a=b, a>b
lis5=['This','is','A','sorted','List']
lis5.sort()
print lis5	#mal ordenado
lis5.sort(sincaseSort)
print lis5	#usando función de comparación

#números aleatorios, Randomizing: módulo random
import random
#randint(a,b)	genera un entero aleatorio t.q. a<=N<=b
print random.randint(3,10)
#random		genera un flotante aleatorio 0.0<=N<1.0
print random.random()
#uniform(a,b)	genera un flotante aleatorio t.q. a<=N<=b
print random.uniform(2,9)
#choice(seq)	elige un valor de una secuencia no vacía
lis6=[1,2,3,'a','b','c']
print random.choice(lis6)
#shuffle(seq)	reordena aleatoriamente una secuencia seq
random.shuffle(lis6)
print lis6
#sample(seq,k)	elige k elementos aleatorios de la secuencia seq
print random.sample(lis6,3)
#elegir números al azar de un rango sin repetir hasta acabar
lis7=range(4,20) #num al azar del 4 al 20
while lis7:
	ele=random.choice(lis7)
	lis7.remove(ele)
	print ele,

#Funciones del tiempo
import time
print time.localtime() #muestra la hora actual
print time.gmtime(0) #muestra el tiempo en que empezó a funcionar el reloj de Python
print time.time() #muestra la hora actual en segundos (desde gmtime)
inicio=time.time()
final=time.time()
print inicio-final #muestra los segundos transcurrido entre 2 instantes del programa
raw_input()

#Funciones matemáticas
import math
print math.ceil(3.5)	#techo del número
print math.floor(3.3)	#piso del número
print math.sqrt(2)		#raíz cuadrada
print math.fsum([0.1,0.2])	#sum more precisely floating point numbers
#another way is round(sum(0.1,0.2),4)

zip(['a','b','c'],[1,2,3])	#crea una lista de correspondencias de listas
import cmath #trabaja con números imaginarios, complejos
print cmath.sqrt(-25)	#5j raíz cuadrada de incluso negativos

#NumPy: módulo para cómputo científico		tonotron_ipn@hotmail.com
import numpy as np	#alias de biblioteca
print np.random.rand()	#devuelve un flotante aleatorio entre 0 y 1
print np.random.randint(100,1000)	#devuelve entero aleatorio entre 100 y 1000 (sin mil)
print np.random.choice(3,p=[0.3,0.4,0.3])	#devuelve un entero entre 0 y 3, donde cada valor tiene un peso weighted random
a = np.array([1,2,3])	#data type for vectors and matrices
b = np.array([[1,2,3],[4,5,6],[7,8,9]])
print np.dot(b,b)	#matrix multiplication

#Extracción de datos de páginas web
#Se recomienda usar el módulo requests pero éste debe instalarse
#por ello usaremos urllib2 y urllib
import urllib2	#importa librería de trabajo con URLs
response=urllib2.urlopen('http://www.uniprot.org/uniprot/B5ZC00.fasta')
#urlopen abre http:, ftp:, file: y asigna el objeto a una variable
print response.info()			#muestra las cabeceras del url abierto
print response.info()['server']	#un valor del diccionario info
print 'url',response.geturl()
print 'code',response.code
#lectura de contenido, solo se usa una de las 3 una vez.
html=response.read()		#1: como en archivos, lee todo en una cadena
print '>>>'+html+'<<<'
print response.readline()	#2: como en archivos, solo lee una línea en una cadena
html=response.readlines()	#3: como en archivos, lee todo en una lista de líneas
print html
for line in response:		#4: lee el objeto response como lista
	print line.rstrip()
#permite descargar en un archivo la página web
leo=open('descargado.html','w')	#cuando no sean archivo de texto, como mp3, usar 'wb'
leo.write(response.read())	#escribe en descargado.html la lectura de response
leo.close()

response.close()	#cierra el uso de la página web

#Conexión a una base de datos MySQL
#Instalar el módulo python-mysql
import MySQLdb	#importa el módulo de comunicación
db=MySQLdb.connect(host="localhost", user="root", passwd="pato", db="test")	#conecta con un user y pw a una db
cur=db.cursor()				#con un objeto cursor manda los comandos

#instrucciones de despliegue
cur.execute("show tables")	#manda un comando de desplegar tabla
print cur.fetchall()		#muestra la tupla con el contenido de la tabla
cur.execute("select * from ja")	#manda otro comando desplegar tabla
for x in cur.fetchall():		#muestra la tabla ordenada a través de un for que recurre una tupla de tuplas
	print x[0],'\t',x[1]		#cada tupla contiene el conjunto de los atributos del registro
#también existen fetchone y fetchmany. execute y executemany

#instrucciones de cambio
try:				#prueba un comando de cambios
	cur.execute("insert into ja values(20,0)")	#manda un comando de cambios
	db.commit()									#lo guarda si no falló
except:			#por si falla
	db.rollback()	#regresar a su estado anterior

cur.close()	#cierra el cursor

#declara set
a=set()
#agregar a un set
a.update(['hola'])
#eliminar de un set
a.remove('hola')

#print de python3
a=3
b='xx'
print(b)
print('jaja')
print('jaja {0}'.format(a))
print('kay{1} {0}'.format(b,a))
