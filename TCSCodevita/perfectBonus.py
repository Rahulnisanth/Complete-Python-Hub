def min_budget_for_all_orders(n, projects):
    projects.sort(key=lambda x: (x[1], -x[2]))
    min_budget = 0
    current_budget = 0

    for project in projects:
        expenditure, bonus, penalty = project
        if current_budget < expenditure:
            current_budget = expenditure

        min_budget += current_budget
        current_budget += bonus

    return min_budget


n = int(input())
projects = []
for _ in range(n):
    expenditure, bonus_penalty = map(str, input().split())
    expenditure, bonus_penalty = map(int, expenditure.split()), map(
        int, bonus_penalty.split()
    )
    projects.append((expenditure[0], bonus_penalty[0], bonus_penalty[1]))

print(min_budget_for_all_orders(n, projects))
