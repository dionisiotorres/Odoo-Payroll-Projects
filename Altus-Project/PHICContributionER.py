# Condition
datef = int(str(payslip.date_from)[-2:])
datet = int(str(payslip.date_to)[-2:])

if datet == 15:
    result = True
else:
    result = False
    
# Computation
if result:
    if contract.wage <= 10000:
        result = 137.5
    elif contract.wage < 40000:
        result = contract.wage * 0.01375
    elif contract.wage >= 40000:
        result = 550
