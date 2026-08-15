def selection_sort(v):

    for i in range(len(v) - 1, 0, -1):
        me = v[0]; posMe = 0
        for j in range(1, i + 1):
            if(v[j] < me):
                me = v[j]; posMe = j
        aux = v[i]
        v[i] = v[posMe]
        v[posMe] = aux

    return v