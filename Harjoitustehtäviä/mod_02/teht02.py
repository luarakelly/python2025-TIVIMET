# Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

# ---

import math

# user input variables
ympyrän_säde = float(input("Anna ympuran säde:"))
pinta_ala = math.pi * ympyrän_säde ** 2 # ala formula => A = π * r²

# output
# :.2f => format as a floating-point number and round to 2 decimal places
# :0.2f 2 decimals| :.0f => no decimals
print(f"Ympyran pinta-ala, jonka säde on {ympyrän_säde}: {pinta_ala:.2f}")