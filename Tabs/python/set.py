def Input(a):
    l = set()
    for i in range(a):
        element = int(input("Enter the element: "))
        membership = float(input("Enter the membership: "))
        
        if membership < 0 or membership > 1:
            print("Error: Membership values must be between 0 and 1.")
            return None
        
        if any(e[0] == element for e in l):
            print("Error: Duplicate elements detected in the set.")
            return None
        
        l.add((element, membership))
    
    if not l:
        print("Error: Fuzzy sets must not be empty.")
        return None

    return l

def UnionFunc(setA, setB):
    unionSet = set()
    for i in setA:
        if i[0] in {e[0] for e in unionSet}:
            for j in unionSet:
                if j[0] == i[0]:
                    if j[1] < i[1]:
                        unionSet.remove(j)
                        unionSet.add(i)
                    break
        else:
            unionSet.add(i)
    
    for i in setB:
        if i[0] in {e[0] for e in unionSet}:
            for j in unionSet:
                if j[0] == i[0]:
                    if j[1] < i[1]:
                        unionSet.remove(j)
                        unionSet.add(i)
                    break
        else:
            unionSet.add(i)
    
    return unionSet

def Intersection(setA, setB):
    intersectionSet = set()
    for i in setA:
        if any(e[0] == i[0] for e in setB):
            membership_in_b = next(e[1] for e in setB if e[0] == i[0])
            intersectionSet.add((i[0], min(i[1], membership_in_b)))
    return intersectionSet

def Complement(setA, universe):
    complementSet = set()
    for element, membership in universe:
        if element in {e[0] for e in setA}:
            membership_in_a = next(e[1] for e in setA if e[0] == element)
            complementSet.add((element, 1 - membership_in_a))
        else:
            complementSet.add((element, 1))
    return complementSet

def are_sets_equal(setA, setB):
    if len(setA) != len(setB):
        return False
    for element in setA:
        if element not in setB:
            return False
    return True

# Question 2

n = int(input("Enter the number of elements in set A: "))
setA = Input(n)
if setA is None:
    exit()

m = int(input("Enter the number of elements in set B: "))
setB = Input(m)
if setB is None:
    exit()

universe = setA.union(setB)

complementA = Complement(setA, universe)
complementB = Complement(setB, universe)

lhs_union = UnionFunc(complementA, complementB)
lhs_intersection = Intersection(complementA, complementB)

rhs_intersection_complement = Complement(Intersection(setA, setB), universe)
rhs_union_complement = Complement(UnionFunc(setA, setB), universe)

if are_sets_equal(lhs_union, rhs_intersection_complement):
    print("A' ∪ B' = (A ∩ B)' holds true.")
else:
    print("A' ∪ B' = (A ∩ B)' does not hold true.")

if are_sets_equal(lhs_intersection, rhs_union_complement):
    print("A' ∩ B' = (A ∪ B)' holds true.")
else:
    print("A' ∩ B' = (A ∪ B)' does not hold true.")


# Question 1

# num1 = int(input("Size of the set A: "))
# setA = Input(num1)
# if setA is None:
#     setA = set()

# num2 = int(input("Size of the set B: "))
# setB = Input(num2)
# if setB is None:
#     setB = set()

# Union = UnionFunc(setA, setB)
# print("Union: ", Union)
# print("Intersection: ", Intersection(setA, setB))
# print("Complement: ", Complement(setA, Union))
def Intersection(setA, setB):
    intersectionSet = set()
    for i in setA:
        if any(e[0] == i[0] for e in setB):
            membership_in_b = next(e[1] for e in setB if e[0] == i[0])
            intersectionSet.add((i[0], min(i[1], membership_in_b)))
    return intersectionSet

def Complement(setA, universe):
    complementSet = set()
    for element, membership in universe:
        if element in {e[0] for e in setA}:
            membership_in_a = next(e[1] for e in setA if e[0] == element)
            complementSet.add((element, 1 - membership_in_a))
        else:
            complementSet.add((element, 1))
    return complementSet

def are_sets_equal(setA, setB):
    if len(setA) != len(setB):
        return False
    for element in setA:
        if element not in setB:
            return False
    return True

n = int(input("Enter the number of elements in set A: "))
setA = Input(n)
if setA is None:
    exit()

m = int(input("Enter the number of elements in set B: "))
setB = Input(m)
if setB is None:
    exit()

universe = setA.union(setB)

complementA = Complement(setA, universe)
complementB = Complement(setB, universe)

lhs_union = UnionFunc(complementA, complementB)
lhs_intersection = Intersection(complementA, complementB)

rhs_intersection_complement = Complement(Intersection(setA, setB), universe)
rhs_union_complement = Complement(UnionFunc(setA, setB), universe)

if are_sets_equal(lhs_union, rhs_intersection_complement):
    print("A' ∪ B' = (A ∩ B)' holds true.")
else:
    print("A' ∪ B' = (A ∩ B)' does not hold true.")

if are_sets_equal(lhs_intersection, rhs_union_complement):
    print("A' ∩ B' = (A ∪ B)' holds true.")
else:
    print("A' ∩ B' = (A ∪ B)' does not hold true.")