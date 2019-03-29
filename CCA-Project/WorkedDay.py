# Condition is always True
# Computation
total_workdays = 0
for line in payslip.worked_days_line_ids:
    total_workdays += line.number_of_days
result = total_workdays
