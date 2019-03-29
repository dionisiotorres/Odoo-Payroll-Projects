# Condition
for line in payslip.input_line_ids:
    if line.code == 'MEAL':
        a = line.amount

if a > 0:
    result = True
    
# Computation
    for line in payslip.input_line_ids:
        if line.code == 'ABS':
            absday = line.amount
        if line.code == 'MEAL':
           mpd = line.amount

    result = mpd * (WORKDAY - absday)
