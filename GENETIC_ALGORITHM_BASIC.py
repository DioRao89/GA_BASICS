'''
intervalo para analise de raiz de polinomio
raiz entre Xmin e Xmax
f(x) = 1x^0+2x^1+3x^2-7x^3
f(4) = pol([1,2,3,-7],4)
'''
import matplotlib.pyplot as plt
import numpy as np
def AG(coef,xmax, xmin,n):
    #populacao inicial Po
    pop = np.random.uniform(xmin, xmax, 100)
    # mutacao
    # crossover
    #funcao aptidao
    vetor_resultado = pol(coef,pop) 
    print('valor', vetor_resultado)
    print('min',abs(min(vetor_resultado, key=abs)))#retorna o valor minimo absoluto
    #min 4.97378652277196
    tuples_fit = list(zip(pop,vetor_resultado))
    print('min tupla',min(tuples_fit, key= lambda x:abs(x[1])))
    # min tupla (0.49736966163298746, -4.97378652277196)
    #new_gen
    parents = []
    print(len(pop))
    for i in range(10):
        best = min(tuples_fit, key= lambda x:abs(x[1])) 
        #____________________________
        pop = np.delete(pop, np.where(pop == best[0])) #
        vetor_resultado = np.delete(vetor_resultado, np.where(vetor_resultado == best[1])) #
        tuples_fit =  list(zip(pop,vetor_resultado)) # 
        #__________________________
        parents.append(best[0])
        print(best)
    print(len(pop))
    print('parents' , parents)
#calcula o valor da funcao para um x dado
def pol(coef,x):
    y = 0
    for i,valor in enumerate(coef):
        y += valor*x**i
    return y

xmin = -100
xmax = 100

coeficientes = [-3,1.5,-10,-2] # y = -3 +1.5x
'''
vet_y = []
dx = 0.01
vet_x = list(np.arange(xmin,xmax,dx))
for i,x in enumerate(vet_x):
    vet_y.append(pol(coeficientes,x))
plt.plot(vet_x,vet_y)
plt.show()    
'''
total_pop = 100
AG(coeficientes,xmax,xmin,total_pop)
#print(vet_xmed)
plt.xlabel("iteracoes")
plt.ylabel("raiz")
plt.xkcd()
plt.show()
