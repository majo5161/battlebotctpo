##########################################################################################################
#               __                                                                      __               #
#       (      /  \                         +++++++++++++++++                          /  \      )       #
#       ( (   /    \_______________________|                 |_______________________ /    \   ) )       #
#     (    (  ( + )     _____________      | Battle bot CTPO |      ______________     ( + )  )    )     #
#       ( (                          ------|                 |------                           ) )       #
#       (                                    +++++++++++++++++                                  )        #
#                                                                                                        #
#            									Pasantía           
#                                                                                                        #
#                   Colegio Técnico Profesional de Oreamuno, Informática Empresarial                     #
#                           Diseño lucha robots CENFOTEC                                                                      #
#                               Integrantes:                                                             #
#                                                                                                        #
#                                  - Montenegro Araya Manfred                                            #
#                                  - Mora Torres Jazmín                                                  #
#                                  - Ramírez Guzmán María Celeste                                              #
#                                  - Vega Camacho María José
#								   - Gamboa Gonzalez Jefferson
#                                                                                                        #  
#                               Profesor Tutor Pasantía:                                                          #
#                                    Ronald Fallas Rojas                                                 #
#                                                                                                        #
#                                        Año: 2024                                                       #
#                                      Versión: 1.0                                                      #
##########################################################################################################



from ideaboard import IdeaBoard
import espnow
import board
from time import sleep


ib = IdeaBoard()
primeravez = True
g90 = 1

servo1 = ib.Servo(board.IO4)

def giro90():
    ib.motor_1.throttle = velocidadGiro * -1
    ib.motor_2.throttle = velocidadGiro
    sleep(g90)
    stop()

def ataqueInicio():
    #ataque inicial de 0
    servo1.angle = 0
    sleep(2)

def atacar():
    #ataca en un ángulo de 90grados
    servo1.angle = 90
    sleep(2)
    
    
#    servo1.angle = 10
#    sleep(5)
while True:
    ataqueInicio()
    atacar()



