FISHES_TYPE = {
    "\N{BATTERY}": "garbage",
    "\N{SHOPPING TROLLEY}": "garbage",
    "\N{MANS SHOE}": "garbage",
    "\N{WRENCH}": "garbage",
    "\N{BABY BOTTLE}": "garbage",
    "\N{FISH}": "common",
    "\N{SHRIMP}": "common",
    "\N{CRAB}": "common",
    "\N{TROPICAL FISH}": "uncommon",
    "\N{BLOWFISH}": "uncommon",
    "\N{LOBSTER}": "uncommon",
    "\N{SQUID}": "rare",
    "\N{OCTOPUS}": "rare",
    "\N{DOLPHIN}": "rare",
    "\N{SHARK}": "legendary",
    "\N{SPOUTING WHALE}": "legendary",
}

RODS = [
    "wooden rod",
    "magnet rod",
    "fly-fishing rod",
    "spinning rod",
    "harpoon",
    "telescopic rod",
    "carbon-fibre rod",
    "metal rod",
    "trusty rod",
    "pikachu rod",
]
RODS_WEIGHT = [0.75, 0.07, 0.07, 0.05, 0.03, 0.01, 0.008, 0.0065, 0.0045, 0.001]
print(sum(RODS_WEIGHT))
RODS_PRICES = {
    "fly-fishing rod": 85000,
    "magnet rod": 100000,
    "spinning rod": 200000,
    "harpoon": 350000,
    "telescopic rod": 420000,
    "carbon-fibre rod": 800000,
    "metal rod": 1000000,
    "trusty rod": 7500000,
    "pikachu rod": 15000000,
}

WEIGHTS = {
    "wooden rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.2,
        0.2,
        0.2,
        0.06,
        0.06,
        0.06,
        0.002,
        0.002,
    ],
    "magnet rod": [
        0.65,
        0.65,
        0.65,
        0.65,
        0.65,
        0.35,
        0.35,
        0.35,
        0.15,
        0.15,
        0.15,
        0.04,
        0.04,
        0.04,
        0.001,
        0.001,
    ],
    "fly-fishing rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.25,
        0.25,
        0.25,
        0.06,
        0.06,
        0.06,
        0.002,
        0.002,
    ],
    "spinning rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.25,
        0.25,
        0.25,
        0.1,
        0.1,
        0.1,
        0.002,
        0.002,
    ],
    "harpoon": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.2,
        0.2,
        0.2,
        0.1,
        0.1,
        0.1,
        0.004,
        0.004,
    ],
    "telescopic rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.4,
        0.4,
        0.4,
        0.23,
        0.23,
        0.23,
        0.07,
        0.07,
        0.07,
        0.002,
        0.002,
    ],
    "carbon-fibre rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.37,
        0.37,
        0.37,
        0.3,
        0.3,
        0.3,
        0.12,
        0.12,
        0.12,
        0.002,
        0.002,
    ],
    "metal rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.45,
        0.45,
        0.45,
        0.25,
        0.25,
        0.25,
        0.1,
        0.1,
        0.1,
        0.004,
        0.004,
    ],
    "trusty rod": [
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.35,
        0.3,
        0.3,
        0.3,
        0.2,
        0.2,
        0.2,
        0.006,
        0.006,
    ],
    "pikachu rod": [
        0.25,
        0.25,
        0.25,
        0.25,
        0.25,
        0.35,
        0.35,
        0.35,
        0.2,
        0.2,
        0.2,
        0.1,
        0.1,
        0.1,
        0.04,
        0.04,
    ],
}

FISHES = list(FISHES_TYPE.keys())
ROD = "\N{FISHING POLE AND FISH}"


EVENTS = [
    "Oops. You spill all your bait into the water. You spend {amount} {currency} to buy a bucket from the shop.",
    "Your line snaps while you cast out and pay {amount} {currency} for a new spool.",
    "Your hook is blunt and you pay {amount} {currency} for a new set from the shop.",
]

LEGENDARY_PRICE = 35000
EPIC_PRICE = 7000
RARE_PRICE = 3000
UNCOMMON_PRICE = 650
COMMON_PRICE = 140
GARBAGE_PRICE = 7


WEATHER = [
    "Sunny \N{BLACK SUN WITH RAYS}\N{VARIATION SELECTOR-16}",
    "Snowing \N{CLOUD WITH SNOW}\N{VARIATION SELECTOR-16}",
    "Lightning \N{THUNDER CLOUD AND RAIN}\N{VARIATION SELECTOR-16}",
    "Windy \N{DASH SYMBOL}",
    "Raining \N{CLOUD WITH RAIN}\N{VARIATION SELECTOR-16}",
    "Cloudy \N{WHITE SUN BEHIND CLOUD}\N{VARIATION SELECTOR-16}",
]
WEATHER_EFFECTS = {
    "Sunny \N{BLACK SUN WITH RAYS}\N{VARIATION SELECTOR-16}": [
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.036,
        -0.03,
        -0.0015,
        -0.0015,
    ],
    "Snowing \N{CLOUD WITH SNOW}\N{VARIATION SELECTOR-16}": [
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        -0.07,
        -0.07,
        -0.07,
        -0.07,
        -0.07,
        -0.05,
        -0.05,
        -0.05,
        -0.05,
        -0.0019,
        -0.0019,
    ],
    "Lightning \N{THUNDER CLOUD AND RAIN}\N{VARIATION SELECTOR-16}": [
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.03,
        -0.036,
        -0.03,
        -0.0015,
        -0.0015,
    ],
    "Windy \N{DASH SYMBOL}": [
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.000,
        0.000,
    ],
    "Raining \N{CLOUD WITH RAIN}\N{VARIATION SELECTOR-16}": [
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.05,
        0.05,
        0.05,
        0.03,
        0.03,
        0.03,
        0.02,
        0.02,
        0.02,
        0.002,
        0.002,
    ],
    "Cloudy \N{WHITE SUN BEHIND CLOUD}\N{VARIATION SELECTOR-16}": [
        0.00,
        0.00,
        0.00,
        0.00,
        0.00,
        0.07,
        0.07,
        0.07,
        0.03,
        0.03,
        0.03,
        0.02,
        0.02,
        0.02,
        0.002,
        0.002,
    ],
}
