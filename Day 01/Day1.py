sum([int(k[0]+k[-1]) for k in [[j for j in i if j.isnumeric()] for i in input.split()]])    
