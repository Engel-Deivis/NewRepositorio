print("Buenos dias. Bienvenidos a nuestra feria de empleo acontinuacion le presentaremos las vacantes disponibles. \n1 - Mesero \n2 - Cocinero \n3 - Chofer \n4 - Seguridad \n5 - Adminstrador \n6 - Contable. \nLos requisitos minimos para todas las vacantes: \n1 - Mayor o igual de 18 años \n2 - Ser bachiller o universitario \n Gracias pase feliz resto del dia espero que pueda encontrar su empleo deseado en nuestra feria bendiciones.")

nombre = input("Digite su nombre: ")
apellido = input("Digite su apellido: ")
direccion = input("Digite su direccion: ")
correo = input("Digite su correo electronico: ")
educacion = input("Digite su nivel academico: ")
vacante = input("Digite su vacante deseada: ")

if educacion == "Bachiller" or educacion == "Universitario":
    edad = int(input)(f"{nombre} {apellido} su direccion es {direccion} correo electronico {correo} y su nivel academico es {educacion} su vacante deseada es {vacante} Felicidades cumple con todos los requisitos para la vacante {vacante} \nFavor digitar su edad: ")
    if edad >= 18:
        print("Usted cumple con la edad requerida.")
   