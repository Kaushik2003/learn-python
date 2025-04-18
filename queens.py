from itertools import permutations

N = 8
sol = 0
cols = range(N)

for combo in permutations(cols):  # Permutations ensure unique rows and columns
    if len(set(combo[i] + i for i in cols)) == N and len(set(combo[i] - i for i in cols)) == N:
        sol += 1
        print("Solution " + str(sol) + ": " + str(combo) + "\n")
        for i in combo:
            row = ['.'] * N
            row[i] = 'Q'
            print(" ".join(row))
        print("\n")