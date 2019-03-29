# Condition
datef = int(str(payslip.date_from)[-2:])
datet = int(str(payslip.date_to)[-2:])
month = int(str(payslip.date_to)[5:7])

for line in payslip.input_line_ids:
    if line.code == 'MRA' and datet >= 28 and line.amount and contract.x_medical_reimbursement:
        result = True
        
# Computation
if result:
    for line in payslip.input_line_ids:
        if line.code == 'MRA':
            result = line.amount
