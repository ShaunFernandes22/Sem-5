import random
gene = ['01101', '11000', '01000', '10011']

def selection(gene):
    x = []
    for i in gene:
        x.append(int(i, 2))
    
    fx = []
    for i in x:
        fx.append(i*i)
    
    fx_sum = sum(fx)
    fx_avg = round(fx_sum/4, 2)

    expected_count = []
    for i in fx:
        expected_count.append(round((i/fx_avg), 4))
        
    actual_count = []
    for i in expected_count:
        actual_count.append(round(i))

    mate_pool = []
    for (i, j) in zip(actual_count, gene):
        if i:
            for _ in range(i):
                mate_pool.append(j)

    return  x, fx, fx_sum, fx_avg, expected_count, actual_count, mate_pool

def generate_mate(size, mate_element_size):
    if size %2 != 0:
        return None
    available_positions = list(range(size))
    random.shuffle(available_positions)
    mate = [-1] * size
    for i in range(size):
        if mate[i] == -1:
            j = random.choice(available_positions)
            while mate[j] != -1 or i == j:
                j = random.choice(available_positions)
            mate[i] = j
            mate[j] = i
            available_positions.remove(i)
            available_positions.remove(j)

    crossover = [-1] * size
    for i in mate:
        if crossover.count(-1) != 0:
            crossover[i] = crossover[mate[i]] = random.randint(1, mate_element_size-1)
    return mate , crossover

def crossover(mate_pool):
    # mate, crossover_points = generate_mate(len(mate_pool), len(mate_pool[0]))
    mate, crossover_points = [3, 2, 1, 0], [2, 3, 3, 2]
    new_population = [-1] * len(mate_pool)
    for i in mate:
        new_population[i] = mate_pool[i][:crossover_points[i]] + mate_pool[mate[i]][crossover_points[i]:]
    
    x=[]
    for i in new_population:
        x.append(int(i, 2))
    fx = []
    for i in x:
        fx.append(i * i)
    
    return mate_pool, new_population, mate, crossover_points, x, fx

def mutation(new_population, mutation_gene):
    mutated_population = []
    for individual in new_population:
        mutated_individual = ''.join([str(int(bit) ^ int(m_bit)) for bit, m_bit in zip(individual, mutation_gene)])
        mutated_population.append(mutated_individual)

    x=[]
    for i in mutated_population:
        x.append(int(i, 2))
    fx = []
    for i in x:
        fx.append(i * i)

    return mutated_population, x, fx

def GA(gene, itr, generation):
    if itr == 0:
        return
    x, fx, fx_sum, fx_avg, expected_count, actual_count, mate_pool = selection(gene)
    if (sum(actual_count) != len(gene)):
        print("Error !")
        return 
    print(f"--------------------------------------------Generation {generation}---------------------------------------------")
    print("Initial population \tX \tX^2\tExpected Count\tActual Count")
    for i in range(len(gene)):
        print(f" {gene[i]}\t\t\t{x[i]}\t{fx[i]}\t  {expected_count[i]}\t\t{actual_count[i]}")
    
    print(f"\nSum : {fx_sum} \t Average : {fx_avg} \t Maximum : {max(fx)}")
    print("-------------------------------------------------------------------------------------------------------")


    mate_pool, new_population, mate, crossover_points, x, fx = crossover(mate_pool)
   
    print(f"\n--------------------------------------- New Population {generation} ------------------------------------------")
    print("Mate Pool\tMate\t\tCrossover Points\tNew Population\tX value\t\tf(x)")
    for i in range(len(gene)):
        print(f" {mate_pool[i]}\t\t {mate[i]}\t\t\t{crossover_points[i]}\t\t{new_population[i]} \t\t{x[i]}\t\t{fx[i]}")
    print(f"Sum : {fx_sum} \t Average : {fx_avg} \t Maximum : {max(fx)}")
    print(f"------------------------------------------------------------------------------------------------------")

    mutation_gene = "01011"
    mutated_population , x, fx = mutation(new_population, mutation_gene)

    print(f"\n------------------------------------ Mutated Population {generation} ------------------------------------------")
    print("After Crossover  Mutation gene  Mutated Population\t X value\tf(x)")
    for i in range(len(gene)):
        print(f" {new_population[i]} \t\t\t{mutation_gene}\t\t {mutated_population[i]}\t\t  {x[i]}\t\t{fx[i]}")
    print(f"Sum : {fx_sum} \t Average : {fx_avg} \t Maximum : {max(fx)}")
    print(f"-------------------------------------------------------------------------------------------------------")
    GA(gene, itr-1, generation+1)
    return

GA(gene, 3, 0)
