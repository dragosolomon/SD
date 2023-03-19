def radix(arr, base=10):
    if len(arr) == 0:
        return arr

    # Determina maximul din array
    max_val = max(arr)

    # Determina numarul de cifre necesare
    num_digits = 0
    while max_val > 0:
        num_digits += 1
        max_val //= base

    # Sorteaza array-ul pe fiecare cifra
    for i in range(num_digits):
        buckets = [[] for j in range(base)]
        for j in arr:
            digit = j // (base**i) % base
            buckets[digit].append(j)
        arr = [item for bucket in buckets for item in bucket]
    
    return arr


arr = [2,5,10,34,4,8,18]
radix(arr)
print(arr)