def selection_sort(v):

    for i in range(len(v) - 1, 0, -1):
        m = v[0]; posM = 0
        for j in range(1, i + 1):
            if(v[j] > m):
                m = v[j]; posM = j
        aux = v[i]
        v[i] = v[posM]
        v[posM] = aux

    return v


