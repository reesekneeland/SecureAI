from string import punctuation 

def passStrength(password, Stats):
    stat = Stats(password).strength()
    for c in password:
        if c in "".join(set(punctuation)):
            stat += (stat * .1)
     
    num = round(stat*100)
    if num != 0: dec = round((stat*100) % num, 3)
    else: dec = round((stat*100), 3)
    return 100 if num >= 99 and dec > 0.99 else 0 if num == 0 and dec < 0.01 else num