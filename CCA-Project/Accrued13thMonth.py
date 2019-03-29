# Condition is always True
# Computation
if contract.struct_id.name == 'Regular':
    result = BASICPAY / (365 / 7)
elif contract.struct_id.name == 'Per Piece Rate':
    result = contract.wage * 25 / (365 / 7)
