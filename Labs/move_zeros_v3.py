def move_zeros_v3(l):
    for n in l:
        print(n)
        if n != 0:
            x = n
            index = l.index(x)
            print("Choisi:", n)
            print("Index:", l.index(n))
            for y in range(0, index):
                if l[y] == 0:
                    l[index] = 0
                    l[y] = x
                    print("Devient Zero:", index)
                    print ("Index: ",y, "Change en: ", l[y])
                    break;

liste = list(eval(input("Entrer un liste separe par des virgules: ")))

z = move_zeros_v3(liste)
print(liste, z)

