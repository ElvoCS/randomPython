
l = [3,4,65,32,1,7,9,5,4,45,907,65,4335,790,12]

def sort(arr):
    while True:
        corrected = False
        for i in range(0, len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrected = True
        if not corrected:
            return arr

print (sort(l))
