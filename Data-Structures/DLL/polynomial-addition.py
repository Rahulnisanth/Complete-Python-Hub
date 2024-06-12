class PolyNode:
    def __init__(self, coefficient=0, power=0, next=None):
        self.coefficient = coefficient
        self.power = power
        self.next = next

class PolyAdd:
    def addPoly(self, poly1: "PolyNode", poly2: "PolyNode") -> "PolyNode":
        result = current = PolyNode()
        while poly1 and poly2:
            if poly1.power > poly2.power:
                current.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            if poly1.power < poly2.power:
                current.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            else:
                current.next = PolyNode((poly1.coefficient + poly2.coefficient), poly1.power)
                poly1 = poly1.next
                poly2 = poly2.next
            # Traversing the current node :
            if current.next: 
                current = current.next
        # Adding extras in poly - 1 :
        while poly1:
            current.next = PolyNode(poly1.coefficient, poly1.power)
            poly1 = poly1.next
        # Adding extras in poly - 2 :
        while poly2:
            current.next = PolyNode(poly2.coefficient, poly2.power)
            poly2 = poly2.next
        return result.next

# Creating the linked list from input :
def create_poly_linked_list(coefficients_and_powers):
    head = None
    tail = None
    for i in range(0, len(coefficients_and_powers), 2):
        coefficient = coefficients_and_powers[i]
        power = coefficients_and_powers[i + 1]
        new_node = PolyNode(coefficient, power)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

# Printing the formatted result  :
def print_poly_linked_list(result):
    terms = []
    while result:
        if result.power == 0:
            terms.append(f"{result.coefficient}")
        elif result.power == 1:
            terms.append(f"{result.coefficient}x")
        else:
            terms.append(f"{result.coefficient}x{result.power}")
        result = result.next
    print(" + ".join(terms).replace('+ -', '- '))

# Input stream :
# Poly - 1 ...
n1 = int(input())
coefficients_and_powers1 = list(map(int, input().split()))
# Poly - 2 ...
n2 = int(input())
coefficients_and_powers2 = list(map(int, input().split()))
# Main drive program ...
poly1 = create_poly_linked_list(coefficients_and_powers1)
poly2 = create_poly_linked_list(coefficients_and_powers2)
obj = PolyAdd()
result = obj.addPoly(poly1, poly2)
print("Result after adding two polynomials")
print_poly_linked_list(result)

