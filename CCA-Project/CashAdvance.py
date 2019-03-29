# Condition
for line in payslip.input_line_ids:
    if line.code == 'ADVANCE':
        a = line.amount
        
if a > 0:
    result = True
    
# Computation
for line in payslip.input_line_ids:
    if line.code == 'ADVANCE':
        a = line.amount
        
if a > 0:
    result = True
