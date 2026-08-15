def mediana_menor(A, B):
    n = len(A)
    
    if n == 1:
        return min(A[0], B[0])
    if n == 2:
        return sorted(A + B)[1]

    mediana_index = n // 2

    if n % 2 == 0:
        x = A[mediana_index - 1]
        y = B[mediana_index]
        
        if x == y:
            return x
        elif y > x:
            return mediana_menor(A[mediana_index:], B[:mediana_index])
        else:
            return mediana_menor(A[:mediana_index], B[mediana_index:])
    else:
        x = A[mediana_index]
        y = B[mediana_index]
        
        if x == y:
            return x
        elif y > x:
            return mediana_menor(A[mediana_index:], B[:mediana_index + 1])
        else:
            return mediana_menor(A[:mediana_index + 1], B[mediana_index:])

#Não faço a mínima ideia de como fazer essa, mas foi o código que Bustamonte passou. 