from os import system
system ("cls")

username=73528
c5=username % 10
c4=int((username % 100)/10)
c3=int((username % 1000)/100)
c2=int((username % 10000)/1000)
c1=int((username % 100000)/10000)
password=int(str(c5)+str(c4)+str(c3)+str(c2)+str(c1))
newpassword=82537

print("Bienvenido al sistema de ubicación para zonas publicas wifi")

opciónes_favoritas = ["Cambiar contraseña",
                      "Ingresar coordenadas actuales",
                      "Ubicar zona wifi más cercana",
                      "Guardar archivo con ubicación cercana",
                      "Actualizar registros de zonas wifi desde archivo",
                      "Elegir opción de menú favorita",
                      "Cerrar sesión"]

opciónes_sinmun = ["Cambiar contraseña",
                      "Ingresar coordenadas actuales",
                      "Ubicar zona wifi más cercana",
                      "Guardar archivo con ubicación cercana",
                      "Actualizar registros de zonas wifi desde archivo",
                      "Elegir opción de menú favorita",
                      "Cerrar sesión"]

def menu_principal():

    print("MENÚ PRINCIPAL")

    print("1)", opciónes_favoritas[0])
    print("2)", opciónes_favoritas[1])
    print("3)", opciónes_favoritas[2])
    print("4)", opciónes_favoritas[3])
    print("5)", opciónes_favoritas[4])
    print("6)", opciónes_favoritas[5])
    print("7)", opciónes_favoritas[6])

def menu_sinmun():

    print("MENÚ PRINCIPAL")

    print("1)", opciónes_sinmun[0])
    print("2)", opciónes_sinmun[1])
    print("3)", opciónes_sinmun[2])
    print("4)", opciónes_sinmun[3])
    print("5)", opciónes_sinmun[4])
    print("6)", opciónes_sinmun[5])
    print("7)", opciónes_sinmun[6])

def iniseci():
    enter=int(input("Introduzca el nombre de usuario: "))

    if enter==username:

        entpass=int(input("Introduzca la contraseña: "))

        if entpass==password:

            capt=int(str(c3)+str(c4)+str(c5))
            sum=int(((c1 - c3) * (c5 + c2)) / (c5 + c2))
            captcha=capt + sum

            print(capt,"+",sum)
            capres=int(input("introduzca el valor de la suma:"))

            if capres==captcha:

                system ("cls")
                print("Sesión iniciada")
                print("")
                input("presione 'ENTER'")
                system("cls")

                def eleg_op():
                    while True:
                        system("cls")
                        menu_principal()

                        opció=(input("Elija una opción: "))
                        cambiocord=0
                        
                        if opció=="1":
                            system("cls")
                            newpassword=82537
                            cpass=int(input("antes de continar ingrese su contraseña actual--->"))
                            try:
                                if cpass == newpassword:
                                    print("contraseña correcta")
                                    newc=int(input("ingrese la nueva contraseña--->"))
                                    if newc == newpassword:
                                        print("la contraseña no puede ser igual a la anterios")
                                        input("Presione Enter")
                                    else:
                                        print("nueva contraseña guardada correctamente")
                                        newpassword=newc
                                        input("Presione Enter")
                                else:
                                    print("ERROR")
                                    input("Presione Enter")
                            except:
                                print("carácter invalido")
                                input("Presione Enter")

                        elif opció=="2":
                            system("cls")
                            while True:
                                try:
                                    latitud0 = []
                                    longitud0 = []
                                    coordenadas = []

                                    print("Ingresa las coordenadas del lugar 1")
                                    latitud = int(input("Latitud: "))
                                    longitud = int(input("Longitud: "))
                                        
                                    print("Ingresa las coordenadas del lugar 2")
                                    latitud2 = int(input("Latitud: "))
                                    longitud2 = int(input("Longitud: "))
                                        
                                    print("Ingresa las coordenadas del lugar 2")
                                    latitud3 = int(input("Latitud: "))
                                    longitud3 = int(input("Longitud: "))
                                    
                                    lat_sup = -100000000000000
                                    lat_inf = -100000000000000
                                    lon_or = -100000000000000
                                    lon_occ = -100000000000000
                                        
                                    if longitud > lon_or:
                                            if longitud > lon_occ:
                                                if latitud > lat_sup:
                                                    if latitud > lat_inf:
                                                        ubic = (latitud,longitud)
                                                        coordenadas.append(ubic)
                                                    else:
                                                        print("ERROR11")
                                                        latitud0.clear
                                                        longitud0.clear
                                                        break
                                                else:
                                                    print("ERROR12") 
                                                    latitud0.clear
                                                    longitud0.clear   
                                                    break      
                                            else:
                                                print("ERROR13")
                                                latitud0.clear
                                                longitud0.clear
                                                break
                                    else:
                                        print("ERROR14")  
                                        latitud0.clear
                                        longitud0.clear     
                                        break 
                                    

                                    if longitud2 > lon_or:
                                            if longitud2 > lon_occ:
                                                if latitud2 > lat_sup:
                                                    if latitud2 > lat_inf:
                                                        ubic = (latitud2,longitud2)
                                                        coordenadas.append(ubic)
                                                    else:
                                                        print("ERROR21")
                                                        latitud0.clear
                                                        longitud0.clear
                                                        break
                                                else:
                                                    print("ERROR22")   
                                                    latitud0.clear
                                                    longitud0.clear 
                                                    break      
                                            else:
                                                print("ERROR23")
                                                latitud0.clear
                                                longitud0.clear
                                                break
                                    else:
                                        print("ERROR24")
                                        latitud0.clear
                                        longitud0.clear       
                                        break     

                                    if longitud3 > lon_or:
                                            if longitud3 > lon_occ:
                                                if latitud3 > lat_sup:
                                                    if latitud3 > lat_inf:
                                                        ubic = (latitud3,longitud3)
                                                        coordenadas.append(ubic)
                                                        print("Las coordenadas ingresadas son:")
                                                        lug=0
                                                        for lat in coordenadas:
                                                            lug = lug + 1
                                                            print(f"Lugar{lug}: Lat y  Long -  {lat}")
                                                        input("Presione Enter")
                                                        cambiocord=cambiocord+1
                                                        break
                                                    else:
                                                        print("ERROR31")
                                                        latitud0.clear
                                                        longitud0.clear
                                                        break
                                                else:
                                                    print("ERROR32")    
                                                    latitud0.clear
                                                    longitud0.clear
                                                    break      
                                            else:
                                                print("ERROR33")
                                                latitud0.clear
                                                longitud0.clear
                                                break
                                    else:
                                        print("ERROR34")
                                        latitud0.clear
                                        longitud0.clear       
                                        break
                                except ValueError:
                                    input("Error, Presione Enter: ")

                                    if cambiocord == "1":
                                        print("estas son las coordenadas que tiene actualmente")
                                        print("1 es la que esta ubicada mas al norte")
                                        print("2 es la que esta ubicada mas al occidente")
                                        for i in range(3):
                                            print("Lugar ", i+1, ": (", coordenadas[i][0], ", ", coordenadas[i][1], ")")
                                        cambiocoord=input("selccione la cooordenada que desea editar (1)-(2)-(3) o (0) para regresar al menu-->")
                                        if cambiocoord == "1":
                                            print("ingrese la nueva cordenada")
                                            la=float(input("longitud--->"))
                                            lo=float(input("latitud--->"))
                                            new=[la,lo]
                                            coordenadas.pop(0)
                                            coordenadas.insert(0,new)
                                            print(coordenadas)
                                        elif cambiocoord == "2":
                                            print("ingrese la nueva cordenada")
                                            la=float(input("longitud--->"))
                                            lo=float(input("latitud--->"))
                                            new=[la,lo]
                                            coordenadas.pop(1)
                                            coordenadas.insert(1,new)
                                            print(coordenadas)
                                        elif cambiocoord == "3":
                                            print("ingrese la nueva cordenada")
                                            la=float(input("longitud--->"))
                                            lo=float(input("latitud--->"))
                                            new=[la,lo]
                                            coordenadas.pop(2)
                                            coordenadas.insert(2,new)
                                            print(coordenadas)
                                        elif cambiocoord == "0":
                                            print("seras rediriguido al menu")
                            
                        elif opció=="3":
                            system("cls")
                            print("eligió la opción 3")
                            inten=4
                        elif opció=="4":
                            system("cls")
                            print("eligió la opción 4")
                            inten=4
                        elif opció=="5":
                            system("cls")
                            print("eligió la opción 5")
                            inten=4
                        elif opció=="6":
                            system("cls")
                            menu_principal()

                            favo=(input("elija su opción favorita: "))

                            system("cls")

                            print("resuelva ala adivinanza")
                            print("")              
                            print("soy mas de uno sin llegar a tres\ny cuatro cunado dos me des :)")
                            print("")               
                            adiv1=int(input("digite su respuesta: "))

                            if adiv1==2:
                                system("cls")
                                adiv2=int(input("bien, felicidades\nvamos por la ultima :)\n\nque es ponocho, con dos lados redondos, parece un infinito de lado\ny rima con un mocho :O\n\ndigite su respuesta: "))
                                if adiv2==8:
                                    system("cls")
                                    print("perfecto")
                                    print("")
                                    enter=input("presione 'Enter'")

                                    if favo == "1":  
                                        system("cls") 

                                        opciónes_favoritas.insert(0,opciónes_favoritas[0])
                                        opciónes_favoritas.pop(1)
                                        menu_principal()
                                    elif favo == "2":
                                        system("cls")
                                        
                                        opciónes_favoritas.insert(0,opciónes_favoritas[1])
                                        opciónes_favoritas.pop(2)
                                        menu_principal()
                                    elif favo == "3":
                                        system("cls")
                                        
                                        opciónes_favoritas.insert(0,opciónes_favoritas[2])
                                        opciónes_favoritas.pop(3)
                                        menu_principal()
                                    elif favo == "4":
                                        system("cls")
                                        
                                        opciónes_favoritas.insert(0,opciónes_favoritas[3])
                                        opciónes_favoritas.pop(4)
                                        menu_principal()
                                    elif favo == "5":
                                        system("cls")
                                        
                                        opciónes_favoritas.insert(0,opciónes_favoritas[4])
                                        opciónes_favoritas.pop(5)
                                        menu_principal()
                                    elif favo == "6":
                                        system("cls")
                                        print("error, el '6' siempre estará en el opción N°6")
                                        print("")
                                        enter=input("presione 'Enter'")
                                        system("cls")
                                        menu_sinmun()
                                        inten=inten+1
                                    elif favo == "7":
                                        system("cls")
                                        print("error el '7' siempre estará en el opción N°7")
                                        print("")
                                        enter=input("presione 'Enter'")
                                        system("cls")
                                        menu_sinmun()
                                    else:
                                        system("cls")
                                        print("error, no ingreso un valor lógico")
                                        print("")
                                        input("presione 'Enter'")
                                        menu_sinmun()


                                else:
                                    system("cls")
                                    print("error")
                                    print("")
                                    enter=input("presione 'Enter'")
                            else:
                                system("cls")
                                print("error")
                                print("")
                                enter=input("presione 'Enter'")
                                
                        elif opció=="7":

                            system("cls")
                            menu_principal()
                            print("fin de la sección")
                            break
                        else:
                            system("cls")
                            print("error")
                            print("")
                            input("presione 'Enter'")

                eleg_op()

            else:
                system ("cls")
                print("ERROR")
                print("")

        else:
            system ("cls")
            print("ERROR")
            print("")

    else:
        system ("cls")
        print("ERROR")
        print("")

iniseci()