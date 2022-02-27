'''1 Subsets'''

l = [1, [2, 3]]
def powerset(x):
    result = [[]]
    for i in x:
        newsubset = [sub + [i] for sub in result]
        result.extend(newsubset)
    print(result)

powerset([1, 2, [2, 3]])