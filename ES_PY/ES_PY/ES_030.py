"""Utilizza il modulo random per simulare una partita a dadi tra Alice e Bob."""
import random
alice = random.randint(1,6)
bob = random.randint(1,6)
if alice > bob:
    print(f"Il vincitore è alice con un tiro da {alice}")
else: print(f"Il vincitore è bob con un tiro da {bob}")


