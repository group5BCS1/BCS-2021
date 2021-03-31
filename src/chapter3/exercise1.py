# this program finds the gross pay
hours = int(input('Enter hours:'))
rate_per_hour = float(input('Enter rate:'))
if hours>40:
            gross_pay = 40*(rate_per_hour)+(((hours-40)* 1.5))*rate_per_hour
else:
            gross_pay = hours * rate_per_hour
print('The gross pay is:', gross_pay)