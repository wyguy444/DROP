import random
from fitness import determine_fitness


class GeneticAlgorithm:
    def __init__(self, ride_dict, travel_times):
        self.ride_dict = ride_dict
        self.travel_times = travel_times

    def determine_optimal_route(self, ride_choices):
        population = self.generate_population(ride_choices)
        for i in range(50):
            population = self.sort_by_fitness(population)
            mating_pool = self.generate_mating_pool(population)
            population = self.breed_next_generation(mating_pool)
            population = self.randomly_mutate(population)
        population = self.sort_by_fitness(population)
        return(
            population[0],
            round(determine_fitness(population[0], self.ride_dict, self.travel_times), 2)
        )


    def generate_population(self, ride_choices):
        population = []
        for i in range(100):
            ride_id_list = list(ride_choices.keys())
            random.shuffle(ride_id_list)
            population.append(ride_id_list)
        return population


    def sort_by_fitness(self, population):
        population.sort(key=lambda route: determine_fitness(route, self.ride_dict, self.travel_times))
        return population


    def generate_mating_pool(self, population):
        return population[:50]


    def breed_next_generation(self, mating_pool):
        mating_pairs = self.generate_mating_pairs(mating_pool)
        return(self.mate(mating_pairs))


    def randomly_mutate(self, population):
        mutation_rate = 0.05
        for route in population:
            if random.random() < mutation_rate:
                random_index_1 = random.randrange(len(route))
                random_index_2 = random.randrange(len(route))
                value_1 = route[random_index_1]
                value_2 = route[random_index_2]
                route[random_index_1] = value_2
                route[random_index_2] = value_1
        return population


    def generate_mating_pairs(self, mating_pool):
        pairs = []
        for i in range(100):
            pairs.append(random.choices(mating_pool, weights=[50-j for j in range(50)], k=2))
        return pairs


    def mate(self, mating_pairs):
        population = []
        for pair in mating_pairs:
            child = []
            childP1 = []
            childP2 = []
            parent1 = pair[0]
            parent2 = pair[1]
            
            geneA = int(random.random() * len(parent1))
            geneB = int(random.random() * len(parent1))
            
            startGene = min(geneA, geneB)
            endGene = max(geneA, geneB)

            for i in range(startGene, endGene):
                childP1.append(parent1[i])
                
            childP2 = [item for item in parent2 if item not in childP1]

            child = childP1 + childP2
            population.append(child)
        return population