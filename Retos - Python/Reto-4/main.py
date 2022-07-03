NumeroBaldosas , BaldosasSoportadas  = input().split()
ListBaldosas = input().split()

Repeticiones = {}
TotalFallas = 0
Fallas = 0
MemoriaRam = 1

#TotalFallas = len(ListBaldosas) - len(set(ListBaldosas))   Una linea :))

for i in ListBaldosas:
    if i in Repeticiones:
        Repeticiones[i] +=1
    else:
        Repeticiones[i] = 0

for j in Repeticiones:
    if Repeticiones[j] != 0:
        TotalFallas += Repeticiones[j] #Varias Lineas :)))))))

for k in ListBaldosas:
    if k in ListBaldosas[MemoriaRam:int(BaldosasSoportadas) + MemoriaRam]:
        Fallas+=1
    MemoriaRam+=1

print(TotalFallas , Fallas , NumeroBaldosas)