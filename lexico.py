def crea_tabla_tansiciones():
	graph = {}
	graph[(1, "d")] = 2
	graph[(1, ".")] = 15
	graph[(1, "+")] = 9
	graph[(1, "-")] = 10
	graph[(1, "*")] = 11
	graph[(1, "/")] = 12
	graph[(1, "l")] = 7
	graph[(1, "(")] = 13
	graph[(1, ")")] = 14


	graph[(2, "d")] = 2
	graph[(2, ".")] = 4
	graph[(2, "+")] = 3
	graph[(2, "-")] = 3
	graph[(2, "*")] = 3
	graph[(2, "/")] = 3
	graph[(2, "l")] = 3
	graph[(2, "(")] = 3
	graph[(2, ")")] = 3

	graph[(3, "d")] = "NUM"
	graph[(3, ".")] = "NUM"
	graph[(3, "l")] = "NUM"
	graph[(3, "+")] = "NUM"
	graph[(3, "-")] = "NUM"
	graph[(3, "*")] = "NUM"
	graph[(3, "/")] = "NUM"
	graph[(3, "(")] = "NUM"
	graph[(3, ")")] = "NUM"
	
	graph[(4, "d")] = 5
	graph[(4, ".")] = 15
	graph[(4, "+")] = 15
	graph[(4, "-")] = 15
	graph[(4, "*")] = 15
	graph[(4, "/")] = 15
	graph[(4, "l")] = 15
	graph[(4, "(")] = 15
	graph[(4, ")")] = 15
	
	graph[(5, "d")] = 5
	graph[(5, ".")] = 6
	graph[(5, "+")] = 6
	graph[(5, "-")] = 6
	graph[(5, "*")] = 6
	graph[(5, "/")] = 6
	graph[(5, "l")] = 6
	graph[(5, "(")] = 6
	graph[(5, ")")] = 6
	
	graph[(7, "d")] = 7
	graph[(7, ".")] = 8
	graph[(7, "+")] = 8
	graph[(7, "-")] = 8
	graph[(7, "*")] = 8
	graph[(7, "/")] = 8
	graph[(7, "l")] = 7
	graph[(7, "(")] = 8
	graph[(7, ")")] = 8

	graph[(8, "d")] = "ID"
	graph[(8, ".")] = "ID"
	graph[(8, "l")] = "ID"
	graph[(8, "+")] = "ID"
	graph[(8, "-")] = "ID"
	graph[(8, "*")] = "ID"
	graph[(8, "/")] = "ID"
	graph[(8, "(")] = "ID"
	graph[(8, ")")] = "ID"
	# graph[(8,"")]="ID"

	graph[(4, "d")] = "NINT"
	graph[(6, "d")] = "NREAL"
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
otro = False
# num = ""
apilando_letra = False
dejo_de_apilar=False
end=False
buffer=""
singleton=False
while 1:

	if otro and char !="":
		file.seek(a - 1)
		otro = False
	char = file.read(1)

	a = file.tell()
	if not apilando_letra:
		posicion_grafo = 1
		if buffer!=".":
			cadena = ""
		if end:
			break
		if not char :
			end=True

	if char.isalpha():
		if buffer=="." and cadena[-2].isdigit():
			print("error INT.CHAR "+ cadena+char)
			break
		if buffer=="d":
			otro=True
		buffer = "l"
	elif char.isdigit():
		# if buffer=="." and cadena[-2].isalpha():
		# 	print("error INT.CHAR")
		# 	break
		# if buffer=="l":
		# 	otro=True
		buffer = "d"
	else:
		
		if apilando_letra:
			apilando_letra=False
			otro=True
			if char==".":
				buffer="."
		else:
			buffer = char

	while True:
		print(lista_identificadores)
		print(lista_tokens)

		if buffer == ".":
			cadena = cadena + char
			posicion_grafo = 1
			otro=False
			break
		if otro:
			print(cadena.count("."))
			lista_tokens.append(cadena)
			# if cadena.isdigit():
			if cadena[-1:].isdigit() :
				if cadena.count(".")>1:
					break
				lista_identificadores.append("NUM" + str(insertados))
			else:
				lista_identificadores.append("ID" + str(insertados))
			apilando_letra=False
			insertados = insertados + 1
			break
		try:
			if str(posicion_grafo).isdigit():
				if buffer == "l" or buffer=="d":
					# if cadena[-1:]==""
					cadena = cadena + char
					apilando_letra = True
				elif buffer == ".":
					cadena = cadena + char
					posicion_grafo = 1
				elif  char=="\n" or char==" ":
					break
				# 	apilando_letra = True
				posicion_grafo = tabla[(posicion_grafo, buffer)]

		except Exception as e:
			print("error is digit")
			raise e
			break
		if str(posicion_grafo).isalpha():
			# insertados = insertados + 1
			if apilando_letra:
				lista_tokens.append(cadena)
				apilando_letra = False
				otro = True
			else:
				lista_tokens.append(buffer)
			lista_identificadores.append(posicion_grafo + str(insertados))
			insertados = insertados + 1
			posicion_grafo = 1
			break
		if posicion_grafo == "error":
			print("error err")
			break
		if apilando_letra:
			break

		

file.close()

