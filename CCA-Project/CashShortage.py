# Condition
for line in payslip.input_line_ids:
    if line.code == 'SHORTAGE':
        a = line.amount
        
if a > 0:
    result = True
    
# Computation
if result:
    for line in payslip.input_line_ids:
        if line.code == 'SHORTAGE':
            result = line.amount
