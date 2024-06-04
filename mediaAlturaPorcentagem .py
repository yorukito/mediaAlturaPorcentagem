azul = '\033[34m'
vermelho = '\033[1;31m'
parar_cor = '\033[m'


alt = []
masculino = feminino = 0
maior_altura = float("-inf")
menor_altura = float("inf")
masculino = 0
genero = 0
soma_alt = 0

while 1:

    # continuar
    cont = input(f"prosseguir?\n{vermelho}s{parar_cor} ou {vermelho}n{parar_cor}: ")
    test_p = 's, n'

    while cont not in test_p:
        print(f"{vermelho}perdão, não foi possive ler{parar_cor}")
        cont = input(f"prosseguir?\n{vermelho}s{parar_cor} ou {vermelho}n{parar_cor} ")


    if cont == 's':
        # genero
        genero = input("masculino [m], feminino[f]: ")
        test_g = 'm, f'

        while genero not in test_g:
            genero = input(f"masculino [{vermelho}m{parar_cor}], feminino[{vermelho}f{parar_cor}]: ")


        if genero == "m":
            masculino += 1
            alt.append('masculino')

        if genero == "f":
            feminino += 1
            alt.append('feminino')

        # altura
        altura = (input("altura: "))
        test_a = altura.replace(".", "").isnumeric()

        while not test_a:
            print(f"{vermelho}digite um número{parar_cor}")
            altura = (input("altura: "))
            test_a = altura.replace(".", "").isnumeric()
        altura = float(altura)
        alt.append(altura)

        if altura < menor_altura:
            menor_altura = altura

        if altura > maior_altura:
            maior_altura = altura
        soma_alt += altura

    else:
        break

if len(alt) == 0:
    print(f"{vermelho}nao foi possivel realizar o procedimento{parar_cor}")

else:

    media_m = alt.count('masculino')/ (alt.count('masculino')+alt.count('feminino')) * 100
    media_f = alt.count('feminino')/ (alt.count('masculino')+alt.count('feminino')) * 100
    media_alt = soma_alt / (alt.count('masculino')+alt.count('feminino'))

    # medias
    print(f"\n\nmedia masculina: {azul}{media_m:.2f}%{parar_cor}\nmedia feminina: {azul}{media_f:.2f}%{parar_cor}\nmedia da altura: {azul}{media_alt:.2f}{parar_cor}\n")
    # altura
    print(f"maior altura: {azul}{maior_altura}{parar_cor}\nmenor altura: {azul}{menor_altura}{parar_cor}\n")
    # quantidade dos generos
    print(f"quntidade masculina: {azul}{alt.count('masculino')}{parar_cor}\nquantidade feminina: {azul}{alt.count('feminino')}{parar_cor}")
    print(f"\n{alt}")