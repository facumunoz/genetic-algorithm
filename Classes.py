from builtins import object

import random
from math import *


list_moves = [1, 2, 3, 4, 5]


class MineField(object):
    def __init__(self, height_y, width_x):
        self.height_y = height_y
        self.width_x = width_x
        self.exit_x = width_x
        self.exit_y = 8
        self.minefield = []
        for i in range(height_y):
            self.minefield.append([' ']*width_x)
        self.minefield[self.exit_y][self.exit_x-1] = 'E'

    def get_exit_x(self):
        return self.exit_x

    def get_exit_y(self):
        return self.exit_y

    def print(self):
        for i in range(self.height_y):
            print(self.minefield[i])

    def add_mine(self, size, left_top_anchor_row, left_top_anchor_column):
        for row in range(left_top_anchor_row, left_top_anchor_row+size):
            for col in range(left_top_anchor_column, left_top_anchor_column+size):
                self.minefield[row][col] = 'X'

    def remove_zeros(self):
        for row in range(self.width_x):
            for col in range(self.height_y):
                if self.minefield[row][col] == '0':
                    self.minefield[row][col] = ' '


class Individual(object):
    def __init__(self, genes):
        self.genes = genes
        self.position_x = 0
        self.position_y = 10

    def get_genes(self):

        """
        Obtain individual's current list of genes
        :return: self.genes
        """
        genes_return = self.genes[:]
        return genes_return

    def get_position_x(self):
        return self.position_x

    def get_position_y(self):
        return self.position_y

    def set_position_x(self, position_x):
        self.position_x = position_x

    def set_position_y(self, position_y):
        self.position_y = position_y

    def mutate(self):
        for i in range(len(self.genes)):
            list_probability = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
            if random.choice(list_probability) == 1:
                new_gene = random.choice(list_moves)
                while new_gene == self.genes[i]:
                    new_gene = random.choice(list_moves)
                self.genes[i] = new_gene


def mate(individual1, individual2, number_of_genes):
    crossover_point = random.randrange(1, number_of_genes, 1)
    genes = []
    for i in range(0, crossover_point):
        genes.append(individual1.get_genes()[i])
    for i in range(crossover_point, number_of_genes):
        genes.append(individual2.get_genes()[i])
    return Individual(genes)


def random_genes(amount_of_genes):
    genes = []
    for i in range(amount_of_genes):
        # choosing list of directions where 1 = forward, 2 = up, 3 = down, 4 = North-east, 5 = South-east
        genes.append(random.choice(list_moves))
    return genes


def find_distance(x1, y1, x2, y2):
    inside = ((x2 - x1)**2) + ((y2 - y1)**2)
    return sqrt(inside)







