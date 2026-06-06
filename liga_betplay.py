import os

def mainMenu()->str:
    menus = {
        "encabezado": "----------------------------\n        Liga betplay\n----------------------------",
        "menuPrincipal": "1.Registrar equipo\n2.Registrar planta tecnica\n3.Registrar jugadores\n4.Programar fechas\n5.Registrar estadisticas\n6.Buscar informacion\n0.Salir",
        "buscarInformacion": "1.Listar planta tecnica\n2.Listar jugadores\n3.Visualizar estadisticas\n4.Regresar",
        "menuPlantaTecnica": "1.Registrar director tecnico\n2.Registrar preparador de portero\n3.Registrar preparador fisico\n4.Registrar al medico\n5.Registrar al fisioterapeuta\n6.Salir"
    }
    return menus

def validarEquipo(codeEquipo,globalTeams) -> bool:
    if globalTeams.get(codeEquipo):
        return True
    else:
        return False

def confirmacion() -> bool:
    opciones = ["y".upper,"n".upper]
    while True:
        seleccion = input("Digita (y)yes si quieres registrar otro o (n)no si no quieres: ").upper
        if seleccion in opciones and seleccion == "y".upper:
            return True
        elif seleccion in opciones and seleccion == "n".upper:
            return False
        else:
            print("Escogiste una opcion invalida, vuelve a digitar")
            os.system("pause")


def registerTeam(globalTeams, equipos):
    while True:
        codeEquipo = int(input("Ingresa el codigo del equipo: "))
        if validarEquipo(codeEquipo,globalTeams):
            print("El codigo ya se encuentra registrado, vuelve a digitar")
            os.system("pause")
        else:
            nombreEquipo = input("Ingresa el nombre del equipo: ")
            equipo = {
                "nombre": nombreEquipo,
                "estadisticas": {
                    "partidosJugados": 0,
                    "partidosGanados": 0,
                    "partidosPerdidos": 0,
                    "partidosEmpatados": 0,
                    "golesFavor": 0,
                    "golesEnContra": 0,
                    "totalPuntos": 0
                }
            }
            equipos.update({codeEquipo:equipo})
            globalTeams.update({"equipos":equipos})
            if confirmacion():
                continue
            else:
                break

def registerStaff(globalTeams):
    while True:
        for id, info in globalTeams["equipos"].items():
                print(f"{id}. {info["nombre"]}")
        codeEquipo = int(input("Digite el codigo del equipo: "))
        if validarEquipo(codeEquipo,globalTeams["equipos"]):
            plantaTecnica = globalTeams["equipos"].get(codeEquipo)
            directorTecnico = input("Digite el nombre del director tecnico: ")
            prepFisico = input("Digite el nombre del preparador fisico: ")
            prepArquero = input("Digite el nombre del preparador de arquero: ")            
            medico = input("Digite el nombre del medico: ")
            fisio = input("Digite el nombre del fisio: ")
            planta = {
                "directorTecnico": directorTecnico,
                "prepFisico": prepFisico,
                "prepArquero": prepArquero,
                "medico": medico,
                "fisio": fisio
            }
            plantaTecnica.update({"plantaTecnica":planta})
            break
        else: 
            print("El codigo del equipo no existe, vuelve a intentar")
            os.system("pause")

def registerPlayers(globalTeams, numJugadores):
    jugadores = {}
    while True:
        for id, info in globalTeams["equipos"].items():
                print(f"{id}. {info["nombre"]}")
        codeEquipo = int(input("Digite el codigo del equipo: "))
        if validarEquipo(codeEquipo,globalTeams["equipos"]):
            for jugador in range(numJugadores):
                numPlayer = 0
                players = globalTeams["equipos"].get(codeEquipo)
                print(f"Registro informacion del jugardor {jugador+1}")
                nombre = input("Ingrese el nombre del jugador: ")
                nacionalidad = input("Ingrese la nacionalidad del jugador: ")
                posJuego = input("Ingrese la posicion del jugador: ")
                numDorsal = int(input("Ingrese el numero de dorsal del jugador: "))
                edad = int(input("Ingrese la edad del jugador: "))
                infojugadores = {
                    "nombre": nombre,
                    "nacionalidad": nacionalidad,
                    "posJuego": posJuego,
                    "numDorsal": numDorsal,
                    "edad": edad
                }
                jugadores.update({jugador+1:infojugadores})
                players.update({"jugadores":jugadores})
            return
        else:
            print("El codigo de equipo no existe, vuelve a digitar")
            os.system("pause")

def programFecha(globalTeams,partidos):
    while True:
        fecha = input("Digite la fecha que desea registrar (DD/MM/AAAA): ")
        ctnPartidos = int(input("Digite la cantidad de partidos para esta fecha: "))
        print("Equipos registrados: ")
        idPartido = {}
        numPartidos = {}
        for codigo, info in globalTeams["equipos"].items():
            print(f"{codigo}-{info["nombre"]}")
        
        for partido in range(ctnPartidos):
            while True:
                codeUno = int(input("Digite el codigo del primer equipo: "))
                if validarEquipo(codeUno,globalTeams["equipos"]):
                    obtenerCodeUno = globalTeams["equipos"].get(codeUno)
                    break
                else:
                    print("Codigo de equipo no encontrado, vuelve a digitar")
                    os.system("pause")
            while True:
                codeDos = int(input("Digite el codigo del segundo equipo: "))
                if validarEquipo(codeDos,globalTeams["equipos"]):
                    obtenerCodeDos = globalTeams["equipos"].get(codeDos)
                    break
                else:
                    print("Codigo de equipo no encontrado, vuelve a digitar")
                    os.system("pause")
            
            partidoInfo = {
                codeUno: {
                        "nombre": obtenerCodeUno["nombre"],
                        "marcador": 0
                        },
                codeDos: {
                        "nombre":obtenerCodeDos["nombre"],
                        "marcador": 0
                        }
            }


            idPartido.update({f"p{partido+1}":partidoInfo})
            numPartidos.update({"juegos":idPartido})
            partidos.update({fecha:numPartidos})
            globalTeams.update({"partidos":partidos})
            
        if confirmacion():
            continue
        else:
            return

def validateDate(selectFecha, globalTeams):
    if globalTeams["partidos"].get(selectFecha):
        return True
    else:
        return False

def validateGame(selectPartido, juegos):
    if juegos["juegos"].get(selectPartido):
        return True
    else:
        return False
    
def validateNumTeam (idEquipo, infoPartido):
    if infoPartido.get(idEquipo):
        return True
    else:
        return False

def registerStatistics(globalTeams):
    os.system("cls")
    for fecha, juegos in globalTeams["partidos"].items():
        print(fecha)
        for identificador, infoPartido in juegos["juegos"].items():
            print(identificador)
            for idEquipo, info in infoPartido.items():
                print(f"Nombre: {info["nombre"]}")
                print(f"Marcador: {info["marcador"]}")          
    while True:
        selectFecha = input("Seleccione la fecha: ")
        if validateDate(selectFecha,globalTeams):
            break
        else:
            print("la fecha no esta registrada, vuelve a intentar")
            os.system("pause")
    while True:
        selectPartido = input("Seleccione el partido: ")
        if validateGame(selectPartido, juegos):
            infoPartido = globalTeams["partidos"][selectFecha]["juegos"][selectPartido]
            for idEquipo, info in infoPartido.items():
                print(idEquipo)
                print(f"Nombre: {info["nombre"]}")
                print(f"Marcador: {info["marcador"]}")
                for numPartido in (infoPartido):
                    marcador = int(input(f"Digite el marcador del equipo{numPartido}: "))
                    infoPartido[numPartido]["marcador"] = marcador
                break
            obtenerIds = list(infoPartido.keys())
            idUno = obtenerIds[0]
            idDos = obtenerIds[1]
            marcadorUno = infoPartido[idUno]["marcador"]
            marcadorDos = infoPartido[idDos]["marcador"]
            if marcadorUno > marcadorDos:
                puntosGolesUno = marcadorUno * 5
                puntosGolesDos = marcadorDos * 5
                estadisticasUno = globalTeams["equipos"][idUno]["estadisticas"]
                estadisticasDos = globalTeams["equipos"][idDos]["estadisticas"]
                estadisticasUno["partidosJugados"] += 1
                estadisticasDos["partidosJugados"] += 1
                estadisticasUno["partidosGanados"] += 1
                estadisticasDos["partidosPerdidos"] += 1
                estadisticasUno["golesFavor"] += marcadorUno
                estadisticasDos["golesFavor"] += marcadorDos
                estadisticasUno["golesEnContra"] += marcadorDos
                estadisticasDos["golesEnContra"] += marcadorUno
                estadisticasUno["totalPuntos"] += puntosGolesUno
                estadisticasDos["totalPuntos"] += puntosGolesDos
            elif marcadorUno < marcadorDos:
                puntosGolesUno = marcadorUno * 5
                puntosGolesDos = marcadorDos * 5
                estadisticasUno = globalTeams["equipos"][idUno]["estadisticas"]
                estadisticasDos = globalTeams["equipos"][idDos]["estadisticas"]
                estadisticasUno["partidosJugados"] += 1
                estadisticasDos["partidosJugados"] += 1
                estadisticasDos["partidosGanados"] += 1
                estadisticasUno["partidosPerdidos"] += 1
                estadisticasUno["golesFavor"] += marcadorUno
                estadisticasDos["golesFavor"] += marcadorDos
                estadisticasUno["golesEnContra"] += marcadorDos
                estadisticasDos["golesEnContra"] += marcadorUno
                estadisticasUno["totalPuntos"] += puntosGolesUno
                estadisticasDos["totalPuntos"] += puntosGolesDos
            else:
                puntosGolesUno = marcadorUno * 5
                puntosGolesDos = marcadorDos * 5
                estadisticasUno = globalTeams["equipos"][idUno]["estadisticas"]
                estadisticasDos = globalTeams["equipos"][idDos]["estadisticas"]
                estadisticasUno["partidosJugados"] += 1
                estadisticasDos["partidosJugados"] += 1
                estadisticasUno["partidosEmpatados"] += 1
                estadisticasDos["partidosEmpatados"] += 1
                estadisticasUno["golesFavor"] += marcadorUno
                estadisticasDos["golesFavor"] += marcadorDos
                estadisticasUno["golesEnContra"] += marcadorDos
                estadisticasDos["golesEnContra"] += marcadorUno
                estadisticasUno["totalPuntos"] += puntosGolesUno
                estadisticasDos["totalPuntos"] += puntosGolesDos
            return  
        else:
            print("El partido no esta registrado, vuelve a intentar")
            os.system("pause")


def listInfo(globalTeams,menu):
    print(menu["buscarInformacion"])
    seleccion = int(input("Digite la opcion que desee: "))
    match seleccion:
        case 1:
            for id, info in globalTeams["equipos"].items():
                print(f"{id}. {info["nombre"]}")
            while True:
                seleccion = int(input("Escoge el equipo: "))
                if (validarEquipo(seleccion,globalTeams["equipos"])):
                    obtenerPlanta = globalTeams["equipos"][seleccion]["plantaTecnica"]
                    for cargo, nombre in obtenerPlanta.items():
                        print(f"{nombre} - {cargo}")
                    os.system("pause")
                    break
                else:
                    print("Error el equipo no esta registrado, vuelve a digitar")
                    os.system("pause")                   
        case 2:
            for id, info in globalTeams["equipos"].items():
                print(f"{id}. {info["nombre"]}")
            while True:
                seleccion = int(input("Escoge el equipo: "))
                if (validarEquipo(seleccion,globalTeams["equipos"])):
                    obtenerJugadadores = globalTeams["equipos"][seleccion]["jugadores"]
                    for idJugador, info in obtenerJugadadores.items():
                        for llave, valor in info.items():
                            print(f"{llave}: {valor}")
                    os.system("pause")
                    break
                else:
                    print("Error el equipo no esta registrado, vuelve a digitar")
                    os.system("pause")         
        case 3:
            for id, info in globalTeams["equipos"].items():
                print(f"{id}. {info["nombre"]}")
            while True:
                seleccion = int(input("Escoge el equipo: "))
                if (validarEquipo(seleccion,globalTeams["equipos"])):
                    obtenerEstadisticas = globalTeams["equipos"][seleccion]["estadisticas"]
                    for llave, valor in obtenerEstadisticas.items():
                        print(f"{llave}: {valor}")
                    os.system("pause")
                    break
                else:
                    print("Error el equipo no esta registrado, vuelve a digitar")
                    os.system("pause")      
        case 4:
            return
        case _:
            pass
    


equipos = {}
partidos = {}
globalTeams = {}
menu = mainMenu()
while True:
    os.system("cls")
    print(menu["encabezado"])
    print(menu["menuPrincipal"])
    opcion = int(input("Seleccione la opcion: "))
    match opcion:
        case 1:
            registerTeam(globalTeams, equipos)
        case 2:
            registerStaff(globalTeams)
        case 3:
            numJugadores = int(input("Ingrese la cantidad de jugadores que se va a registrar: "))
            registerPlayers(globalTeams,numJugadores)
        case 4:
            programFecha(globalTeams,partidos)
        case 5:
            registerStatistics(globalTeams)
        case 6:
            os.system("cls")
            listInfo(globalTeams,menu)
            os.system("pause")
        case 0:
            break
        case _:
            print("Opcion invalida, vuelve a digitar")
            os.system("pause")

