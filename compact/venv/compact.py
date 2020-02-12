def compact(*args):

    oglist = []
    if "generator" in str(type(args[0])):
        print("it's a generator!")
        for num in args[0]:
            # input(num)
            oglist.append(num)
    else:
        oglist = [*args[0], ]
    print("original list:", oglist)
    cleanedlist = []
    cleanedlist.append(oglist[0])
    old = cleanedlist[-1]
    for ii, x in enumerate(oglist):
        # if index is more than 0 and the old lists previous number is not x
        if ii > 0 and oglist[ii-1] != x:
            cleanedlist.append(x)
    old = cleanedlist[-1]
    return cleanedlist


if __name__ == "__main__":
    import random
    # lista = [random.randint(0, 3) for x in range(0, 10)]
    # print(lista)
    genlista = compact(random.randint(0, 3) for x in range(0, 10))
    print("genlista",genlista)