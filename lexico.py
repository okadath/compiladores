def crea_tabla_tansiciones():
	graph = {}

	graph[(1, "+")] = 9
	graph[(1, "-")] = 10
	graph[(1, "*")] = 11
	graph[(1, "/")] = 12
	graph[(1, "(")] = 13
	graph[(1, ")")] = 14
	graph[(1, "l")] = 7
	# graph[(1, "")] = 7

	graph[(7, "d")] = 7
	graph[(7, "l")] = 7
	graph[(7, "+")] = 8
	graph[(7, "-")] = 8
	graph[(7, "*")] = 8
	graph[(7, "/")] = 8
	graph[(7, "(")] = 8
	graph[(7, ")")] = 8

	graph[(8, "d")] = "ID"
	graph[(8, "l")] = "ID"
	graph[(8, "+")] = "ID"
	graph[(8, "-")] = "ID"
	graph[(8, "*")] = "ID"
	graph[(8, "/")] = "ID"
	graph[(8, "(")] = "ID"
	graph[(8, ")")] = "ID"
	graph[(8,"")]="ID"
	
	graph[(8, "l")] = "ID"
	graph[(9, "+")] = "SUM"
	graph[(10, "-")] = "RES"
	graph[(11, "*")] = "MUL"
	graph[(12, "/")] = "DIV"
	graph[(13, "(")] = "PARI"
	graph[(14, ")")] = "PARD"
	graph[(15, "error")] = "error"
	# print(graph)
	return graph


tabla = crea_tabla_tansiciones()

# print(tabla[(1, ")")])
file = open('file.txt', 'r')
lista_tokens = []
lista_identificadores = []
insertados = 1
retroceso = False
num = ""
apilando_letra = False
dejo_de_apilar=False
end=False
while 1:

	if retroceso and char!="":
		file.seek(a - 1)
		retroceso = False
	char = file.read(1)

	a = file.tell()
	if not apilando_letra:
		posicion_grafo = 1
		cadena = ""
		if end:
			break
		if not char :
			end=True

	if char.isalpha():
		buffer = "l"
	elif char.isdigit():
		buffer = "d"
	else:
		if apilando_letra:
			dejo_de_apilar=True
			apilando_letra=False
		else:
			buffer = char
			
	while True:
		print(lista_identificadores)
		print(lista_tokens)
		if dejo_de_apilar:
			# posicion_grafo = tabla[(posicion_grafo, buffer)]
			lista_tokens.append(cadena)
			lista_identificadores.append("ID" + str(insertados))
			apilando_letra=False
			dejo_de_apilar=False
			retroceso=True
			break
		try:
			if str(posicion_grafo).isdigit():
				if buffer == "l":
					cadena = cadena + char
					apilando_letra = True
				if buffer == "":
					break
				posicion_grafo = tabla[(posicion_grafo, buffer)]

		except Exception as e:
			raise e
			break
		if str(posicion_grafo).isalpha():
			if apilando_letra:
				lista_tokens.append(cadena)
				apilando_letra = False
				retroceso = True
			else:
				lista_tokens.append(buffer)
			lista_identificadores.append(posicion_grafo + str(insertados))
			insertados = insertados + 1
			posicion_grafo = 1
			break
		if posicion_grafo == "error":
			print("error")
			break
		if apilando_letra:
			break
		

file.close()

