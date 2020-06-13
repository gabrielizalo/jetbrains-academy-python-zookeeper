atoms_ini = int(input())
atoms_end = int(input())
HALF_LIFE = 12
periods = 0
atoms_process = atoms_ini
while atoms_process > atoms_end:
    periods += 1
    atoms_process = atoms_process / 2
print(periods * HALF_LIFE)
