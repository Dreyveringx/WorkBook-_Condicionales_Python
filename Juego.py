
import os

def centrar_textos(textos):
  
    ancho_terminal = os.get_terminal_size().columns

    textos_centrados = []
    for texto in textos:
       
        espacio_en_blanco = (ancho_terminal - len(texto)) // 2

        texto_centrado = " " * espacio_en_blanco + texto + " " * espacio_en_blanco

        textos_centrados.append(texto_centrado)

    return textos_centrados

num_partidas= 5

for _ in range(num_partidas):
    textos = ["¡𝔹𝕀𝔼ℕ𝕍𝔼ℕ𝕀𝔻𝕆!🤗", " ◄[🏆]► En Busca del Tesoro ◄[🥇]►"]

    textos_centrados = centrar_textos(textos)

    for texto in textos_centrados:
        print(texto)


    nombre = str(input("\n\nIngresar Nombre: "))

    textos = ["🌟¡QUE COMIENCE EL JUEGO!🌟"]

    textos_centrados = centrar_textos(textos)

    for texto in textos_centrados:
        print(texto)

    textos = ["⚠️ 📜*Única regla*📜 ⚠️", "Recuerda contestar las preguntas en MAYÚSCULA y con la palabra indicada en cada opción que se encuentra escrita también en MAYÚSCULA."]

    textos_centrados = centrar_textos(textos)

    for texto in textos_centrados:
        print(texto)        

    print(" \n\n 🌳Estamos en medio de una densa selva tropical, rodeados de vegetación exuberante y sonidos de animales desconocidos. ☀️El sol se filtra a través de las hojas de los árboles, creando un ambiente misterioso🌲.")

    print(f" \n\n 🤠{nombre}, eres un(a) intrépido explorador que ha estado buscando el legendario 🗿Tesoro de los Antiguos🗿  durante años. La leyenda cuenta que este tesoro está escondido en lo más profundo de esta selva y que otorgará inmensas riquezas y poder a quien lo encuentre. ")

    print(f"\n\n🤠{nombre}, te encuentras en un claro en medio de la selva. Frente a ti, hay un antiguo altar de piedra tallada con inscripciones en un idioma desconocido. Tienes dos opciones: \n\n 🅰️ Investigar el altar \n\n 🅱️ ignorar el altar")

    elección = input("\n\nElija una opción A o B: ")

    if elección == "A":
        camino = (input("\n\nAl estudiar las inscripciones, descubres una serie de símbolos que te guían hacia una bifurcación en el camino. Las inscripciones sugieren que uno de los caminos lleva al tesoro, mientras que el otro es mortal. Tienes dos opciones: \n\n *Tomar el camino de la IZQUIERDA \n\n *Tomar el camino de la DERECHA \n\n ¿Qué camino elijes IZQUIERDA o DERECHA❔: "))
        if camino == "IZQUIERDA":
            (print("\n\n💢Sigues el camino de la izquierda y avanzas con cautela. Después de un tiempo, llegas a una trampa mortal y mueres.❌")) 

            textos = ["\n\n☠️¡PIERDES!☠️"]

            textos_centrados = centrar_textos(textos)

            for texto in textos_centrados:
                print(texto)

            reiniciar = input(f"\n\n🤠{nombre}, Desea \n\nReiniciar el juego ✔️ Responda (SI) \n\nSalir del juego ❌ Responda (NO)❔: ")
            if reiniciar.lower() != "si":
                break


        else:
            decisión = (input("\n\nEl camino de la derecha te lleva a través de la selva densa, pero eventualmente llegas a una enorme puerta de piedra. Esta puerta parece ser la entrada a una antigua ciudad subterránea. Tu búsqueda continúa. \n\n Después de abrir la enorme puerta de piedra, entras en la antigua ciudad subterránea. Las paredes están adornadas con relieves de tesoros y riquezas. Parece que estás en el lugar correcto. \n\n  \n\n  Sin embargo, te enfrentas a un nuevo dilema:\n\n🧐EXPLORAR el interior de la ciudad subterranea. \n\n 🧐INVESTIGAR una puerta en la esquina que parece conducir a un pasaje oscuro. \n\n ¿Cuál es tu desición EXPLORAR o INVESTIGAR❔: "))
            if decisión == "EXPLORAR":
                (print("\n\n 💢Una trampa antigua se activa, y una lluvia de dardos envenenados te alcanza. Tu búsqueda ha llegado a un final mortal.❌"))

                textos = ["\n\n☠️¡PIERDES!☠️"]

                textos_centrados = centrar_textos(textos)

                for texto in textos_centrados:
                    print(texto)

                reiniciar = input(f"\n\n🤠{nombre}, Desea \n\nReiniciar el juego ✔️ Responda (SI) \n\nSalir del juego ❌ Responda (NO)❔: ")
                if reiniciar.lower() != "si":
                    break

            else:
                (print("\n\nA medida que avanzas por el pasaje, llegas a una enorme cámara subterránea. En el centro de la cámara, brilla el Tesoro de los Antiguos.\n\n"))
            
                textos = ["`•.,¸¸,.•´¯   🏆  ¡𝒢𝒜𝒩𝒜𝒮𝒯𝐸!  🏆   ¯´•.,¸¸,.•`", "Has tenido éxito en tu búsqueda. El tesoro es tuyo. ¡Felicidades!"]

                textos_centrados = centrar_textos(textos)

                for texto in textos_centrados:
                    print(texto)
                
                reiniciar = input(f"\n\n🤠{nombre}, Desea \n\nReiniciar el juego ✔️ Responda (SI) \n\nSalir del juego ❌ Responda (NO)❔: ")
                if reiniciar.lower() != "si":
                    break

    else:
        eleccion= (input(f"\n\n 🤠{nombre}Decides seguir adelante, ignorando el altar y confiando en tu instinto. Después de caminar un tiempo, llegas a un río. Tienes dos opciones: \n\n🏊‍♂️ NADAR para cruzar el rio2. \n\n 🧐BUSCAR un camino alternativo siguiendo el rio. \n\n Cuál es tu elección❔: "))
        if eleccion == "NADAR":
            (print("💢🏊‍♂️Tratas de cruzar el río a nado, pero las fuertes corrientes te arrastran y mueres❌"))

            textos = ["\n\n☠️¡PIERDES!☠️"]

            textos_centrados = centrar_textos(textos)

            for texto in textos_centrados:
                print(texto)

            reiniciar = input(f"\n\n🤠{nombre}, Desea \n\nReiniciar el juego ✔️ Responda (SI) \n\nSalir del juego ❌ Responda (NO)❔: ")
            if reiniciar.lower() != "si":
                break
        else:
            (print("\n\n 🏞️Sigues el río y encuentras un puente colgante que te permite cruzar de manera segura.🌉\n\n "))
            textos = ["\n\n☠️¡PIERDES!☠️", "\n\n 💢Al otro lado eres sorprendido por una enorme pantera quien se abalanza contra ti y eres devorado en el acto.❌"]

            textos_centrados = centrar_textos(textos)

            for texto in textos_centrados:
                    print(texto)
                    
            reiniciar = input(f"\n\n🤠{nombre}, Desea \n\nReiniciar el juego ✔️ Responda (SI) \n\nSalir del juego ❌ Responda (NO)❔: ")
            if reiniciar.lower() != "si":
                break
            