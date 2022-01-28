lista=""
lista_nums="123456789"
lista_alfa="abcdefghijklmnñopqrstuvwxyz"
por="*"
mas="+"
lista_alfabeto=[lista_nums,lista_alfa,por,mas]
lista_otro=lista_nums+lista_alfa+por+mas

def esta_en_tabla(val):
	if val in lista_nums:
		return lista_nums
	if val in lista_alfa:
		return lista_alfa
	if val in mas:
		return mas
	if val in por:
		return  por
def crea_tabla_tansiciones():
	graph = {}
	graph[(0, lista_nums)] = 6
	graph[(0, mas)] = 1
	graph[(0, "otro")] = "*"
	
	graph[(1, mas)] = "**"
	graph[(1, "otro")] = "*"
	# graph[(3, mas)] = "*"
	# graph[(3, "otro")] = "**"
	
	graph[(6, lista_nums)] = 6
	graph[(6, "otro")] = "*"
	# graph[(4, otro)] = "*"

	# graph[(1, lista_alfabeto)] = 2
	# graph[(1, "+")] = 9
	# graph[(1, "*")] = 11
	# graph[(1, "contenido")] =
	

	return graph


tabla = crea_tabla_tansiciones()

# print(tabla[(1, ")")])
file = open('file.txt', 'r')
lista_tokens = []
lista_identificadores = []
insertados = 1
otro = False
# num = ""
apilando_letra = False
dejo_de_apilar = False
end = False
buffer = ""
singleton = False

char="V "
pila=""
posicion_grafo=0

A=0
while 1:
	
	if posicion_grafo=="*":
		file.seek(a - 1)
		otro = False
	char = file.read(1)
	if not char:
		buffer=""
	a = file.tell()
	buffer=char
	singleton = False
	ciclo = True
	while ciclo:
		# if buffer:
		# singleton = False
		hallado=False
		for i in lista_alfabeto:
			for x in i:
				# print(buffer)
				# print(x)
				if hallado:
					break
				if str(x)==str(buffer) and singleton==False:
					t=esta_en_tabla(char)
					try:
						# print(posicion_grafo)
						# print(t)
						posicion_grafo= tabla[( posicion_grafo,t)]
						pila = pila + buffer
						# print(buffer)
					except Exception as e:
						posicion_grafo = tabla[(posicion_grafo, "otro")]
					singleton=True
					# print(x)
					
					ciclo=False
					hallado=True
		if not  hallado:
			posicion_grafo = tabla[(posicion_grafo,"otro")]
			# print("no hallado")
			# print(posicion_grafo)
			
		# print(pila)
		if posicion_grafo=="*":
			print("termina cadena")
			posicion_grafo = 0
			print(pila)
			pila=""
			break
		if posicion_grafo == "**":
			print("termina cadena ++")
			a=a-1
			posicion_grafo = 0
			print(pila)
			pila = ""
			break
		# if str(posicion_grafo).isalpha():
		# 	posicion_grafo = 1
		# 	pila=""
		# 	break
		if posicion_grafo == "error":
			print("error err")
			break
	if buffer=="":
		break
file.close()

