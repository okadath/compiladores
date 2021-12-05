def crea_tabla_tansiciones():
	graph = {}  



	graph[(1,"+")]=9
	graph[(1,"-")]=10
	graph[(1,"*")]=11
	graph[(1,"/")]=12
	graph[(1,"(")]=13
	graph[(1,")")]=14
	graph[(1,"l")]=7


	graph[(7,"d")]=7
	graph[(7,"l")]=7
	graph[(7,"+")]=8
	graph[(7,"-")]=8
	graph[(7,"*")]=8
	graph[(7,"/")]=8
	graph[(7,"(")]=8
	graph[(7,")")]=8

	graph[(8,"l")]= "ID"
	graph[(9,"+")]= "SUM"
	graph[(10,"-")]= "RES"
	graph[(11,"*")]= "MUL"
	graph[(12,"/")]= "DIV"
	graph[(13,"(")]= "PARI"
	graph[(14,")")]= "PARD"
	graph[(15,"error")]="error"
	# print(graph)
	return graph


tabla=crea_tabla_tansiciones()

# print(tabla[(1, ")")])
file = open('file.txt', 'r')
lista_tokens=[]
lista_identificadores=[]
insertados=1
retroceso=False
while 1:

	# read by character
	char = file.read(1)  
	if retroceso:
		char= file.seek(file.tell()-1)# -1 ??
		retroceso=False
	# file.tell() nos dice la pocision del puntero del archivo
	# si necesitas moverte a una posicion dada usas file.seek()
	# https://docs.python.org/3/tutorial/inputoutput.html#methods-of-file-objects
	# print(file.tell())      
	if not char:
		break

	# if char==("\n"):
	# 	print("\\n")
	# 	# pass
	# elif char==(" "):
	# 	print("_")
	# 	# pass
	# else:
	# 	# print("char es"+ char)
	# 	print(char)
	# 	# pass
	print(char)
	print(char.isalpha())

	# for i in rangfe(0,15)
	# id_a_insertar
	if char.isalpha():
		buffer="l"
	elif char.isdigit():
		buffer="d"
	else:
		buffer=char
	posicion_grafo=1
	cadena=""
	num=""
	apilando_letra=False
	while True:
# 
		# if 

		print(cadena)
		print(lista_tokens)
		print(lista_identificadores)
		print(buffer)
		print(posicion_grafo)
		try:
			if str(posicion_grafo).isdigit():
				if buffer=="l":
					cadena=cadena+char
					apilando_letra=True
				posicion_grafo=tabla[(posicion_grafo,buffer)]
		except Exception as e:
			raise e
			print("error")
			print("transicion no aceptada o caracter no valido: "+str(buffer))
			break

		# el problema esta aqui, no llega al siguiente
		# y se queda en un bucle en (7,l)
		# no se si por que el siguiente valor lo lee como alpha
		# por que noa ctualizo el buffer
		# por que el siguiente no hago aun el retroceso
		# mañana tengo que debuggear esto
		# ahorita creo que no es culpa del retroceso
		# se queda en el loop (7,"l")=7
		if str(posicion_grafo).isalpha():
			if apilando_letra:
				lista_tokens.append(cadena)
				apilando_letra=False
				# lista_identificadores.append(posicion_grafo+str(insertados))	
			else: 
				lista_tokens.append(buffer)

			lista_identificadores.append(posicion_grafo+str(insertados))
			print(lista_tokens)
			print(lista_identificadores)
			insertados=insertados+1
			posicion_grafo=1
			break
		if posicion_grafo=="error":
			print("error")
			break



file.close()


