# Condition
datef = int(str(payslip.date_from)[-2:])
datet = int(str(payslip.date_to)[-2:])

if datet >= 28 and contract.x_clothing_laundry:
    result = True
else:
    result = False
    
# Computation
if result:
    result = contract.x_clothing_laundry/12
