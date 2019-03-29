result = False
if payslip.input_line_ids:
    for line in payslip.input_line_ids:
        if line.code == 'TARD' or line.code == 'UNDT' and line.amount:
            result = True

if result:
    minutes_late = 0
    for line in payslip.input_line_ids:
        if line.code == 'TARD':
            minutes_late += line.amount
        elif line.code == 'UNDT':
            minutes_late += line.amount

result = 0 - contract.wage * 12 / 261 / 8 / 60 * minutes_late
