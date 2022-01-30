def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def crea_tabla_tansiciones():
	graph = {}
	graph[(1, "d")] = 2
	graph[(1, ".")] = 15
	graph[(1, "+")] = 9
	graph[(1, "-")] = 17
	graph[(1, "*")] = 11
	graph[(1, "/")] = 12
	graph[(1, "l")] = 7
	graph[(1, "(")] = 13
	graph[(1, ")")] = 14
	graph[(1, "=")] = 20
	graph[(1, ";")] = 21
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
	graph[(2, "=")] = 20
	graph[(2, ";")] = 21

	graph[(3, "d")] = "NUM"
	graph[(3, ".")] = "NUM"
	graph[(3, "l")] = "NUM"
	graph[(3, "+")] = "NUM"
	graph[(3, "-")] = "NUM"
	graph[(3, "*")] = "NUM"
	graph[(3, "/")] = "NUM"
	graph[(3, "(")] = "NUM"
	graph[(3, ")")] = "NUM"
	graph[(3, "=")] = "NUM"
	graph[(3, ";")] = "NUM"


	graph[(4, "d")] = 5
	graph[(4, ".")] = 15
	graph[(4, "+")] = 15
	graph[(4, "-")] = 15
	graph[(4, "*")] = 15
	graph[(4, "/")] = 15
	graph[(4, "l")] = 15
	graph[(4, "(")] = 15
	graph[(4, ")")] = 15
	graph[(4, "=")] = 20
	graph[(4, ";")] = 21



	graph[(5, "d")] = 5
	graph[(5, ".")] = 6
	graph[(5, "+")] = 6
	graph[(5, "-")] = 6
	graph[(5, "*")] = 6
	graph[(5, "/")] = 6
	graph[(5, "l")] = 6
	graph[(5, "(")] = 6
	graph[(5, ")")] = 6
	graph[(5, "=")] = 20
	graph[(5, ";")] = 21



	graph[(7, "d")] = 7
	graph[(7, ".")] = 8
	graph[(7, "+")] = 8
	graph[(7, "-")] = 8
	graph[(7, "*")] = 8
	graph[(7, "/")] = 8
	graph[(7, "l")] = 7
	graph[(7, "(")] = 8
	graph[(7, ")")] = 8
	graph[(5, "=")] = 20
	graph[(5, ";")] = 21



	graph[(8, "d")] = "ident"
	graph[(8, ".")] = "ident"
	graph[(8, "l")] = "ident"
	graph[(8, "+")] = "ident"
	graph[(8, "-")] = "ident"
	graph[(8, "*")] = "ident"
	graph[(8, "/")] = "ident"
	graph[(8, "(")] = "ident"
	graph[(8, ")")] = "ident"
	graph[(8, "=")] = "ident"
	graph[(8, ";")] = "ident"

	# graph[(8,"")]="ID"

	graph[(9, "d")] = "opersum"
	graph[(9, ".")] = "opersum"
	graph[(9, "l")] = "opersum"
	graph[(9, "+")] = 16
	graph[(9, "-")] = "opersum"
	graph[(9, "*")] = "opersum"
	graph[(9, "/")] = "opersum"
	graph[(9, "(")] = "opersum"
	graph[(9, ")")] = "opersum"
	graph[(9, "=")] = "opersum"
	graph[(9, ";")] = "opersum"


	graph[(17, "d")] = "opersub"
	graph[(17, ".")] = "opersub"
	graph[(17, "l")] = "opersub"
	graph[(17, "+")] = 18
	graph[(17, "-")] = "opersub"
	graph[(17, "*")] = "opersub"
	graph[(17, "/")] = "opersub"
	graph[(17, "(")] = "opersub"
	graph[(17, ")")] = "opersub"
	graph[(17, "=")] = "opersub"
	graph[(17, ";")] = "opersub"



	graph[(4, "d")] = "NINT"
	graph[(6, "d")] = "NREAL"
	graph[(8, "l")] = "ident"
	# graph[(9, "+")] = "SUM"
	# graph[(10, "-")] = "opersub"
	graph[(11, "*")] = "opermul"
	graph[(12, "/")] = "operdiv"
	graph[(13, "(")] = "PARI"
	graph[(14, ")")] = "PARD"
	graph[(16, "+")] = "opersum"
	graph[(18, "-")] = "opersub"
	graph[(15, "error")] = "error"
	graph[(20, "=")] = "equal"
	graph[(21, ";")] = "puntoycoma"


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
lista_reservadas=["int","when" ,"until","main","MAIN","=","long","double"
	,"float","real","\"","char","unsigned","signed"]

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
	insertedd=0
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
				# print(cadena[-1:])
				lista_identificadores.append("NUM_" + str(insertados))
			else:
				if "while"==cadena:
					lista_tokens.append(cadena)
					lista_identificadores.append("while" + str(insertados))
				for i in lista_reservadas:
					if i == cadena:
						lista_tokens.append(cadena)
						lista_identificadores.append(i+"_" + str(insertados))
						insertedd=1
						break



				if cadena.count(".")>0:
					print("error, palabra con . ")
					raise Exception
					break
					# lista_tokens.append(cadena)
					# lista_identificadores.append("when" + str(insertados))
				elif insertedd==0:
					lista_tokens.append(cadena)
					lista_identificadores.append("ident" + "_" + str(insertados))

			apilando_letra=False
			insertados = insertados + 1
			break
		try:
			if str(posicion_grafo).isdigit():
				# print(char)
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
			lista_identificadores.append(posicion_grafo + "_"+str(insertados))
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
			lista_identificadores[i] = "operinc"+lista_identificadores[i][7:]
			del lista_identificadores[i+1]

except:
	print("terminado")


try:
	for i in range(0,len(lista_tokens)-1):
		# print(lista_tokens[i])
		if lista_tokens[i]=="-" and lista_tokens[i+1]=="-":
			# print(lista_identificadores[i])
			lista_tokens[i]="--"
			del lista_tokens[i+1]
			lista_identificadores[i] = "operdec"+lista_identificadores[i][7:]
			del lista_identificadores[i+1]

except:
	print("terminado")

# for i in range(0, len(lista_tokens)):
	# print(lista_tokens[i]+"   \t <--> \t"+lista_identificadores[i])

lista_tipo_lexemas=[]

for i in range(0, len(lista_tokens)):
	lista_tipo_lexemas.append({"token":lista_identificadores[i],"value":lista_tokens[i],"tipo":"","modif":""})
								  # ,"nodo":{"dato":"","hijo_izq":"","hijo_der":""}})

list_types=["int","char","float","double"]
list_modificadores=["unsigned","signed","long"]
for i in range(0, len(lista_tokens)):
	# cadena=
	for a in list_modificadores:
		if lista_identificadores[i].split("_")[0]==a:
			# print(lista_identificadores[i]+" es "+ a)

			lista_tipo_lexemas[i+1]["modif"]=a
			lista_tipo_lexemas[i + 2]["modif"] = a
	for a in list_types:
		if lista_identificadores[i].split("_")[0]==a:
			# print(lista_identificadores[i]+" es "+ a)
			# lista_tipo_lexemas[i]["tipo"]=lista_tipo_lexemas[i]["value"]

			lista_tipo_lexemas[i+1]["tipo"]=a
	if lista_tipo_lexemas[i]["value"].isdigit():
		print(lista_tipo_lexemas[i]["value"] + " es int")
		lista_tipo_lexemas[i]["tipo"] = "int"
	elif is_integer(lista_tipo_lexemas[i]["value"]):
		print(lista_tipo_lexemas[i]["value"] + " es real")
		lista_tipo_lexemas[i]["tipo"] = "real"
	elif lista_tipo_lexemas[i]["value"][0].isdigit()	:
		print(lista_tipo_lexemas[i]["value"] + " es real")
		lista_tipo_lexemas[i]["tipo"] = "real"

# for a in lista_tipo_lexemas:
# 	print(a)
lista=[]
i=0
inicioo=0
while i< (len(lista_tokens)):
# for i in range(1, len(lista_tokens)):
	lista=[]
	if lista_tipo_lexemas[i]["token"].split("_")[0]=="equal":
		inicioo=i
		for j in range(i-1, len(lista_tokens)):
			if lista_tipo_lexemas[j]["token"].split("_")[0]=="puntoycoma":
				i=j
				break
			lista.append(lista_tipo_lexemas[j])
	i=i+1

	for j in lista:
		if j["tipo"]=="float":
			lista_tipo_lexemas[inicioo-1]["tipo"]="float"
		if j["tipo"]=="real":
			lista_tipo_lexemas[inicioo-1]["tipo"]="real"
		if j["tipo"]=="char":
			lista_tipo_lexemas[inicioo-1]["tipo"]="char"
		# elif j["tipo"]!="":
		# 	lista_tipo_lexemas[inicioo-1]["tipo"]="int"

	# print(i)
	# for a in lista:
	# 	print(a)


# aqui se imprime la tarea 4
for a in lista_tipo_lexemas:
	print(a)

# El lenguaje C no define tamaños fijos para sus tipos de datos básicos.
# Lo único que garantiza es que un short int tiene un tamaño menor o igual que un int
# y este a su vez un tamaño menor o igual a un long int.
# Esta característica del lenguaje ha complicado la creación de progra
# mas que sean compatibles entre varias plataformas.




punteros_a_valores=[]
registros=[]

i=0


def IsArithmeticOP(cadena)-> bool:
	return (cadena=="+" or cadena=="-" or cadena=="*" or cadena=="/")

def generatearithmeticOP(cadena, reg1,reg2):
	op=""
	if cadena=="+":
		op="ADD"
	elif cadena=="-":
		op="SUB"
	elif cadena=="*":
		op="MUL"
	elif cadena=="/":
		op="DIV"
	print(op+" R"+str(reg1)+", R"+str(reg2)+";")


def generateload(cadena,registro):
	print("LOAD "+cadena+" R"+str(registro)+";")

def get_node(array,label):
	for i in array:


		if i["val"]==label:
			# print("i es")
			# print(i)
			return i

def generate_code(array,arbol, regnum):
	try:
		# print("arbol es")
		# print(arbol)
		if (IsArithmeticOP(arbol["nodo"]["label"])):
			# print(arbol["nodo"]["label"])
			generate_code(array,get_node(array,arbol["nodo"]["der"]),regnum)
			generate_code(array,get_node(array,arbol["nodo"]["izq"]),regnum+1)
			generatearithmeticOP(arbol["nodo"]["label"],regnum,regnum+1)

		else:
			generateload(arbol["nodo"]["label"],regnum )
	except Exception as e:
		print(inicio)
		raise(e)
		generateload(arbol["nodo"]["label"], regnum)


while i< (len(lista_tokens)):
# for i in range(1, len(lista_tokens)):
	arbol=[]
	if lista_identificadores[i-1].split("_")[0] == "ident":
		# punteros_a_valores.append({"id":lista_tipo_lexemas[i-1]["token"],"arbol":"","valor":""})
		inicioo=i
		for j in range(i+1, len(lista_tokens)):
			if lista_tipo_lexemas[j]["token"].split("_")[0]=="puntoycoma":
				# aqui insertamos el padre del arbol, pero con while, for, y demas el arbol se construye apuntando a un valor distinto
				# punteros_a_valores[-1]["arbol"] = lista_tipo_lexemas[j-2]["token"]
				# punteros_a_valores[-1]["arbol"] = lista_tipo_lexemas[inicioo+2]["token"]
				i=j
				break
			arbol.append({"val":lista_tipo_lexemas[j]["token"],"nodo":{"label":lista_tipo_lexemas[j]["value"],"izq":"","der":""}})
	# arbol[inicioo]["arbol"]=lista_tipo_lexemas[inicioo]["token"]

	if len(arbol)>1:

		for j in range(1, len(arbol)-1):
			# print(arbol[j]["val"].split(("_"))[0][:4])
			if arbol[j]["val"].split(("_"))[0][:4]=="oper":
				arbol[j]["nodo"]["izq"] = arbol[j - 2]["val"]
				arbol[j]["nodo"]["der"] = arbol[j + 1]["val"]
		arbol[1]["nodo"]["izq"] = arbol[0]["val"]

	# else:
				# arbol[j]["nodo"]["izq"]=arbol[j-1]["val"]
				# arbol[j]["nodo"]["der"]=arbol[j+1]["val"]





	# if (len(arbol)!=0):
	# 	# print(arbol)
	# 	print("=============================")
	# 	print("el arbol es:")
	# 	for aa in arbol:
	# 		print(aa)
	# 	if (len(arbol) > 1):
	# 		#donde esta el nodo inicial en la representacion de lista
	# 		ll=get_node(arbol,arbol[-2]["val"])
	# 	else:
	# 		ll=get_node(arbol,arbol[0]["val"])

	# 	generate_code(arbol,ll,10)
	i=i+1







