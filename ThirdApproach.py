# Importing periodic table as a dictionary.
periodic_table = {
    1: ["H", "Hydrogen"],
    2: ["He", "Helium"],
    3: ["Li", "Lithium"],
    4: ["Be", "Beryllium"],
    5: ["B", "Boron"],
    6: ["C", "Carbon"],
    7: ["N", "Nitrogen"],
    8: ["O", "Oxygen"],
    9: ["F", "Fluorine"],
    10: ["Ne", "Neon"],
    11: ["Na", "Sodium"],
    12: ["Mg", "Magnesium"],
    13: ["Al", "Aluminum"],
    14: ["Si", "Silicon"],
    15: ["P", "Phosphorus"],
    16: ["S", "Sulfur"],
    17: ["Cl", "Chlorine"],
    18: ["Ar", "Argon"],
    19: ["K", "Potassium"],
    20: ["Ca", "Calcium"],
    21: ["Sc", "Scandium"],
    22: ["Ti", "Titanium"],
    23: ["V", "Vanadium"],
    24: ["Cr", "Chromium"],
    25: ["Mn", "Manganese"],
    26: ["Fe", "Iron"],
    27: ["Co", "Cobalt"],
    28: ["Ni", "Nickel"],
    29: ["Cu", "Copper"],
    30: ["Zn", "Zinc"],
    31: ["Ga", "Gallium"],
    32: ["Ge", "Germanium"],
    33: ["As", "Arsenic"],
    34: ["Se", "Selenium"],
    35: ["Br", "Bromine"],
    36: ["Kr", "Krypton"],
    37: ["Rb", "Rubidium"],
    38: ["Sr", "Strontium"],
    39: ["Y", "Yttrium"],
    40: ["Zr", "Zirconium"],
    41: ["Nb", "Niobium"],
    42: ["Mo", "Molybdenum"],
    43: ["Tc", "Technetium"],
    44: ["Ru", "Ruthenium"],
    45: ["Rh", "Rhodium"],
    46: ["Pd", "Palladium"],
    47: ["Ag", "Silver"],
    48: ["Cd", "Cadmium"],
    49: ["In", "Indium"],
    50: ["Sn", "Tin"],
    51: ["Sb", "Antimony"],
    52: ["Te", "Tellurium"],
    53: ["I", "Iodine"],
    54: ["Xe", "Xenon"],
    55: ["Cs", "Cesium"],
    56: ["Ba", "Barium"],
    57: ["La", "Lanthanum"],
    58: ["Ce", "Cerium"],
    59: ["Pr", "Praseodymium"],
    60: ["Nd", "Neodymium"],
    61: ["Pm", "Promethium"],
    62: ["Sm", "Samarium"],
    63: ["Eu", "Europium"],
    64: ["Gd", "Gadolinium"],
    65: ["Tb", "Terbium"],
    66: ["Dy", "Dysprosium"],
    67: ["Ho", "Holmium"],
    68: ["Er", "Erbium"],
    69: ["Tm", "Thulium"],
    70: ["Yb", "Ytterbium"],
    71: ["Lu", "Lutetium"],
    72: ["Hf", "Hafnium"],
    73: ["Ta", "Tantalum"],
    74: ["W", "Tungsten"],
    75: ["Re", "Rhenium"],
    76: ["Os", "Osmium"],
    77: ["Ir", "Iridium"],
    78: ["Pt", "Platinum"],
    79: ["Au", "Gold"],
    80: ["Hg", "Mercury"],
    81: ["Tl", "Thallium"],
    82: ["Pb", "Lead"],
    83: ["Bi", "Bismuth"],
    84: ["Po", "Polonium"],
    85: ["At", "Astatine"],
    86: ["Rn", "Radon"],
    87: ["Fr", "Francium"],
    88: ["Ra", "Radium"],
    89: ["Ac", "Actinium"],
    90: ["Th", "Thorium"],
    91: ["Pa", "Protactinium"],
    92: ["U", "Uranium"],
    93: ["Np", "Neptunium"],
    94: ["Pu", "Plutonium"],
    95: ["Am", "Americium"],
    96: ["Cm", "Curium"],
    97: ["Bk", "Berkelium"],
    98: ["Cf", "Californium"],
    99: ["Es", "Einsteinium"],
    100: ["Fm", "Fermium"],
    101: ["Md", "Mendelevium"],
    102: ["No", "Nobelium"],
    103: ["Lr", "Lawrencium"],
    104: ["Rf", "Rutherfordium"],
    105: ["Db", "Dubnium"],
    106: ["Sg", "Seaborgium"],
    107: ["Bh", "Bohrium"],
    108: ["Hs", "Hassium"],
    109: ["Mt", "Meitnerium"],
    110: ["Ds", "Darmstadtium"],
    111: ["Rg", "Roentgenium"],
    112: ["Cn", "Copernicium"],
    113: ["Nh", "Nihonium"],
    114: ["Fl", "Flerovium"],
    115: ["Mc", "Moscovium"],
    116: ["Lv", "Livermorium"],
    117: ["Ts", "Tennessine"],
    118: ["Og", "Oganesson"]
}

elist = list(periodic_table.values()) # A list containing symbols & names.

# code to make a list of element name
j = 0
e_symbol = []
while j < 118:
    e_symbol.append(elist[j][1])
    j = j + 1
#print(e_symbol)

# code to make a list of symbols
i = 0
pt_symbols = []
while i < 118:
    pt_symbols.append(elist[i][0])
    i = i + 1
#print(pt_symbols)
 # pt_symbols is a list with element symbols in IUPAC form.

# below code converts the double character symbols to single character symbols and returns the data in a list.
sc_symbol = list()
i_number = 0
for x in pt_symbols:
    if len(x)>1:
        sc_symbol.append(x[-2:-1])
        i_number = i_number + 1
    else:
        sc_symbol.append(x)
        i_number = i_number + 1

#print(sc_symbol)
at_number = []
an = 1
while an <=118:
    at_number.append(an)
    an = an + 1

#print(at_number)

import pandas as pd
df = pd.DataFrame(list(zip(at_number,pt_symbols,sc_symbol,e_symbol)))
df.columns = ['Atomic Number','Symbol','sc_Symbol','Element Name']#Generated a dataframe with 3 columns

#print(df)

import time
#Taking input from user
print("Please enter your first name here") 
name = input()
uc_name = name.upper()
if "J" in uc_name:
    print("Sorry, even Mendeleev could not solve this predictment, there is no element with J symbol")
    time.sleep(5)
    exit()
elif "Q" in uc_name:
    print("Sorry, even Mendeleev could not solve this predictment, there is no element with Q symbol")
    time.sleep(5)
    exit()
elif uc_name.isalpha() == False:
    print("Don't be a smartass, you have been warned!!")
    time.sleep(5)
    exit()
else: 
    print("You have entered your first name as",name.upper())

length= len(uc_name)
i = 0

while i <= (length-1):
    if uc_name[i] in pt_symbols:
        j = pt_symbols.index(uc_name[i])
        print("Use the element", df['Element Name'][j],df['Symbol'][j], "with atomic number", df['Atomic Number'][j])
    elif uc_name[i] in sc_symbol:
        k = sc_symbol.index(uc_name[i])
        print("Use the element", df['Element Name'][k],df['Symbol'][k], "with atomic number", df['Atomic Number'][k])
    i = i + 1
