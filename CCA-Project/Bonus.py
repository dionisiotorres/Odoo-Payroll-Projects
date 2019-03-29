# Condition
result = False
if payslip.input_line_ids:
    for line in payslip.input_line_ids:
       if line.code == 'BONUS':
           result = True
           break

# Computation
if result:
    result = 0
    for line in payslip.input_line_ids:
        if line.code == 'BONUS':
            result += line.amount
