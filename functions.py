def histogram(l1):
    myMap = {}
    for i in l1:
        myMap[i] = myMap.get(i, 0) + 1    
    sortedMap = sorted(myMap.items(), key=lambda x: (x[1], x[0]))
    print(type(sortedMap))
    return sortedMap

print(histogram([13,12,11,13,14,13,7,7,13,14,12]))
