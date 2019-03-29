# Condition
if payslip.credit_note:
    result = True
    
# Computation
if result:
    base = contract.wage * 25
    if base <= 10000:
        result = 137.5
    elif base < 40000:
        result = base * 0.01375
    elif base >= 40000:
        result = 550
