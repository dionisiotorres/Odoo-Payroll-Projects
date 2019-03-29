# Condition
if contract.meal_allowance:
    result = True
    
# Computation
if result:
    for line in payslip.input_line_ids:
        if line.code == 'ABS':
            absday = line.amount

    result = contract.meal_allowance * (WORKDAY - absday)
