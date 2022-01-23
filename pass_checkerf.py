
def passStrength(password, Stats):
    num = round((Stats(password).strength()*100))
    if num != 0: dec = round((Stats(password).strength()*100) % num, 3)
    else: dec = round((Stats(password).strength()*100), 3)
    return 100 if num == 99 and dec > 0.99 else 0 if num == 0 and dec < 0.01 else num
