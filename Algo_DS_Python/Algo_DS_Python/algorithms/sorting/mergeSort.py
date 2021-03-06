

def merge(x,y):
    w = []
    i = 0
    j = 0
    while(j < len(y) or i < len(x)):
        if(j == len(y)):
            w.append(x[i])
            i+=1
        elif(i == len(x)):
            w.append(y[j])
            j+=1
        elif(x[i] < y[j]):
            w.append(x[i])
            i+=1
        else:
            w.append(y[j])
            j+=1
    return w


def mergeSort(x):
    if len(x)  == 1 or len(x) == 0:
        return x
    nx = x[0:len(x)//2]
    lx = x[len(x)//2:len(x)] 
    nx = mergeSort(nx)
    lx = mergeSort(lx)
    return merge(nx,lx)

