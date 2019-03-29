# Condition
datef = int(str(payslip.date_from)[-2:])
datet = int(str(payslip.date_to)[-2:])
month = int(str(payslip.date_to)[5:7])

if datet >= 28 and contract.x_transportation:
    result = True
    
# Computation
if result:
    result = contract.x_representation
