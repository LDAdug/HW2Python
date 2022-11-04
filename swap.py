def swap_list(somelist):
    length=len(somelist)
    
    if len(somelist) % 2 == 0:
        temp = somelist[-1]
        somelist[-1] = somelist[(length//2)-1]
        somelist[(length//2)-1] = temp
        return somelist
    else:
        temp =somelist[-1]
        somelist[-1] = somelist[length//2]
        somelist[length//2] = temp
        return somelist

    
    
