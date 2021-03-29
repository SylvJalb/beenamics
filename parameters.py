import numpy as np

# la ville où sont situé les ruches
city_name = "Gelos"
lat = "43.285713"
lon = "-0.372236"

# la clé de l'api openweathermap
api_key = "0446cefece6ab95b7f30537fd53489e0"


# le nombre de jour prédit par l'API
nbr_day_predict = 4

# Le nombre de cellules dans la ruche
CELLShive = 250000

# La durée de vie en jour, par catégorie
LIFESPANegg = 3
LIFESPANlarva = 5
LIFESPANpupa = 12

# La répartition des abeilles infirmières
NEEDnurses_per_pupa = 0.33
NEEDnurses_per_egg = 0.33
NEEDnurses_per_larva = lambda i: [.1,.5,.75,1.75,3][i]

# Les differents besoins en pollen
POLLENNEEDadult = .004
POLLENNEEDnurse = .05
POLLENNEEDlarva = lambda i: [.001,.003 , .006, .012, .027][i]

# Les differents besoins en nectar
NECTARNEEDlarva = lambda i: [.006,.018,.04,.09,.185][i]
NECTARNEEDadult = .005
NECTARNEEDnurse = .02
NECTARNEEDactiveforager = .02

# Le taux de cannibalism
CANNIBALISMhungerbase = lambda i: [.23,.3,.58,.06,0][i - 1]

# Les variables servant au calcul de l'ELR (L'activité de ponte quotidienne)
SUPthreshold = 0.2
ELRstochrange = 0.01
ELRbase = 1600

# Les diferents facteurs à prendre en compte
FACTORpollenstorage = 6
FACTORforagingsuccess = .8
FACTORminpollenforagers = .01
FACTORforagingmax = .33
FACTORpollensavingmax = .3
FACTORothertasks = 0.2

# le montant de pollen et nectar collecté à chaque voyage de recherche de nourriture
LOADpollenforager = .06
LOADnectarforager = .04
# le nombre de voyages effectués par butineur où il ramène du pollen ou/et du nectar, par jour
TURNSpollenforager = 10
TURNSnectarforager = 15

# le nombre d'abeilles qui se charge de la transformation du nectar pour une cellule
ProcessorsPerCell = 2
# le ratio de nectar qui sera transformé en miel
RATIOnectar_to_honey = .4

# Le taux de mortalité par catégorie
MORTALITYnursing = .005
MORTALITYprocessing = .005
MORTALITYforaging = .035
MORTALITYadultbase = 0.01
MORTALITYpupae = 0.001
MORTALITYlarvae = 0.01
MORTALITYeggs = 0.03

# le jour du "swarming day"
swd = 140

# Le nombre d'abeille adulte au départ
BEESadultbase = 15000

# les valeurs _t0 sont des valeurs experiementales
# que l'on prend en regardant les graphs ou experimentalement
INITpollen = 0
INITnectar = 0
INIThoney = 50000
STOCHASTIC_FACTOR = True

# les différents poids
w_hivebase = 14000
w_cellsbase = .037
w_pollen = .23
w_nectar = .43
w_larva = lambda i: [.0002,.00059,.00331,.0644,.16][i-1]
w_honey = .5
w_egg = .0001
w_pupa = .16
w_adult = .1

#METEO
# La vitesse de vent à partir de laquelle les abeilles ne sont plus en mesure de voler (en m/s)
WIND_max = 12.5
# L'humidité minimale afin d'avoir du nectar
HUMIDITY_min = 60