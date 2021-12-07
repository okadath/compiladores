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
	# graph[(1, "")] ="IDd"


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

	graph[(9, "d")] = "sum"
	graph[(9, ".")] = "sum"
	graph[(9, "l")] = "sum"
	graph[(9, "+")] = 16
	graph[(9, "-")] = "sum"
	graph[(9, "*")] = "sum"
	graph[(9, "/")] = "sum"
	graph[(9, "(")] = "sum"
	graph[(9, ")")] = "sum"


	graph[(4, "d")] = "NINT"
	graph[(6, "d")] = "NREAL"
	graph[(8, "l")] = "ID"
	# graph[(9, "+")] = "SUM"
	graph[(10, "-")] = "RES"
	graph[(11, "*")] = "MUL"
	graph[(12, "/")] = "DIV"
	graph[(13, "(")] = "PARI"
	graph[(14, ")")] = "PARD"
	graph[(16, "+")] = "SUM"
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
		if buffer=="." and cadena[-1].isdigit():
			print("error INT.CHAR "+ cadena+char)
			break
		if buffer=="d":
			otro=True
		buffer = "l"
	elif char.isdigit():
		buffer = "d"
		# otro = True
	else:
		
		if apilando_letra:
			apilando_letra=False
			otro=True
			if char==".":
				buffer="."
			# if char=="+":
			# 	buffer=""
		else:
			buffer = char

	doble=False
	while True:
		# print(lista_identificadores)
		# print(lista_tokens)
	
			
		if buffer == ".":
			cadena = cadena + char
			posicion_grafo = 1
			otro=False
			break
		if otro:
			# print(cadena.count("."))
			# if cadena.isdigit():
			try:
				if cadena[0] == ".":
					print("error inicia con . ")
					raise Exception
					break
			except Exception as e:
				pass
			if cadena[-1:].isdigit() :
				if cadena[0].isalpha():
					print("error, id con . "+ cadena)
					raise Exception
					break
				if cadena[0]==".":
					print("error, numero con con . "+ cadena)
					raise Exception
					break
				if cadena.count(".")>1:
					print("error, palabraa con . ")
					raise Exception
					break
				lista_tokens.append(cadena)
				print(cadena[-1:])
				lista_identificadores.append("NUMM" + str(insertados))
			else:
				if "while"==cadena:
					lista_tokens.append(cadena)
					lista_identificadores.append("while" + str(insertados))
				elif "when" == cadena:
					lista_tokens.append(cadena)
					lista_identificadores.append("when" + str(insertados))
				elif cadena.count(".")>0:
					print("error, palabra con . ")
					raise Exception
					break
					# lista_tokens.append(cadena)
					# lista_identificadores.append("when" + str(insertados))
				
				else:
					lista_tokens.append(cadena)
					lista_identificadores.append("ID" + str(insertados))
			apilando_letra=False
			insertados = insertados + 1
			break
		try:
			if str(posicion_grafo).isdigit():
				print(char)
				if buffer=="+":
					cadena = cadena + char
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
			# print("error is digit")
			# print("error"+str(char))
			# raise e
			break
		if str(posicion_grafo).isalpha():
			# insertados = insertados + 1
			try:
				if cadena[-1]==".":
						print("error,  incorrecto "+ cadena)
						raise Exception
						break
			except:
				pass
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
try:
	for i in range(0,len(lista_tokens)-1):
		# print(lista_tokens[i])
		if lista_tokens[i]=="+" and lista_tokens[i+1]=="+":
			# print(lista_identificadores[i])
			lista_tokens[i]="++"
			del lista_tokens[i+1]
			lista_identificadores[i] = "inc"+lista_identificadores[i][3:]
			del lista_identificadores[i+1]

except:
	print("terminado")

print(lista_tokens)
print(lista_identificadores)
