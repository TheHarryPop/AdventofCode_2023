# -*- coding: utf-8 -*-
data_test = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

data = """"""

# La première ligne de l'input contient 4 graines identifiées 79, 14, 55, & 13
# Les catégories suivantes correspondent à des paramètres :
#   seed to soil : permet de déterminer quel sol en fonction de quelle graine
#       50 98 2 :
#           50 = début de plage de destination (sol)
#           98 = début de plage source (graine)
#           2 = longueur de plage
#       La plage source commence à 98 et contient 2 valeurs (longueur) -> 98, 99
#       La plage destination commence à 50 et contient 2 valeurs (longueur) -> 50, 51
#       Donc la graine 98 correspond au sol 50 et la graine 99 correspond au sol 51.
#   soil to fertilizer : permet de déterminer quel fertilisant en fonction de quel sol
#   fertilizer to water : permet de déterminer quel fertilisant avec quel arrosage en fonction de quel fertilisant
#   water to light : permet de déterminer quel ensoleillement en fonction de quel arrosage
#   light to temperature : permet de déterminer quelle température en fonction de quel ensoleillement
#   temperature to humidity : permet de déterminer quelle humidité en fonction de quelle température
#   humidity to location : permet de déterminer quel emplacement en fonction de quelle humidité
# Avec les quatre graines de départ on va déterminer à la fin quatre emplacements.
# Le but est de donner l'emplacement le plus proche de 0.
