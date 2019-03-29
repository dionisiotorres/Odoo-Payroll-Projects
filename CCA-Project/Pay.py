# Condition is always True
# Computation
result = 0
for line in payslip.input_line_ids:
    if line.code == 'x5': #rate=.06
        result += line.amount * .06 * 5
    elif line.code == 'x10':
        result += line.amount * .06 * 10
    elif line.code == 'x50':
        result += line.amount * .06 * 50
    elif line.code == 'CRSBx5': #rate=0.02
        result += line.amount * .02 * 5
    elif line.code == 'CRSJAR': #rate=0.8
        result += line.amount * .8
    elif line.code == 'CHN': #rate=2.16
        result += line.amount * 2.16
    elif line.code == 'CHNSJAR': #rate=0.8
        result += line.amount * .8
    elif line.code == 'BJAR': #rate=1.2
        result += line.amount * 1.2
    elif line.code == 'CRB': #rate=8.32
        result += line.amount * 8.32
    elif line.code == 'GB': #rate=0.8
        result += line.amount * 0.8
    elif line.code == 'CC': #rate=.8
        result += line.amount * 0.8
    elif line.code == 'CRF': #rate=1.44
        result += line.amount * 1.44
