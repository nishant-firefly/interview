print("########## Array and the variations :  arr = [1,2,3]#######")
arr = [1,2,3]
print("Append arr.append(4): should be O(1) but in Amortized: O(n)")
arr.append(4)
print(arr)
print("Delete => del arr[3]: O(n) Omega(1) Index Error if not found")
del arr[3]
print(arr)
print("Append arr.insert(1,5): O(n) Imp: No index Error, will insert in end or \n\tstart for postive and negative number")
arr.insert(1,5)
print(arr)
print("arr[1]: O(1)  Index Error if not found")



