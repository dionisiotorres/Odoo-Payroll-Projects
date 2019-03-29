# Condition
for line in payslip.input_line_ids:
    if line.code == 'OT':
        if line.amount > 0:
            result = True
            
# Computation
if result:
    for line in payslip.input_line_ids:
        if line.code == 'OT':
            result = contract.wage / 10 * line.amount * 1.3
