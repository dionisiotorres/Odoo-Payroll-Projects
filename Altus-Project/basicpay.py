month31 = [1, 3, 5, 7, 8, 10, 12]
month30 = [4, 6, 9, 11]
month = int(str(payslip.date_from)[5:7])
if month in month31:
    days = 31
elif month in month30:
    days = 30
else:
    if int(str(payslip.date_from)[0:4]) % 4 == 0:
        days = 29
    else:
        days = 28

datef = int(str(payslip.date_from)[-2:])
datet = int(str(payslip.date_to)[-2:])
dated = datet - datef + 1           #days from date_from to date_to

if contract.schedule_pay == 'monthly':
    result = contract.wage * dated / days
elif contract.schedule_pay == 'quarterly':
    result = contract.wage * 3
elif contract.schedule_pay == 'semi-annually':
    result = contract.wage * 6
elif contract.schedule_pay == 'annually':
    result = contract.wage * 12
elif contract.schedule_pay == 'weekly':
    result = contract.wage / days * dated
elif contract.schedule_pay == 'bi-weekly':
    result = contract.wage / days * dated
elif contract.schedule_pay == 'bi-monthly':
    if datef == 16 and days == 31 or days == 29:
        dayd = 1 + (days - 1) / 2
        result = (contract.wage * dated) / dayd /2
    elif datef <= 15:
        result = (contract.wage * dated) / 15 / 2
    elif datef >= 16 and days == 30:
        result = (contract.wage * dated) / 15 / 2
    elif datef >= 16 and days == 28:
        result = (contract.wage * dated) / 13 / 2
