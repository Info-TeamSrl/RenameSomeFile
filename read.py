import os
arr = os.listdir()
x = len(arr)
for n in range(x):
    print(arr[n])
    aux=arr[n]
    aux=aux.replace("_WEB", "")
    aux=aux.replace("_web", "")
    aux=aux.replace("-WEB", "")
    print(aux)
    print("--------------------------")
    try:
        os.rename(arr[n], aux)
    except:
        print("An exception occurred"+arr[n]+"-"+aux)