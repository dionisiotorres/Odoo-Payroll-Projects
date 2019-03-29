# Condition
if payslip.payslip_ot_line_ids:
    result = True
   
# Computation
if result:
    result = 0
    hour_cost = contract.wage * 12 / 261 / 8
    for line in payslip.payslip_ot_line_ids:
        if line.code == 'OT1822':
            result = line.number_of_hours * hour_cost * 0.10
