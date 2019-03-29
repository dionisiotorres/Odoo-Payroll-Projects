# Condition
datef = int(str(payslip.date_from)[-2:])
datet = int(str(payslip.date_to)[-2:])

result = False
for reg in employee.payroll_contribution_reg_ids:
	if reg.contract_id and reg.contract_id.id != contract.id:
		continue
	if reg.type_id.code == 'SSSL' and reg.valid_for_sal_rule(payslip.date_from, payslip.date_to, 15) and datet == 15:
                result = True
		break

# Computation
if result:
    result = 0
    payroll_contribution_reg = False
    for reg in employee.payroll_contribution_reg_ids:
        if reg.contract_id and reg.contract_id.id != contract.id:
            continue
            
        if reg.type_id.code == 'SSSL':
            payroll_contribution_reg = reg
            break
            
    if payroll_contribution_reg:
        result = payroll_contribution_reg.contribution_base/payroll_contribution_reg.x_period_of_contribution / 2
