from builtins import len, sorted, int

import copy

from Classes import *

# Creating minefield

minefield = MineField(45, 45)

minefield.add_mine(2, 5, 5)
minefield.add_mine(3, 10, 7)
minefield.add_mine(5, 15, 4)
minefield.add_mine(3, 3, 20)
minefield.add_mine(5, 17, 15)
minefield.add_mine(4, 10, 10)
minefield.add_mine(2, 15, 20)
minefield.add_mine(3, 2, 20)
minefield.add_mine(3, 35, 25)
minefield.add_mine(6, 36, 32)
minefield.add_mine(5, 8, 30)
minefield.add_mine(6, 30, 6)
minefield.add_mine(5, 23, 29)

# setting parameters
reached_end = False
generation_counter = 1
individuals_per_generation = 70
genes_per_generation = 90

# Creating the initial population
population = []
for i in range(individuals_per_generation):
    genes = random_genes(genes_per_generation)
    new_individual = Individual(genes)
    population.append(new_individual)

# beginning loop
while not reached_end:

    distance_dict = {}

    rows = individuals_per_generation

    population_copy = copy.copy(population)

    column = 0

    # processing generation's moves
    while column <= genes_per_generation - 1:

        row = 0
        while row < rows:

            individual = population[row]
            genes = individual.get_genes()

            # choosing list of directions where 1 = forward, 2 = up, 3 = down, 4 = North-east, 5 = South-east
            if genes[column] == 1:
                individual.set_position_x(individual.get_position_x() + 1)

            elif genes[column] == 2:
                individual.set_position_y(individual.get_position_y() - 1)

            elif genes[column] == 3:
                individual.set_position_y(individual.get_position_y() + 1)

            elif genes[column] == 4:
                individual.set_position_y(individual.get_position_y() - 1)
                individual.set_position_x(individual.get_position_x() + 1)

            elif genes[column] == 5:
                individual.set_position_y(individual.get_position_y() + 1)
                individual.set_position_x(individual.get_position_x() + 1)

            try:
                if minefield.minefield[individual.get_position_y()][individual.get_position_x()] == 'X':
                    distance_dict[str(population_copy.index(individual))] = find_distance(minefield.get_exit_x(),
                                                                                          minefield.get_exit_y(),
                                                                                          individual.get_position_x(),
                                                                                          individual.get_position_y())
                    population.remove(individual)
                    rows -= 1
                    row -= 1
                elif individual.get_position_y() == minefield.get_exit_y() and individual.get_position_x() \
                        == minefield.get_exit_x() - 1:
                    reached_end = True
                    print('Number of generations: ' + str(generation_counter))
                    print('SUCCESS')
                    break

                else:
                    minefield.minefield[individual.get_position_y()][individual.get_position_x()] = '0'
            except IndexError:
                distance_dict[str(population_copy.index(individual))] = find_distance(minefield.get_exit_x(),
                                                                                      minefield.get_exit_y(),
                                                                                      individual.get_position_x(),
                                                                                      individual.get_position_y())
                population.remove(individual)
                rows -= 1
                row -= 1

            row += 1

        column += 1

        print(len(population))
        print(len(distance_dict))

        if reached_end:
            break

        if len(distance_dict) >= individuals_per_generation:
            break

        print()
        print()
        print()
        print()

        minefield.print()
        minefield.remove_zeros()
        print('Generation number: ' + str(generation_counter))

    if reached_end:
        break

    sort_distances = sorted(distance_dict.items(), key=lambda item: item[1])

    fittest_individuals = []
    for i in range(individuals_per_generation // 2):
        fittest_individuals.append(population_copy[int(sort_distances[i][0])])

    print(len(fittest_individuals))

    new_population = []

    while len(new_population) != individuals_per_generation:
        new_population.append(mate(fittest_individuals[random.randrange(0, len(fittest_individuals))],
                                   fittest_individuals[random.randrange(0, len(fittest_individuals))],
                                   genes_per_generation))

    population = new_population[:]

    generation_counter += 1
    print('NEW GENERATION')
