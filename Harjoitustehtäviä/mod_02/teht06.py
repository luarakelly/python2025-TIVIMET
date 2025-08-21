# Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#        kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#        nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

#Vihje: tutustu random.randint()-funktion käyttöön.

# ---
import random

# Generate a three-digit code with digits from 0 to 9
kolme_numeroinen_koodi = ""
for _ in range(3): #In Python, _ is a throwaway variable — it's used when you don’t need the loop variable.
    kolme_numeroinen_koodi += str(random.randint(0, 9))

# Generate a four-digit code with digits from 1 to 6
neljä_numeroinen_koodi = ""
for _ in range(4):
    neljä_numeroinen_koodi += str(random.randint(1, 6))

# Output the generated codes
# Note: The codes are generated randomly each time the program is run.
print(f"Kolmenumeroinen koodi: {kolme_numeroinen_koodi}")
print(f"Neljänumeroinen koodi: {neljä_numeroinen_koodi}")

