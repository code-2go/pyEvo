#Em uma pizzaria, cada tulipa de chopp custa R$ 0,80 e uma pizza mista grande custa R$10,00 mais R$1,50 por tipo de cobertura pedida (queijo, presunto, banana, etc.). Uma turma vai à pizzaria e pede uma determinada quantidade de "chopps" e uma pizza grande com  uma determinada quantidade de coberturas. faça um algoritmo que calcule e conta e, sabendo quantas pessoas estão à mesa, quanto que cada um deve pagar (não esqueça os 10% do garçom). 

beer = 0.8
pizza = 10
topping = 1.5
nPeople = int(input('A table for how many? '))
nBeer = int(input('How many beers do you want? '))
nPizza = int(input('How many pizza you will want? '))
nTopping = int(input('Add extra topping? How many types? '))
total = float(((nPizza*pizza) + (nBeer*beer) + (nTopping+topping))*1.1)
print('A table bill: \n {} Pizza(s) - ${} \n {} Toppin(s) - ${} \n {} Beer - ${} \n --- --- \n Total - ${} \n Total per person - $ {:.2f}'.format(nPizza, nPizza*pizza, nTopping, nTopping*topping, nBeer, nBeer*beer, total, total/nPeople))
