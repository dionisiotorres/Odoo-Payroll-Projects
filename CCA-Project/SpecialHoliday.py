# Condition
for line in payslip.input_line_ids:
    if line.code == 'SHOLIDAY':
        a = line.amount

if a > 0:
    result = True
    
# Computation
if result:
    for line in payslip.input_line_ids:
        if line.code == 'SHOLIDAY':
            result = contract.wage  * line.amount * 0.3
