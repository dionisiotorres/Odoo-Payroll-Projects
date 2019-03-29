# Condition is always True
# Computation
for line in payslip.input_line_ids:
    if line.code == 'ABS':
        result = 0 - contract.wage * line.amount
