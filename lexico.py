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

	graph[(8,"d")]= "ID"
	graph[(8,"l")]= "ID"
	graph[(8,"+")]= "ID"
	graph[(8,"-")]= "ID"
	graph[(8,"*")]= "ID"
	graph[(8,"/")]= "ID"
	graph[(8,"(")]= "ID"
	graph[(8,")")]= "ID"

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
num=""
apilando_letra=False
while 1:

	# read by character

	if retroceso:
		file.seek(a-2)
		retroceso=False
	char = file.read(1)
	a=file.tell()
	print(file.tell())
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
	if apilando_letra==False:
		posicion_grafo=1
		cadena=""

	while True:

##		if buffer=="":
##			lista_tokens.append(buffer)
##			lista_identificadores.append(posicion_grafo+str(insertados))
##			break
		try:
			if str(posicion_grafo).isdigit():
				if buffer=="l":
					cadena=cadena+char
					apilando_letra=True

				if buffer=="\n" or buffer==" ":
					apilando_letra=False
					break
				posicion_grafo=tabla[(posicion_grafo,buffer)]

		except Exception as e:
			raise e
			print("transicion no aceptada o caracter no valido: "+str(buffer))
			break
		if str(posicion_grafo).isalpha():
			if apilando_letra:
				lista_tokens.append(cadena)
				apilando_letra=False
				retroceso=True
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
		if apilando_letra:
			break



file.close()


