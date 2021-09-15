import random
from fitness import Fitness


class GeneticAlgorithm:
    def __init__(self, ride_dict, travel_times):
        self.ride_dict = ride_dict
        self.travel_times = travel_times
        self.fitness = Fitness(ride_dict, travel_times)

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
            self.fitness.get_full_route_stats(population[0])
        )


    def generate_population(self, ride_choices):
        population = []
        for i in range(100):
            ride_id_list = ride_choices.copy()
            random.shuffle(ride_id_list)
            population.append(ride_id_list)
        return population


    def sort_by_fitness(self, population):
        population.sort(key=lambda route: self.fitness.determine_fitness(route))
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
            parent1 = pair[0].copy()
            parent2 = pair[1].copy()
            
            geneA = 0
            geneB = int(random.random() * len(parent1))
            
            startGene = min(geneA, geneB)
            endGene = max(geneA, geneB)

            for i in range(startGene, endGene):
                childP1.append(parent1[i])
            
            for item in childP1:
                parent2.remove(item)
            childP2 = parent2

            child = childP1 + childP2
            population.append(child.copy())
        return population
