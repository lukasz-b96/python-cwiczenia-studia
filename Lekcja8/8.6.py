import time

def fun_rek(i, j):
    if i < 0 or j < 0:
        raise("niepoprawne dane")
    
    if i == 0 and j == 0:
        return 0.5
    if j == 0:
        return 0.0
    if i == 0:
        return 1.0
    
    return 0.5 * (fun_rek(i-1,j) + fun_rek(i, j-1))



class Solver:
    
    def __init__(self):
        self.dictionary = {}

    def fun_dyn(self, i, j):
        if i < 0 or j < 0:
            raise("niepoprawne dane")
        
        if i == 0 and j == 0:
            return 0.5
        if j == 0:
            return 0.0
        if i == 0:
            return 1.0
        
        if (i,j) in self.dictionary:
            return self.dictionary[(i,j)]
        
        self.dictionary[(i,j)] = 0.5 * (self.fun_dyn(i-1,j) + self.fun_dyn(i, j-1))
        return self.dictionary[(i,j)] 

solver = Solver()

start = time.time()
print(solver.fun_dyn(18,10))
end = time.time()
print("Dynamicznie:", end-start)

start = time.time()
print(fun_rek(18,10))
end = time.time()
print("Rekurencyjnie:", end-start)


