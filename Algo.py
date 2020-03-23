def main(data):
    N_risp = len(data[0][1])
    N_user = len(data)
    comp = []

    for u in range(N_user -1, 0, -1):
        percentuale = 0
        if abs(data[u][0][3] - data[N_user -1][0][3]) <= 1: 
            for n in range(0,N_risp):
                percentuale += (N_risp-1)-abs(data[N_user-1][1][n]-data[u -1][1][n])/N_risp
        if percentuale >= 0.9:
            comp.append([data[N_user-1][0][0], data[u -1][0][0], percentuale])

    return comp