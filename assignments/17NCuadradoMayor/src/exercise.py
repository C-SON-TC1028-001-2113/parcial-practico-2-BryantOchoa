
def main():
    
#escribe tu código abajo de esta línea
    numero = int(input("Escribe un numero : "))
    res = 1
    while res**2<=numero:
        res += 1
    print(res)

if __name__=='__main__':
    main()
