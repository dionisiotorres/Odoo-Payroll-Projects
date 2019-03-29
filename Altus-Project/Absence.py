# Condition
result = False
if contract.wage > 13093.84:
  result = True
  

# Computation
if result:
    unpaid_leaves = 0
    amount = 0
    
    # Amount of Unpaid Leaves
    if worked_days.INSLEAVES:
        unpaid_leaves += worked_days.INSLEAVES.number_of_days
    if worked_days.UNPAID:
        unpaid_leaves += worked_days.UNPAID.number_of_days
    amount += unpaid_leaves * contract.wage*12/313
    result = 0 - amount
