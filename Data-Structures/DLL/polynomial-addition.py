class PolyNode:
    def __init__(self, coefficient=0, power=0, next_node=None):
        self.coefficient = coefficient
        self.power = power
        self.next = next_node

class PolyAdd:
    def addPoly(self, poly1: "PolyNode", poly2: "PolyNode") -> "PolyNode":
        dummy = current = PolyNode()
    
        while poly1 and poly2:
            if poly1.power > poly2.power:
                current.next = PolyNode(poly1.coefficient, poly1.power)
                poly1 = poly1.next
            elif poly1.power < poly2.power:
                current.next = PolyNode(poly2.coefficient, poly2.power)
                poly2 = poly2.next
            else:
                sum_coefficient = poly1.coefficient + poly2.coefficient
                if sum_coefficient != 0:
                    current.next = PolyNode(sum_coefficient, poly1.power)
                poly1 = poly1.next
                poly2 = poly2.next

            if current.next: 
                current = current.next

        current.next = poly1 or poly2
    
        return dummy.next

def create_poly_linked_list(coefficients_and_powers):
    head = None
    tail = None
    for i in range(0, len(coefficients_and_powers), 2):
        coefficient = coefficients_and_powers[i]
        power = coefficients_and_powers[i+1]
        new_node = PolyNode(coefficient, power)
        if head is None:
            head = new_node
            tail = new_node
        else:
            tail.next = new_node
            tail = new_node
    return head

def print_poly_linked_list(poly):
    if not poly:
        print("0")
        return
    terms = []
    while poly:
        if poly.power == 0:
            terms.append(f"{poly.coefficient}")
        elif poly.power == 1:
            terms.append(f"{poly.coefficient}x")
        else:
            terms.append(f"{poly.coefficient}x^{poly.power}")
        poly = poly.next
    print(" + ".join(terms).replace('+ -', '- '))


n1 = int(input())
coefficients_and_powers1 = list(map(int, input().split()))

n2 = int(input())
coefficients_and_powers2 = list(map(int, input().split()))

poly1 = create_poly_linked_list(coefficients_and_powers1)
poly2 = create_poly_linked_list(coefficients_and_powers2)
obj = PolyAdd()
result = obj.addPoly(poly1, poly2)

print("Result")
print_poly_linked_list(result)

