__author__ = 'Rodrigo'

def computepay():
    hours = input('Hours : ')
    rate = input('Rate : ')
    hours2 = float(hours)
    rate2 = float(rate)
    if hours2 <= 40:
        return(hours2*rate2)
    else:
        return((40*rate2)+((hours2-40)*1.5*rate2))

print(computepay())