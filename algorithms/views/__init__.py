class ViewQueens(object):
    def __init__(self, *args, **kwargs):
        pass

    @property
    def show_chromosomes(self):
        bg_black = lambda text: f"\x1b[0;37;40m{text}\x1b[0m"
        bg_white = lambda text: f"\x1b[0;30;47m{text}\x1b[0m"
        fg_black = lambda text: f"\x1b[0;37;40m{text}\x1b[0m"
        fg_white = lambda text: f"\x1b[0;30;47m{text}\x1b[0m"

        _matrix = []

        if self.k < 41:
            for i, _ in enumerate(range(self.k)):
                temp = []
                for j, _ in enumerate(range(self.k)):
                    if (i + j) % 2 == 0:
                        temp.append(bg_black("   "))
                    else:
                        temp.append(bg_white("   "))
                _matrix.append(temp)

            for ind, chromosome in enumerate(self.chromosomes):
                clone_m = [[n for n in m] for m in _matrix]

                for col, row in enumerate(chromosome):
                    if (col + row) % 2 == 0:
                        clone_m[row][col] = fg_black(" \u265B ")
                    else:
                        clone_m[row][col] = fg_white(" \u2655 ")

                print(f"Individual: {ind}")
                for m in clone_m:
                    print("".join(m))
                print(end="\n")
        else:
            print("Show chromosomes for (k < 41)")

        print(f"Population: {len(self.chromosomes)}\nK: {self.k}")

    @property
    def show_chromosomes_fitness(self):
        bg_black = lambda text: f"\x1b[0;37;40m{text}\x1b[0m"
        bg_white = lambda text: f"\x1b[0;30;47m{text}\x1b[0m"
        fg_black = lambda text: f"\x1b[0;37;40m{text}\x1b[0m"
        fg_white = lambda text: f"\x1b[0;30;47m{text}\x1b[0m"

        _matrix = []

        if self.k < 41:
            for i, _ in enumerate(range(self.k)):
                temp = []
                for j, _ in enumerate(range(self.k)):
                    if (i + j) % 2 == 0:
                        temp.append(bg_black("   "))
                    else:
                        temp.append(bg_white("   "))
                _matrix.append(temp)

            for chromosome, chromo_fitness in self.fitness:
                clone_m = [[n for n in m] for m in _matrix]

                for col, row in enumerate(chromosome):
                    if (col + row) % 2 == 0:
                        clone_m[row][col] = fg_black(" \u265B ")
                    else:
                        clone_m[row][col] = fg_white(" \u2655 ")

                print(f"Fitness: {chromo_fitness}")
                for m in clone_m:
                    print("".join(m))
                print(end="\n")
        else:
            print("Show chromosomes for (k < 41)")

        print(f"Population: {len(self.chromosomes)}\nK: {self.k}")

    @property
    def show_best_five_individuals(self):
        individuals = sorted(self._memoize_fitness.items(), key=lambda x: x[1])

        print("\nShow 5 best individuals\n")

        for n, individual in enumerate(individuals):
            if n < 5:
                print(individual)

            else:
                break

        print(f"\nChecked Individuals: {len(individuals)}")
