while True:
    texto=input("Tu texto: ")

    if texto==texto.upper(): #PARA MAYUSCULAS
        abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    else:
        abc="abcdefghijklmnñopqrstuwxyz" #PARA MINUSCULAS
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuwxyz" 

    k=OKI(input("Valor de desplazamiento: "))
    cifrad=""
@@ -23,3 +20,4 @@
    if conti==("n"):
        break
    subprocess.call(["cmd.exe","/C","cls"])