from tkinter import Y
import pygame
pygame.font.init()
Ventana = pygame.display.set_mode((500, 500))
pygame.display.set_caption("JUEGO DE SUDOKU")
x = 0
z = 0
diff = 500 / 9
value= 0
cuadriculapordefecto =[
        [0, 0, 4, 0, 6, 0, 0, 0, 5],
        [7, 8, 0, 4, 0, 0, 0, 2, 0],
        [0, 0, 2, 6, 0, 1, 0, 7, 8],
        [6, 1, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 7, 5, 4, 0, 0, 6, 1],
        [0, 0, 1, 7, 5, 0, 9, 3, 0],
        [0, 7, 0, 3, 0, 0, 0, 1, 0],
        [0, 4, 0, 2, 0, 6, 0, 0, 7],
        [0, 2, 0, 0, 0, 7, 4, 0, 0],
    ]
 

font = pygame.font.SysFont("comicsans", 40)
font1 = pygame.font.SysFont("comicsans", 20)
def cord(pos):
    global x
    x = pos[0]//diff
    global z
    z = pos[1]//diff

def cuadrodestacado():
    for k in range(2):
        pygame.draw.line(Ventana, (0, 0, 0), (x * diff-3, (z + k)*diff), (x * diff + diff + 3, (z + k)*diff), 7)
        pygame.draw.line(Ventana, (0, 0, 0), ( (x + k)* diff, z * diff ), ((x + k) * diff, z * diff + diff), 7)  
       
def dibujarlineas():
    for i in range (9):
        for j in range (9):
            if cuadriculapordefecto[i][j]!= 0:
                pygame.draw.rect(Ventana, (255, 255, 0), (i * diff, j * diff, diff + 1, diff + 1))
                text1 = font.render(str(cuadriculapordefecto[i][j]), 1, (0, 0, 0))
                Ventana.blit(text1, (i * diff + 15, j * diff + 15))         
    for l in range(10):
        if l % 3 == 0 :
            thick = 7
        else:
            thick = 1
        pygame.draw.line(Ventana, (0, 0, 0), (0, l * diff), (500, l * diff), thick)
        pygame.draw.line(Ventana, (0, 0, 0), (l * diff, 0), (l * diff, 500), thick)     
 
    
def valorderelleno(value):
    text1 = font.render(str(value), 1, (0, 0, 0))
    Ventana.blit(text1, (x * diff + 15, z * diff + 15))   
 

def errordeaumento():
    text1 = font.render("equivocado!", 1, (0, 0, 0))
    Ventana.blit(text1, (20, 570)) 
def errordeaumento1():
    text1 = font.render("equivocado! Introduzca una clave válida para el juego", 1, (0, 0, 0))
    Ventana.blit(text1, (20, 570)) 
 
def validvalue(m, k, l, value):
    for it in range(9):
        if m[k][it]== value:
            return False
        if m[it][l]== value:
            return False
    it = k//3
    jt = l//3
    for k in range(it * 3, it * 3 + 3):
        for l in range (jt * 3, jt * 3 + 3):
            if m[k][l]== value:
                return False
    return True
def solvegame(cuadriculapordefecto, i, j):
     
    while cuadriculapordefecto[i][j]!= 0:
        if i<8:
            i+= 1
        elif i == 8 and j<8:
            i = 0
            j+= 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()   
    for it in range(1, 10):
        if validvalue(cuadriculapordefecto, i, j, it)== True:
            cuadriculapordefecto[i][j]= it
            global x, z
            x = i
            z = j
            Ventana.fill((255, 255, 255))
            dibujarlineas()
            cuadrodestacado()
            pygame.display.update()
            pygame.time.delay(20)
            if solvegame(cuadriculapordefecto, i, j)== 1:
                return True
            else:
                cuadriculapordefecto[i][j]= 0
            Ventana.fill((0,0,0))
         
            dibujarlineas()
            cuadrodestacado()
            pygame.display.update()
            pygame.time.delay(50)   
    return False 
def resultadosdejuego():
    text1 = font.render("juego terminado", 1, (0, 0, 0))
    Ventana.blit(text1, (20, 570)) 
bandera=True  
bandera1 = 0
bandera2 = 0
rs = 0
error = 0
while bandera:
    Ventana.fill((64,224,208))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            bandera = False   
        if event.type == pygame.MOUSEBUTTONDOWN:
            bandera1 = 1
            pos = pygame.mouse.get_pos()
            cord(pos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x-= 1
                bandera1 = 1
            if event.key == pygame.K_RIGHT:
                x+= 1
                bandera1 = 1
            if event.key == pygame.K_UP:
                Y-= 1
                bandera1 = 1
            if event.key == pygame.K_DOWN:
                Y+= 1
                bandera1 = 1   
            if event.key == pygame.K_1:
                value = 1
            if event.key == pygame.K_2:
                value = 2   
            if event.key == pygame.K_3:
                value = 3
            if event.key == pygame.K_4:
                value = 4
            if event.key == pygame.K_5:
                value = 5
            if event.key == pygame.K_6:
                value = 6
            if event.key == pygame.K_7:
                value = 7
            if event.key == pygame.K_8:
                value = 8
            if event.key == pygame.K_9:
                value = 9 
            if event.key == pygame.K_RETURN:
                bandera2 = 1  
            if event.key == pygame.K_r:
                rs = 0
                error = 0
                bandera2 = 0
                cuadriculapordefecto=[
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
                ]
            if event.key == pygame.K_d:
                rs = 0
                error = 0
                bandera2 = 0
                cuadriculapordefecto  =[
                    [0, 0, 4, 0, 6, 0, 0, 0, 5],
                    [7, 8, 0, 4, 0, 0, 0, 2, 0],
                    [0, 0, 2, 6, 0, 1, 0, 7, 8],
                    [6, 1, 0, 0, 7, 5, 0, 0, 9],
                    [0, 0, 7, 5, 4, 0, 0, 6, 1],
                    [0, 0, 1, 7, 5, 0, 9, 3, 0],
                    [0, 7, 0, 3, 0, 0, 0, 1, 0],
                    [0, 4, 0, 2, 0, 6, 0, 0, 7],
                    [0, 2, 0, 0, 0, 7, 4, 0, 0],
                ]
    if bandera2 == 1:
        if solvegame(cuadriculapordefecto , 0, 0)== False:
            error = 1
        else:
            rs = 1
        bandera2 = 0   
    if value != 0:           
        valorderelleno(value)
        if validvalue(cuadriculapordefecto , int(x), int(z), value)== True:
            cuadriculapordefecto[int(x)][int(z)]= value
            bandera1 = 0
        else:
            cuadriculapordefecto[int(x)][int(z)]= 0
            errordeaumento1()  
        value = 0   
       
    if error == 1:
        errordeaumento() 
    if rs == 1:
        resultadosdejuego()       
    dibujarlineas() 
    if bandera1 == 1:
        cuadrodestacado()      
    pygame.display.update() 
   
pygame.quit()    