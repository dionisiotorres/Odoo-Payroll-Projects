# Condition
if payslip.credit_note:
    result = True
    
# Computation
if result:
    base = contract.wage * 25
    max = 15750; maxss = 1178.7
    ranges = [[0, 1000, 0],
            [1000, 1250, 73.7],
            [1250, 1750, 110.50],
            [1750, 2250, 147.30],
            [2250, 2750, 184.2],
            [2750, 3250, 221],
            [3250, 3750, 257],
            [3750, 4250, 294.7],
            [4250, 4750, 331.5],
            [4750, 5250, 368.3],
            [5250, 5750, 405.2],
            [5750, 6250, 442],
            [6250, 6750, 478.8],
            [6750, 7250, 515.7],
            [7250, 7750, 552.5],
            [7750, 8250, 589.3],
            [8250, 8750, 626.2],
            [8750, 9250, 663],
            [9250, 9750, 699.8],
            [9750, 10250, 736.7],
            [10250, 10750, 773.5],
            [10750, 11250, 810.3],
            [11250, 11750, 847.2],
            [11750, 12250, 884],
            [12250, 12750, 920.8],
            [12750, 13250, 957.7],
            [13250, 13750, 994.5],
            [13750, 14250, 1031.3],
            [14250, 14750, 1068.20],
            [14750, 15250, 1105],
            [15250, 15750, 1141.80]]
    result = 0
    for r in ranges:
        if all([ base > r[0], base < r[1]]):
            result = r[2] + 10
            break
    if base > max:
        result = maxss + 10
