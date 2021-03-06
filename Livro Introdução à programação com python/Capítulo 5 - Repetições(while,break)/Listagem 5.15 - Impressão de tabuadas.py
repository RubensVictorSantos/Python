print("Listagem 5.15 - Impressão de tabuada. \n")


tabuada = 1
while tabuada <= 10:

    print("\nTabuada do: %d" % tabuada)
    número = 0

    while número <= 10:
        print("%d x %d = %d " % (tabuada, número, tabuada * número))
        número += 1
    tabuada += 1
