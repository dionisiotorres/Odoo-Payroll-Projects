# Condition
if payslip.credit_note:
    result = True
    
# Computation
if result:
    base = contract.wage * 25
    max = 15750; maxss = 581.30
    ranges = [[0, 1000, 0],
        [1000, 1250, 36.3],
        [1250, 1750, 54.5],
        [1750, 2250, 72.7],
        [2250, 2750, 90.8],
        [2750, 3250, 109],
        [3250, 3750, 127.2],
        [3750, 4250, 145.3],
        [4250, 4750, 163.5],
        [4750, 5250, 181.7],
        [5250, 5750, 199.8],
        [5750, 6250, 218],
        [6250, 6750, 236.2],
        [6750, 7250, 254.3],
        [7250, 7750, 272.5],
        [7750, 8250, 290.7],
        [8250, 8750, 308.8],
        [8750, 9250, 327],
        [9250, 9750, 345.2],
        [9750, 10250, 363.3],
        [10250, 10750, 381.5],
        [10750, 11250, 399.7],
        [11250, 11750, 417.8],
        [11750, 12250, 436],
        [12250, 12750, 454.2],
        [12750, 13250, 472.3],
        [13250, 13750, 490.5],
        [13750, 14250, 508.7],
        [14250, 14750, 526.8],
        [14750, 15250, 545],
        [15250, 15750, 563.2]]
    result = 0
    for r in ranges:
        if all([ base > r[0], base < r[1]]):
            result = r[2]
            break
    if base > max:
        result = maxss
