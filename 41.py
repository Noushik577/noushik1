evTuple = (1,2,3,4,5,6,7,8,9,10)
print("Tuple Items = ", evTuple)

print("\nThe Even Numbers in this evTuple Tuple are:")
for i in range(len(evTuple)):
    if(evTuple[i] % 2 == 0):
        print(evTuple[i], end = "  ")