def find_min_bowls(compound_defs, compounds_to_prepare):
    dependencies = {}
    for definition in compound_defs:
        compound, elements = definition.split('=')
        elements = elements.split('+')
        dependencies[compound] = elements

    def max_depth(compound, memo):
        if compound not in dependencies: return 0
        
        if compound in memo:
            return memo[compound]
        
        max_depth_value = 0
        for elem in dependencies[compound]:
            max_depth_value = max(max_depth_value, max_depth(elem, memo))
        
        memo[compound] = max_depth_value + 1
        return memo[compound]

    max_bowls = 0
    memo = {}
    for compound in compounds_to_prepare:
        max_bowls = max(max_bowls, max_depth(compound, memo))
    return max_bowls

# Input processing
N = int(input())
compound_defs = [input().strip() for _ in range(N)]
M = int(input())
compounds_to_prepare = [input().strip() for _ in range(M)]
# Result
result = find_min_bowls(compound_defs, compounds_to_prepare)
print(result)
