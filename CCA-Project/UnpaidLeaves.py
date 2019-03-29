# Condition is always True
# Computation
unpaid_leaves = 0

# Amount of Unpaid Leaves

if worked_days.INSLEAVES:
    unpaid_leaves += worked_days.INSLEAVES.number_of_days

if worked_days.UNPAID:
    unpaid_leaves += worked_days.UNPAID.number_of_days

result = unpaid_leaves
