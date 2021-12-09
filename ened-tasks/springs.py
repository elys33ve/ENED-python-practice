#Hooke's law for springs but as a function

def Springs (K1, K2, Ftotal, config):
    lSeries = ['series','s','Series']
    lParall = ['Parallel','p','parallel']
    if K1 > 0 and K2 > 0 and Ftotal > 0:
        pass
    else:
        print("Invalid input for K1, K2, and/or Ftotal")
    if config in lSeries:
        Keq = 1/(1/(K1 + K2))
        F1 = Ftotal
        F2 = Ftotal
        x1 = F1/K1
        x2 = F2/K2
        xtotal = x1 + x2
        return Keq, F1, F2, x1, x2, xtotal
    elif config in lParall:
        Keq = K1 + K2
        xtotal = Ftotal/Keq
        x1 = xtotal
        x2 = xtotal
        F1 = K1*x1
        F2 = K2*x2
        return Keq, F1, F2, x1, x2, xtotal
    else:
        print("Invalid input for configuration")
