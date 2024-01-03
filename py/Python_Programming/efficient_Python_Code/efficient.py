

# %load_ext line_profiler
# %lprun -f funct_name funct_name(_)

primary_types = ['Water', 'Poison', 'Normal', 'Ice', 'Water', 'Bug', 'Grass', 'Normal', 'Psychic', 'Fairy', 'Rock', 'Ice', 'Grass', 'Rock', 'Steel', 'Normal', 'Normal', 'Fire', 'Grass', 'Ground', 'Psychic', 'Grass', 'Ground', 'Normal', 'Bug', 'Water', 'Water', 'Steel', 'Grass', 'Normal', 'Ground', 'Normal', 'Fire', 'Water', 'Electric', 'Rock', 'Ground', 'Normal', 'Bug', 'Fairy', 'Ground', 'Ice', 'Fighting', 'Bug', 'Ghost', 'Psychic', 'Electric', 'Grass', 'Grass', 'Fairy', 'Ground', 'Water', 'Fire', 'Rock', 'Rock', 'Ice', 'Psychic', 'Steel', 'Water', 'Normal', 'Grass', 'Normal', 'Rock', 'Normal', 'Ghost', 'Fairy', 'Grass', 'Rock', 'Electric', 'Fairy', 'Normal', 'Bug', 'Psychic', 'Fire', 'Normal', 'Water', 'Water', 'Ghost', 'Fire', 'Normal', 'Fire', 'Ice', 'Normal', 'Ground', 'Fairy', 'Normal', 'Water', 'Psychic', 'Psychic', 'Fire', 'Ground', 'Fire', 'Grass', 'Normal', 'Ice', 'Fighting', 'Fire', 'Psychic', 'Ghost', 'Bug', 'Ground', 'Water', 'Normal', 'Normal', 'Dark', 'Rock', 'Electric', 'Normal', 'Grass', 'Bug', 'Ground', 'Psychic', 'Rock', 'Water', 'Grass', 'Grass', 'Poison', 'Water', 'Electric', 'Fire', 'Fire', 'Ice', 'Psychic', 'Fire', 'Ground', 'Water', 'Water', 'Water', 'Dark', 'Ground', 'Water', 'Bug', 'Rock', 'Ice', 'Bug', 'Water', 'Grass', 'Dragon', 'Normal', 'Water', 'Ground', 'Bug', 'Steel', 'Water', 'Bug', 'Dragon', 'Electric', 'Rock', 'Ice', 'Grass', 'Bug', 'Steel', 'Normal', 'Grass', 'Electric', 'Poison', 'Psychic', 'Electric', 'Electric', 'Grass', 'Bug', 'Bug', 'Fairy', 'Fighting', 'Water', 'Poison', 'Normal', 'Water', 'Normal', 'Ghost', 'Grass', 'Fire', 'Water', 'Electric', 'Bug', 'Normal', 'Dark', 'Water', 'Dragon', 'Bug', 'Fire', 'Water', 'Grass', 'Fairy', 'Dark', 'Electric', 'Grass', 'Bug', 'Normal', 'Rock', 'Poison', 'Poison', 'Rock', 'Water', 'Fire', 'Steel', 'Water', 'Psychic', 'Electric', 'Fairy', 'Grass', 'Grass', 'Grass', 'Normal', 'Normal', 'Rock', 'Dragon', 'Bug', 'Water', 'Normal', 'Dragon', 'Poison', 'Psychic', 'Grass', 'Fire', 'Poison', 'Grass', 'Grass', 'Bug', 'Normal', 'Rock', 'Ice', 'Water', 'Water', 'Poison', 'Dragon', 'Bug', 'Grass', 'Grass', 'Normal', 'Dark', 'Ghost', 'Water', 'Steel', 'Electric', 'Psychic', 'Fighting', 'Poison', 'Normal', 'Psychic', 'Normal', 'Water', 'Bug', 'Dark', 'Normal', 'Bug', 'Fairy', 'Fighting', 'Water', 'Fire', 'Fighting', 'Grass', 'Bug', 'Water', 'Water', 'Normal', 'Normal', 'Normal', 'Dragon', 'Grass', 'Water', 'Normal', 'Bug', 'Water', 'Steel', 'Water', 'Ghost', 'Rock', 'Dark', 'Electric', 'Ground', 'Poison', 'Water', 'Bug', 'Grass', 'Water', 'Bug', 'Normal', 'Poison', 'Psychic', 'Bug', 'Fighting', 'Normal', 'Grass', 'Grass', 'Poison', 'Normal', 'Ground', 'Normal', 'Bug', 'Fairy', 'Bug', 'Steel', 'Rock', 'Water', 'Fire', 'Fire', 'Water', 'Grass', 'Ice', 'Dark', 'Psychic', 'Water', 'Ice', 'Psychic', 'Rock', 'Steel', 'Water', 'Water', 'Bug', 'Normal', 'Dragon', 'Water', 'Electric', 'Ground', 'Normal', 'Bug', 'Dragon', 'Fighting', 'Electric', 'Psychic', 'Fighting', 'Fairy', 'Psychic', 'Water', 'Fire', 'Rock', 'Dark', 'Poison', 'Ice', 'Dragon', 'Normal', 'Dragon', 'Grass', 'Electric', 'Water', 'Psychic', 'Ground', 'Steel', 'Ice', 'Fairy', 'Fighting', 'Water', 'Ground', 'Normal', 'Poison', 'Steel', 'Water', 'Psychic', 'Ground', 'Poison', 'Fighting', 'Psychic', 'Steel', 'Rock', 'Water', 'Psychic', 'Water', 'Ghost', 'Psychic', 'Fighting', 'Bug', 'Bug', 'Grass', 'Normal', 'Ice', 'Dragon', 'Electric', 'Electric', 'Grass', 'Fairy', 'Rock', 'Normal', 'Water', 'Fighting', 'Water', 'Bug', 'Normal', 'Normal', 'Poison', 'Electric', 'Grass', 'Dark', 'Fire', 'Steel', 'Fire', 'Poison', 'Dragon', 'Rock', 'Bug', 'Psychic', 'Grass', 'Normal', 'Bug', 'Ghost', 'Dark', 'Fighting', 'Electric', 'Dragon', 'Dark', 'Normal', 'Fighting', 'Electric', 'Rock', 'Normal', 'Normal', 'Bug', 'Fire', 'Water', 'Normal', 'Ground', 'Bug', 'Fire', 'Bug', 'Water', 'Fire', 'Bug', 'Ghost', 'Bug', 'Steel', 'Ice', 'Normal', 'Water', 'Rock', 'Bug', 'Ghost', 'Ghost', 'Bug', 'Grass', 'Psychic', 'Rock', 'Steel', 'Ghost', 'Electric', 'Electric', 'Water', 'Ground', 'Poison', 'Normal', 'Fighting', 'Dark', 'Fairy', 'Grass', 'Poison', 'Normal', 'Fighting', 'Bug', 'Normal', 'Normal', 'Bug', 'Water', 'Bug', 'Fighting', 'Psychic', 'Water', 'Poison', 'Steel', 'Fighting', 'Psychic', 'Fighting', 'Dragon', 'Bug', 'Fire', 'Psychic', 'Grass', 'Normal', 'Normal', 'Poison', 'Bug', 'Water', 'Ground', 'Bug', 'Water', 'Psychic', 'Normal', 'Steel', 'Rock', 'Dragon', 'Grass', 'Grass', 'Water', 'Fighting', 'Ground', 'Fairy', 'Normal', 'Grass', 'Electric', 'Water', 'Fighting', 'Rock', 'Fire', 'Rock', 'Rock', 'Water', 'Grass', 'Fighting', 'Water', 'Bug', 'Bug', 'Grass']

generations = [1, 1, 1, 5, 3, 5, 1, 6, 1, 6, 5, 5, 4, 6, 3, 4, 2, 5, 2, 5, 4, 1, 1, 2, 6, 5, 5, 6, 6, 1, 4, 5, 6, 2, 6, 1, 3, 2, 4, 1, 5, 3, 5, 5, 1, 5, 5, 5, 5, 6, 1, 3, 4, 6, 1, 4, 5, 3, 5, 5, 1, 4, 1, 1, 5, 6, 5, 1, 1, 6, 5, 5, 4, 6, 1, 1, 4, 5, 4, 5, 6, 2, 3, 5, 6, 5, 3, 4, 5, 1, 5, 6, 1, 1, 2, 3, 3, 3, 4, 4, 1, 3, 6, 3, 5, 3, 5, 3, 3, 1, 3, 6, 4, 4, 4, 5, 3, 4, 4, 3, 5, 5, 3, 5, 4, 1, 1, 3, 5, 3, 2, 5, 4, 3, 2, 4, 3, 5, 3, 1, 2, 4, 3, 5, 3, 5, 4, 1, 2, 4, 3, 5, 5, 1, 4, 6, 3, 6, 3, 4, 1, 5, 6, 1, 5, 4, 4, 3, 3, 5, 2, 3, 1, 6, 5, 1, 5, 4, 3, 6, 1, 3, 3, 6, 4, 3, 5, 4, 2, 4, 4, 1, 2, 5, 1, 3, 6, 4, 1, 1, 1, 1, 2, 4, 1, 1, 4, 4, 5, 3, 1, 4, 5, 3, 4, 1, 3, 4, 2, 5, 3, 4, 1, 1, 1, 5, 1, 4, 4, 3, 4, 3, 5, 3, 2, 3, 3, 3, 2, 4, 1, 3, 4, 2, 6, 5, 2, 5, 5, 1, 1, 1, 5, 4, 2, 4, 2, 2, 5, 5, 5, 4, 2, 3, 3, 5, 4, 5, 6, 3, 1, 2, 4, 2, 5, 1, 4, 3, 1, 1, 1, 1, 3, 5, 1, 3, 3, 3, 3, 5, 2, 5, 4, 2, 2, 3, 6, 4, 2, 1, 2, 5, 5, 3, 1, 3, 5, 5, 5, 5, 6, 5, 1, 5, 1, 5, 5, 1, 6, 4, 3, 1, 6, 5, 1, 4, 6, 5, 1, 2, 5, 5, 3, 1, 5, 5, 3, 3, 3, 6, 1, 5, 1, 3, 3, 4, 5, 3, 1, 1, 1, 6, 3, 3, 4, 5, 3, 5, 4, 5, 1, 5, 5, 3, 5, 6, 5, 4, 5, 6, 1, 1, 4, 1, 3, 4, 1, 4, 1, 1, 5, 4, 4, 5, 5, 6, 1, 1, 2, 4, 2, 5, 2, 5, 5, 6, 1, 3, 3, 5, 6, 4, 3, 3, 1, 5, 5, 2, 3, 5, 3, 6, 3, 5, 2, 1, 2, 5, 2, 3, 3, 1, 3, 1, 1, 4, 3, 1, 3, 5, 1, 3, 6, 4, 5, 2, 2, 6, 2, 2, 5, 6, 2, 1, 3, 5, 3, 3, 5, 5, 5, 3, 5, 2, 2, 4, 4, 3, 5, 6, 1, 4, 1, 1, 4, 2, 3, 4, 5, 2, 4, 3, 3, 4, 3, 3, 3, 3, 1, 2, 3, 5, 5, 6, 4, 3, 5, 5, 5, 6, 1, 2, 3, 1, 5, 6, 2, 1, 3, 5]

names = ['Seel', 'Nidorino', 'Fearow', 'Vanilluxe', 'Relicanth', 'Karrablast', 'Exeggutor', 'Diggersby', 'Mew', 'Flabébé', 'Archen', 'Cryogonal', 'Cherubi', 'Barbaracle', 'Jirachi', 'Lopunny', 'Sentret', 'Heatmor', 'Bellossom', 'Drilbur', 'Gallade', 'Ivysaur', 'Sandslash', 'Aipom', 'Scatterbug', 'Carracosta', 'Frillish', 'Honedge', 'Gogoat', 'Kangaskhan', 'Hippowdon', 'Lillipup', 'Braixen', 'Wooper', 'Helioptile', 'Geodude', 'Claydol', 'Furret', 'Burmy', 'Clefairy', 'Sandile', 'Walrein', 'Throh', 'Leavanny', 'Gengar', 'Solosis', 'Eelektross', 'Foongus', 'Ferroseed', 'Sylveon', 'Marowak', 'Wailord', 'Chimchar', 'Tyrunt', 'Golem', 'Mamoswine', 'Elgyem', 'Metagross', 'Panpour', 'Cinccino', 'Gloom', 'Chatot', 'Onix', 'Dodrio', 'Chandelure', 'Florges', 'Lilligant', 'Graveler', 'Raichu', 'Sylveon', 'Minccino', 'Scolipede', 'Cresselia', 'Delphox', 'Wigglytuff', 'Seadra', 'Shellos', 'Lampent', 'Infernape', 'Sawsbuck', 'Delphox', 'Delibird', 'Slaking', 'Stunfisk', 'Spritzee', 'Lillipup', 'Sharpedo', 'Gallade', 'Beheeyem', 'Charmander', 'Krookodile', 'Braixen', 'Bellsprout', 'Snorlax', 'Swinub', 'Hariyama', 'Numel', 'Gardevoir', 'Mismagius', 'WormadamTrash Cloak', 'Dugtrio', 'Wailmer', 'Diggersby', 'Castform', 'Bisharp', 'Lileep', 'Eelektross', 'Zigzagoon', 'Tropius', 'Venomoth', 'Vibrava', 'MeowsticFemale', 'Shieldon', 'Floatzel', 'Carnivine', 'Servine', 'Swalot', 'Finneon', 'Magnezone', 'Combusken', 'DarmanitanStandard Mode', 'Cryogonal', 'Wynaut', 'Emboar', 'Hippopotas', 'Krabby', 'Tentacruel', 'Ludicolo', 'Bisharp', 'Claydol', 'Corsola', 'Shelmet', 'Bastiodon', 'Snorunt', 'Yanma', 'Lumineon', 'Treecko', 'Zekrom', 'Azurill', 'Golduck', 'Phanpy', 'WormadamSandy Cloak', 'Aron', 'Panpour', 'Illumise', 'Zekrom', 'Shinx', 'Kabutops', 'Delibird', 'Carnivine', 'Beautifly', 'Klang', 'Patrat', 'Exeggutor', 'RotomWash Rotom', 'Dragalge', 'Kirlia', 'Dedenne', 'Electrike', 'Cherrim', 'Venomoth', 'Scolipede', 'Swirlix', 'Primeape', 'Simipour', 'Skuntank', 'Glameow', 'Clamperl', 'Swablu', 'Cofagrigus', 'Hoppip', 'Torchic', 'Psyduck', 'Helioptile', 'Larvesta', 'Wigglytuff', 'Mandibuzz', 'Empoleon', 'Shelgon', 'Spewpa', 'Charizard', 'Clamperl', 'Seedot', 'Spritzee', 'Darkrai', 'Electrike', 'Virizion', 'Yanmega', 'Girafarig', 'Cranidos', 'Croagunk', 'Nidoking', 'Pupitar', 'Tympole', 'Flareon', 'Lairon', 'Frogadier', 'Mime Jr.', 'Magnemite', 'Clefable', 'Gloom', 'Exeggcute', 'Bayleef', 'Staravia', 'Rattata', 'Golem', 'Gible', 'Kricketune', 'Seismitoad', 'Slakoth', 'Dragonair', 'Skuntank', 'Munna', 'Cacturne', 'Magmortar', 'Golbat', 'Shroomish', 'Leafeon', 'Ledian', 'Cinccino', 'Armaldo', 'Froslass', 'Seadra', 'Slowbro', 'Nidorino', 'KyuremBlack Kyurem', 'Venomoth', 'Carnivine', 'Abomasnow', 'Zangoose', 'Honchkrow', 'Banette', 'Panpour', 'Beldum', 'Ampharos', 'Wynaut', 'Medicham', 'Seviper', 'Blissey', 'Azelf', "Farfetch'd", 'Relicanth', 'WormadamPlant Cloak', 'Sneasel', 'Fletchling', 'Larvesta', 'Cleffa', 'Mienfoo', 'Panpour', 'Arcanine', 'Hitmonchan', 'Tangela', 'Escavalier', 'Lumineon', 'Kingdra', 'Lickilicky', 'Noctowl', 'Blissey', 'Zekrom', 'Amoonguss', 'Carracosta', 'Staravia', 'Pineco', 'Swampert', 'Jirachi', 'Swanna', 'Drifblim', 'Roggenrola', 'Inkay', 'Electrike', 'Cubone', 'Crobat', 'Prinplup', 'Spinarak', 'Lilligant', 'Poliwhirl', 'Vespiquen', 'Loudred', 'Grimer', 'Kadabra', 'Caterpie', 'Machop', 'Slakoth', 'Foongus', 'Exeggcute', 'Gulpin', 'Delcatty', 'GroudonPrimal Groudon', 'Delcatty', 'Shelmet', 'Granbull', 'Shelmet', 'Bronzong', 'Tyranitar', 'Azumarill', 'Numel', 'Pyroar', 'Mantyke', 'Chikorita', 'Articuno', 'Umbreon', 'Musharna', 'Jellicent', 'Spheal', 'Kadabra', 'Nosepass', 'Cobalion', 'Ducklett', 'Tirtouga', 'Accelgor', 'Fletchling', 'KyuremWhite Kyurem', 'Slowbro', 'Zebstrika', 'Dugtrio', 'Stoutland', 'Shelmet', 'Dragonair', 'Hawlucha', 'RotomFrost Rotom', 'Gardevoir', 'Primeape', 'Swirlix', 'Gothita', 'Krabby', 'Chimchar', 'Aurorus', 'Mandibuzz', 'Nidoqueen', 'Delibird', 'Fraxure', 'Pidove', 'Altaria', 'Oddish', 'Blitzle', 'Ducklett', 'Ralts', 'Baltoy', 'Jirachi', 'Avalugg', 'Clefable', 'Gurdurr', 'Seel', 'Baltoy', 'Vigoroth', 'Stunky', 'Klinklang', 'Luvdisc', 'Mew', 'Sandshrew', 'Koffing', 'Pancham', 'Kirlia', 'Jirachi', 'Probopass', 'Tympole', 'Spoink', 'Basculin', 'Drifblim', 'Duosion', 'Primeape', 'Shelmet', 'Whirlipede', 'Roselia', 'Rufflet', 'Avalugg', 'Druddigon', 'Luxray', 'Eelektrik', 'Chespin', 'Clefable', 'Graveler', 'Chatot', 'Psyduck', 'Makuhita', 'Piplup', 'Pinsir', 'Lopunny', 'Tauros', 'Grimer', 'Eelektross', 'Turtwig', 'Darkrai', 'Emboar', 'Cobalion', 'Talonflame', 'Nidorino', 'Dragonair', 'Larvitar', 'WormadamSandy Cloak', 'Wobbuffet', 'Maractus', 'Teddiursa', 'Leavanny', 'Lampent', 'Yveltal', 'Primeape', 'Plusle', 'Altaria', 'Zweilous', 'Bunnelby', 'Riolu', 'Manectric', 'Lunatone', 'Wigglytuff', 'Bouffalant', 'Leavanny', 'Cyndaquil', 'Clamperl', 'Minccino', 'Groudon', 'Scatterbug', 'Torkoal', 'Scolipede', 'Slowking', 'Rapidash', 'Ledian', 'Cofagrigus', 'Ledian', 'Mawile', 'Sealeo', 'Lickitung', 'Sharpedo', 'Kabutops', 'Beedrill', 'Spiritomb', 'Dusclops', 'Venomoth', 'Nuzleaf', 'Gothita', 'Onix', 'Aron', 'Trevenant', 'Electivire', 'Blitzle', 'Feraligatr', 'Donphan', 'Skrelp', 'Ursaring', 'Hitmontop', 'Hydreigon', 'Spritzee', 'Jumpluff', 'Arbok', 'Taillow', 'Gurdurr', 'Dustox', 'Zangoose', 'Sawsbuck', 'Volcarona', 'Simipour', 'Shedinja', 'Mienfoo', 'Wobbuffet', 'Mantine', 'Croagunk', 'Bronzor', 'Meditite', 'Elgyem', 'Hawlucha', 'Dratini', 'WormadamTrash Cloak', 'Moltres', 'Mr. Mime', 'Roserade', 'Dunsparce', 'Skitty', 'Skuntank', 'Joltik', 'Slowking', 'Rhyperior', 'Beautifly', 'Kyogre', 'Gallade', 'Azurill', 'Aggron', 'Solrock', 'Salamence', 'Weepinbell', 'Skiploom', 'Marshtomp', 'Mienshao', 'Krookodile', 'Xerneas', 'Staraptor', 'Shiftry', 'Eelektross', 'Dewott', 'Throh', 'Barbaracle', 'Ninetales', 'Sudowoodo', 'Nosepass', 'Staryu', 'Snivy', 'Hawlucha', 'Suicune', 'Weedle', 'Nincada', 'Simisage']

from collections import Counter

def counter_ex():
    # Collect the count of primary types
    type_count = Counter(primary_types)
    print(type_count, '\n')

    # Collect the count of generations
    gen_count = Counter(generations)
    print(gen_count, '\n')

    # Use list comprehension to get each Pokémon's starting letter
    starting_letters = [name[0] for name in names]

    # Collect the count of Pokémon for each starting_letter
    starting_letters_count = Counter(starting_letters)
    print(starting_letters_count)

# Import combinations from itertools
from itertools import combinations

pokemon = ['Geodude', 'Cubone', 'Lickitung', 'Persian', 'Diglett']

def combinations_ex():
    # Create a combination object with pairs of Pokémon
    combos_obj = combinations(pokemon, 2)
    print(type(combos_obj), '\n')

    # Convert combos_obj to a list by unpacking
    combos_2 = [*combos_obj]
    print(combos_2, '\n')

    # Collect all possible combinations of 4 Pokémon directly into a list
    combos_4 = [*combinations(pokemon, 4)]
    print(combos_4)
    
ash_pokedex = ['Pikachu', 'Bulbasaur', 'Koffing', 'Spearow', 'Vulpix', 'Wigglytuff', 'Zubat', 'Rattata', 'Psyduck', 'Squirtle']

misty_pokedex = ['Krabby', 'Horsea', 'Slowbro', 'Tentacool', 'Vaporeon', 'Magikarp', 'Poliwag', 'Starmie', 'Psyduck', 'Squirtle']

def sets_ex():
    # Convert both lists to sets
    ash_set = set(ash_pokedex)
    misty_set = set(misty_pokedex)

    # Find the Pokémon that exist in both sets
    both = ash_set.intersection(misty_set)
    print(both)

    # Find the Pokémon that Ash has and Misty does not have
    ash_only = ash_set.difference(misty_set)
    print(ash_only)

    # Find the Pokémon that are in only one set (not both)
    unique_to_set = ash_set.symmetric_difference(misty_set)
    print(unique_to_set)
    
def unique_list():
    unique_generations = set(generations)
    print(unique_generations)
