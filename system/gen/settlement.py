#!/usr/bin/env python3

import random
import sys

from dataclasses import dataclass
from enum import Enum


# LOCAL UTILS

def d(n):
    return random.randint(1, n)


# LOCAL DATA TYPES

SETTLEMENT = Enum("SETTLEMENT", [("VILLAGE", 0), ("TOWN", 1), ("CITY", 2)])
TERRAIN = Enum("TERRAIN", [("WATER", 0), ("MOUNTAIN", 1), ("HILLS", 2), ("PLAINS", 3),
                           ("FOREST", 4), ("DESERT", 5), ("JUNGLE", 6), ("SWAMP", 7),
                           ("TUNDRA", 8)])

THEME = Enum("THEME", [("CENTRE", 0)])


@dataclass
class Neighbourhood:
    name : str
    theme : THEME
    description : str
    feature : str
    faction : str


@dataclass
class District:
    name : str
    theme : THEME
    description : str
    centre : Neighbourhood
    neighbourhoods : list[Neighbourhood]


@dataclass
class Settlement:
    name : str
    tier : SETTLEMENT
    description : str
    terrain : TERRAIN


@dataclass
class Village(Settlement):
    neighbourhood : Neighbourhood


@dataclass
class Town(Settlement):
    district : District


@dataclass
class City(Settlement):
    centre : District
    districts : list[District]



# GENERATORS

def gen_name(tier : SETTLEMENT):
    return f"A tier-{tier} settlement name"

def gen_terrain():
    return random.choice(list(TERRAIN))

def gen_theme():
    return random.choice(list(THEME))

def gen_description(settlement : Settlement):
    return f"A tier-{settlement.tier} settlement description"

def gen_feature(tier : SETTLEMENT):
    return f"A tier-{tier} settlement feature"

def gen_faction(tier : SETTLEMENT):
    return f"A tier-{tier} settlement faction"

def gen_neighbourhood(tier : SETTLEMENT, theme = None):
    return Neighbourhood(
        name = "Neighbourhood",
        theme = theme if theme is not None else gen_theme(),
        description = "Description",
        feature = gen_feature(tier),
        faction = gen_faction(tier)
    )

def gen_district(tier : SETTLEMENT, theme = None):
    tier_down = SETTLEMENT(tier.value - 1)
    return District(
        name = "District Name",
        theme = theme if theme is not None else gen_theme(),
        description = "Description",
        centre = gen_neighbourhood(tier, theme = THEME.CENTRE),
        neighbourhoods = [gen_neighbourhood(tier_down) for i in range(1 + d(2))]
    )


def gen_village():
    t = SETTLEMENT.VILLAGE
    village = Village(
        name = gen_name(t),
        tier = t,
        terrain = gen_terrain(),
        description = None,
        neighbourhood = gen_neighbourhood(t, theme = THEME.CENTRE),
    )
    village.description = gen_description(village)

    return village

def gen_town():
    t = SETTLEMENT.TOWN
    town = Town(
        name = gen_name(t),
        tier = t,
        terrain = gen_terrain(),
        description = None,
        district = gen_district(t)
    )
    
    town.description = gen_description(town)
    return town

def gen_city():
    t = SETTLEMENT.CITY
    city = City(
        name = gen_name(t),
        tier = t,
        terrain = gen_terrain(),
        description = None,
        centre = gen_district(t, theme = THEME.CENTRE),
        districts = [ gen_district(SETTLEMENT.TOWN) for i in range(1 + d(2)) ]
    );

    city.description = gen_description(city)
    return city


def gen_settlement(tier : SETTLEMENT):
    return [gen_village, gen_town, gen_city][tier.value]()


def main():
    if len(sys.argv) == 1:
        tier = random.choice(list(SETTLEMENT))
    else:
        tier = SETTLEMENT[sys.argv[1].upper()]
    
    res = gen_settlement(tier)
    print(res)

if __name__ == "__main__":
    main()
