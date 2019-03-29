# Condition is always True
# Computation
for line in payslip.input_line_ids:
    if line.code == 'WT':
        result = line.amount
