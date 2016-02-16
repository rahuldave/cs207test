
def myaverage(l:list)->float:
    """
    Calculate the average of list l
    
    Examples:
    
    >>> myaverage([1,2])
    1.5
    
    """
    n = len(l)
    if n==0:
        raise ValueError("cant calculate mean of length 0 list")
    try:
        thesum = sum(l)
    except:
        raise TypeError("Cannot sum things of different types")
    average = thesum/n
    return average

def mymedian(l:list)->float:
    """
    Calculate the average of list l
    
    Examples:
    
    >>> mymedian([1,2,3])
    2
    
    >>> mymedian([1,2,3,4])
    2.5
    """
    lsorted = sorted(l)
    mididx = len(lsorted)//2
    if len(lsorted) % 2 == 0: #even
        return (lsorted[mididx-1] + lsorted[mididx])/2
    else:
        return lsorted[mididx]