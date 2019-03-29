# Condition
if contract.moving_allowance:
    result = True
    
# Computation
if result:
    for line in payslip.input_line_ids:
        if line.code == 'ABS':
            absday = line.amount

    result = contract.moving_allowance * (WORKDAY - absday)
