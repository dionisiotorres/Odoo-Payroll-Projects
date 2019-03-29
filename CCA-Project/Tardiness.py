# Condition
result = False
if payslip.input_line_ids:
 for line in payslip.input_line_ids:
   if line.code == 'TARD':
         result = True
         break
         
 # Computation
 if result:
    result = 0
    minutes_late = 0
    for line in payslip.input_line_ids:
      if line.code == 'TARD':
        minutes_late += line.amount
    result = 0 - contract.wage / 10 / 60 * minutes_late
