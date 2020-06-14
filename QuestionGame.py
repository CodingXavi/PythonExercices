print("Q U E S T I O N - G A M E - B Y XaviMoya")
input()
print("Bienvendio a QuestionGame by iv4x. Se trata de un juego en el que se te irán haciendo preguntas y conforme aciertes o falles, pasará una cosa u otra.")
print("El objetivo es llegar al cráter final, para ello tendrás que pasar por distintas pruebas.")
print("Tienes 3 vidas")
print("Si deseas cerrar el juego, escribe salir.")
print("TODA RESPUESTA DEBE IR EN MINÚSCULAS")

vidas = 3

while True:

	print("Presione enter para empezar")
	input()

	if vidas != 0:

		pregunta1 = input(" ¿De qué color tiene el pelo Naruto?\n\r ")
		if pregunta1 == "rubio":
			print("CORRECTO")
			print("Avanzas de nivel")
			print("Presione enter para continuar con el siguiente nivel")
			input()	

			print("Nivel 2. Catacumbas de Largon")
			pregunta1_1 = int(input(" ¿ Cuántas colas tiene Ahri del LoL ?\n\r "))			
			if pregunta1_1 == 9:
				print("CORRECTO")
				print("Avanzas de nivel")
				print("Presione enter para continuar con el siguiente nivel")
				input()
				
				print("Nivel 3. Puente hacia el cráter")
				pregunta1_3 = input("¿ Cuál es la principal diferencia entre un animal y un humano ?\n\r ")				
				if pregunta1_3 == "razonamiento":					
					print("CORRECTO")
					print("Avanzas de nivel")
					print("Presione enter para continuar con el siguiente nivel")
					input()

					print("Nivel 4. El cráter final")
					pregunta1_4 = input("¿ Nombre del tipo de escritura que recuerda a pakistan en programación ?\n\r")
					
					if pregunta1_4 == "kebabcase":						
						print("!!!!!!!!!!!!!!! GANASTE EL JUEGO. ERES UN TITÁN, MONSTRUO, MASTODONTE, CAPBRUT ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡")
						print("Gracias por jugar a QuestionGame")
						break
					else:
						print("Te has quedado a las puertas del final, una pena")
						vidas -=1
						print("Vidas: ", vidas)
						continue

				else:
					print("Fallaste")
					vidas -=1
					print("Vidas: ", vidas)		
					continue

			else:
				print("Fallaste")
				vidas -=1
				print("Vidas: ", vidas)
				continue
		
		else:
			print("Fallaste")
			vidas -=1
			print("Vidas: ", vidas)
			continue

	elif vidas == 0:
		print("Te has quedado sin vidas")
		print("JUEGO TERMINADO")
		break
