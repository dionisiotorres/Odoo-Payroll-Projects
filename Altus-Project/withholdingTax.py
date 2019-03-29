# Condition is always True
# Computation
tax_base = 0
if contract.wage <= 13093.84:
    result = 0
elif contract.wage > 13093.84:
    tax_base = categories.GROSS - categories.ALWNOTAX
if tax_base <= 20833:
    result = 0
elif tax_base > 20833 and tax_base <= 33333:
    result = 0.2 * ( tax_base - 20833)
elif tax_base > 33333 and tax_base <= 66667:
    result = 2500 + 0.25 * (tax_base - 33333)
elif tax_base > 66667 and tax_base <= 166667:
    result = 10333.33 + 0.3 * (tax_base - 66667)
elif tax_base > 166667 and tax_base <= 666667:
    result = 40833.33 + 0.32 * (tax_base - 166667)
elif tax_base > 666667:
    result = 200833.33 + 0.35 * (tax_base - 666667)
else:
    result = 0

for line in payslip.input_line_ids:
    if line.code == 'ANNUALISATION':
        annualised = line.amount

if annualised != 0:
    result = annualised
