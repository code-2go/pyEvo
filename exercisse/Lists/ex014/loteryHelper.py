from random import sample, randint
papper = list(range(1, 61))
nSim = int(input('How many lottery simulation for the draw? '))
for cnt in range(0, nSim):
    print(f'\nSimulation {cnt+1}:')
    print(sorted(sample(card, k=6)))

papper = list(range(1, 61))
sim = []
data = []
nSim = int(input('How many lottery simulation for the draw? '))
play = 1
while play <= nSim:
    data.append(sample(papper, k=6))
    sim.append(data[:])
    data.clear()
    play += 1
for play in range(0, nSim):
    print(sim[play])

sim = []
data = []
play = 1
nSim = int(input('How many lottery simulation for the draw? ')) 
while play <= nSim:
    for cnt in range(0, 6):
        n = randint(1, 60+1)
        if n not in data:
            data.append(n)
        else:
            while n in data:
                n = randint(1, 60+1)
            data.append(n)
    data.sort()
    sim.append(data[:])
    data.clear()
    play += 1
for play in range(0, nSim):
    print(f'Play {play+1} -> {sim[play]}')

