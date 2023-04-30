#menu con todos los objetos
#regirtrarse
#subasta 
#time
#eliminar

import os
import time
print("----BIENVENIDO A LA SUBASTA----")
print("(1)-----registrese para empezar")
print("(2)-----salir")
ronda=[]
participes=[]
pers=[]
dicts=dict(zip(ronda,pers))
premio=0
premio2=0
premio3=0
premio4=0
premio5=0
h1=0
h2=0
h3=0
h4=0
h5=0
opcion=input("--->")
while True:
  try:
      if opcion == "1":
          while True:
           pat1=input(("ingrese su nombre---->"))
           if pat1.isnumeric():
             print("caracter invalido")
           else: 
            participes.append(pat1)
            break
           
          while True:
           pat2=input(("ingrese su nombre---->"))
           if pat2.isnumeric():
             print("caracter invalido")
           else:
            participes.append(pat2)
            break

          while True:
           pat3=input(("ingrese su nombre---->"))
           if pat3.isnumeric():
             print("caracter invalido")
           else:
            participes.append(pat3)
            break
           
          while True:
           pat4=input(("ingrese su nombre---->"))
           if pat4.isnumeric():
             print("caracter invalido")
           else:
            participes.append(pat4)
            break
           
          while True:
           pat5=input(("ingrese su nombre---->"))
           if pat5.isnumeric():
             print("caracter invalido")
           else:
            participes.append(pat5)
            break
           
          os.system("cls")
          break
      elif opcion =="2":
          print("bye")
          break
  except:
      print("caracte invalido")


while True:
  print("----MENU DE OBJETOS A SUBASTAR----")
  print("_-------------------------------_")
  print("(1)---anillo de diamate precio inicial $600")
  print("_-------------------------------_")
  print("(2)---pintura antigua precio inicial $300")
  print("_-------------------------------_")
  print("(3)---libro que relata del año 1780 precio inicial $200")
  print("_-------------------------------_")
  print("(4)---nissan RT/45 precio inicial de 580 ")
  print("_-------------------------------_")
  print("(5)--- caja llena de reliquias antiguas precio inicial 700")
  print("_-------------------------------_")
  try:
    ak=input("deseas salir? s / n-->")
    if ak == "n":
      while True:
        try:
          ops=(input("a que subasta deseas entrar-->"))
          if h1 =="2":
            print("ya se acabo esta subasta")
          else:
           if ops == "1":
            objeto="anillo de diamante"
            p="4000"
            h1=h1+1
            break
           
          if h2 =="2":
            print("ya se acabo esta subasta")
          else:
           if ops == "2":
            objeto="la pintura antigua"
            p="3000"
            h2=h2+1
            break
           
          if h3 =="2":
            print("ya se acabo esta subasta")
          else:
           if ops == "3":
            objeto="el libro"
            p="2000"
            h3=h3+1
            break
           
          if h4 =="2":
            print("ya se acabo esta subasta")
          else:
           if ops =="4":
            objeto="nissan RT/45"
            p="5800"
            h4=h4+1
            break
           
          if h5 =="2":
            print("ya se acabo esta subasta")
          else:
           if ops=="5":
            objeto="la caja llena de reliquias"
            p="6000"
            h5=h5+1
            break
        except:
          print("caracter invalido")
        
      incio=time.time()
      while True:
        try:
              while True:
               if premio >= 3:
                print("El participante",pat1," ya ganó el limite de productos")
               elif premio <= 2:
                print(pat1)
                a1=(input("cuanto vas a ofrecer?--->"))
                if a1.isnumeric():
                 print(pat1,"ofrece",a1)
                 if a1>=p:
                   pers.append(a1)
                   ronda.append(pat1)
                   print("el nuevo valor de",objeto," es de",a1)
                   sale=a1
                   break
                 elif a1<=p:
                  print("el nuevo valor de",objeto," continua igual",p)
                  sale=p
                  break
                else:
                 print("caracter invalido")

              while True:
               if premio2 >= 3:
                print("El participante",pat2," ya ganó el limite de productos")
               elif premio2 <= 2:
                print(pat2)
                a2=(input("cuanto vas a ofrecer?--->"))
                if a2.isnumeric():
                  print(pat2,"ofrece",a2)
                  if sale == a1: 
                    if a2 >= a1:
                      pers.append(a2)
                      ronda.append(pat2)
                      print("el nuevo valor de",objeto," es de",a2)
                      saled2=a2
                      break
                    elif a2 <= a1:
                     print("el nuevo valor de",objeto," continua igual",a1)
                     saled2=a1
                     break
                  elif sale == p:
                    if a2 >= p:
                     pers.append(a2)
                     ronda.append(pat2)
                     print("el nuevo valor de",objeto," es de",a2)
                     saled2=a2
                     break
                    elif a2 <= p:
                     print("el nuevo valor de",objeto," continua igual",p)
                     saled2=p
                     break
                else:
                 print("caracter invalido")
                
              while True:
               if premio3 >= 3:
                print("El participante",pat3," ya ganó el limite de productos")
               elif premio3 <= 2:
                print(pat3)
                a3=(input("cuanto vas a ofrecer?--->"))
                if a3.isnumeric():
                  print(pat3,"ofrece",a3)
                  if saled2 == p: 
                    if a3 >= p:
                      pers.append(a3)
                      ronda.append(pat3)
                      print("el nuevo valor de",objeto," es de",a3)
                      saled3=a3
                      break
                    elif a3 <= p:
                     print("el nuevo valor de",objeto," continua igual",p)
                     saled3=p
                     break
                  elif saled2 == a1:
                    if a3 >= a1:
                     pers.append(a3)
                     ronda.append(pat3)
                     print("el nuevo valor de",objeto," es de",a3)
                     saled3=a3
                     break
                    elif a3 <= a1:
                     print("el nuevo valor de",objeto," continua igual",a1)
                     saled3=a1
                  elif saled2 == a2:
                    if a3 >= a2:
                     pers.append(a3)
                     ronda.append(pat3)
                     print("el nuevo valor de",objeto," es de",a3)
                     saled3=a3
                     break
                    elif a3 <= a2:
                     print("el nuevo valor de",objeto," continua igual",a2)
                     saled3=a2    
                     break
                else:
                 print("caracter invalido")

              while True:
               if premio4 >= 3:
                print("El participante",pat3," ya ganó el limite de productos")
               elif premio4 <= 2:
                print(pat3)
                a4=(input("cuanto vas a ofrecer?--->"))
                if a4.isnumeric():
                  print(pat4,"ofrece",a4)
                  if saled3 == p: 
                    if a4 >= p:
                      pers.append(a4)
                      ronda.append(pat4)
                      print("el nuevo valor de",objeto," es de",a4)
                      saled4=a4
                      break
                    elif a4 <= p:
                     print("el nuevo valor de",objeto," continua igual",p)
                     saled4=p
                     break
                  elif saled3 == a1:
                    if a4 >= a1:
                     pers.append(a4)
                     ronda.append(pat4)
                     print("el nuevo valor de",objeto," es de",a4)
                     saled4=a4
                     break
                    elif a4 <= a1:
                     print("el nuevo valor de",objeto," continua igual",a1)
                     saled4=a1
                  elif saled3 == a2:
                    if a4 >= a2:
                     pers.append(a4)
                     ronda.append(pat4)
                     print("el nuevo valor de",objeto," es de",a4)
                     saled4=a4
                     break
                    elif a4 <= a2:
                     print("el nuevo valor de",objeto," continua igual",a2)
                     saled4=a2    
                     break
                  elif saled3==a3:
                    if a4 >= a3:
                     pers.append(a4)
                     ronda.append(pat4)
                     print("el nuevo valor de",objeto," es de",a4)
                     saled4=a4
                     break
                    elif a4 <= a3:
                     print("el nuevo valor de",objeto," continua igual",a3)
                     saled4=a3
                     break

                else:
                 print("caracter invalido")

              while True:
               if premio5 >= 3:
                print("El participante",pat5," ya ganó el limite de productos")
               elif premio5 <= 2:
                print(pat5)
                a5=(input("cuanto vas a ofrecer?--->"))
                if a5.isnumeric():
                  print(pat5,"ofrece",a5)
                  if saled4 == p: 
                    if a5 >= p:
                      pers.append(a5)
                      ronda.append(pat5)
                      print("el nuevo valor de",objeto," es de",a5)
                      saled5=a5
                      break
                    elif a5 <= p:
                     print("el nuevo valor de",objeto," continua igual",p)
                     saled5=p
                     break
                  elif saled4 == a1:
                    if a5 >= a1:
                     pers.append(a5)
                     ronda.append(pat5)
                     print("el nuevo valor de",objeto," es de",a5)
                     saled5=a5
                     break
                    elif a5 <= a1:
                     print("el nuevo valor de",objeto," continua igual",a1)
                     saled5=a1
                  elif saled4 == a2:
                    if a5 >= a2:
                     pers.append(a5)
                     ronda.append(pat5)
                     print("el nuevo valor de",objeto," es de",a5)
                     saled5=a5
                     break
                    elif a5 <= a2:
                     print("el nuevo valor de",objeto," continua igual",a2)
                     saled5=a2    
                     break
                  elif saled4==a3:
                    if a5 >= a3:
                     pers.append(a5)
                     ronda.append(pat5)
                     print("el nuevo valor de",objeto," es de",a5)
                     saled5=a5
                     break
                    elif a5 <= a3:
                     print("el nuevo valor de",objeto," continua igual",a3)
                     saled5=a3
                     break
                  elif saled4==a4:
                    if a5 >= a4:
                     pers.append(a5)
                     ronda.append(pat5)
                     print("el nuevo valor de",objeto," es de",a5)
                     saled5=a5
                     break
                    elif a5 <= a4:
                     print("el nuevo valor de",objeto," continua igual",a4)
                     saled5=a4
                     break
                else:
                 print("caracter invalido")
              
              fin =time.time()
              dicts=dict(zip(ronda,pers))
              if fin - incio >=10:
               print("se acabo el tiempo")
               print("asi quedaron las pujas")
              for a,b in dicts.items():
               print(f"{a}:{b}")
              bobo=max(dicts, key=dicts.get)
             
              print("el ganador de",objeto," es",bobo)
              if bobo==pat1:
                 premio=premio+1
              elif bobo==pat2:
                 premio2=premio2+1                
              elif bobo==pat3:
                 premio3=premio3+1                
              elif bobo==pat4:
                 premio4=premio4+1                
              elif bobo==pat5:
                 premio5=premio5+1
                  
              print("(1)--quieres regresar al menu")
              print("(2)--salir")
              try:
               o=input("--->")
               if o =="1":
                 print("sera redirigido al menu de subastas")
                 os.system("cls")
                 break
               elif o =="2":
                 print("bye")
                 break 
              except:
                print("caracter invalido")

        except:
          ("caracter invalido")
    elif ak=="s":
      print("bye y regrese")
      break
  except:
    print("caracter invalido")

    

