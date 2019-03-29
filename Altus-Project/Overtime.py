# Condition
result = contract and payslip.payslip_ot_line_ids and len(payslip.payslip_ot_line_ids) > 0


# Computation
if result:
    total_hours = sum(line.number_of_hours for line in payslip.worked_days_line_ids)
    hour_cost = contract.wage * 12 / 261 / 8

    amount = 0.0
    for line in payslip.payslip_ot_line_ids:
      if payslip.contract_id:
        amount += hour_cost * line.number_of_hours * line.rate / 100
    result = amount
