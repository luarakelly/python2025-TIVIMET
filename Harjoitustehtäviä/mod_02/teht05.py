# Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. 
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#    Yksi leiviskä on 20 naulaa.
#    Yksi naula on 32 luotia.
#    Yksi luoti on 13,3 grammaa.

# Esimerkki ohjelman toiminnasta:
#Anna leiviskät: 3
#Anna naulat: 9
#Anna luodit: 13.5
#Massa nykymittojen mukaan: 29 kilogrammaa ja 545.95 grammaa. 

# ---

# user input variables
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# constants 
LUOTI_GRAMMA = 13.3
NAULA_GRAMMA = 32 * LUOTI_GRAMMA
LEIVISKÄ_GRAMMA =  20 * NAULA_GRAMMA

# calculations
leiviskat_g = leiviskat * LEIVISKÄ_GRAMMA
naulat_g = naulat * NAULA_GRAMMA
luodit_g = luodit * LUOTI_GRAMMA

kilogrammat = float((leiviskat_g + naulat_g + luodit_g) // 1000)  # full kilograms
grammat = float((leiviskat_g + naulat_g + luodit_g) % 1000)  # remaining grams

# output
print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")