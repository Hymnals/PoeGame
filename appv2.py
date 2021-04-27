import random
import tkinter
from tkinter import *
import easygui

#auto-py-to-exe

playerName = easygui.enterbox("What is your name Exile?")
m=tkinter.Tk(className='\Exile '+playerName+'\'s ' 'War of Ascenscion Tracker')

turnCounter=1
modNumber=32
suffNum=16
prefNum=16
prefOrSuff=2
packs=[]
packNumber=0
#packMods=[]
#whichMods=[]
rarity=[]
packNames=[]
packPrefs=[]
packSufs=[]
packTypesPrefs=[]
packTypesSufs=[]

modTypesPrefix=[
    "DefenseP", "DefenseP", "DefenseP",
    "EleAil", "EleAil", "EleAil", "EleAil",
    "OffenseP", "OffenseP",
    "StatGain", "StatGain", "StatGain", "StatGain", "StatGain", "StatGain", "StatGain"
]

modTypesSuffix=[
    "ChargeGain", "ChargeGain", "ChargeGain",
    "Critical", "Critical", "Critical",
    "DefenseS", "DefenseS",
    "Flask",
    "LifeGain",
    "Loot", "Loot", "Loot",
    "OffenseS", "OffenseS", "OffenseS"
]

defensePMods=["Guards", "At the end of your turn, Fortify: X.", "At the end of your turn, this pack restores X life to itself."]
eleAilMods=["Ignites", "Shocks", "Freezes", "Chills"]
offensePMods=["At the end of your turn, Charges.", "When this pack attacks, gain X Rage."]
statGainMods=["+X/0/0", "+0/X/0", "+0/0/X", "+X/X/0", "+0/X/X", "+X/X/X"]
chargeGainMods=["At the end of your turn, gain a Power Charge.", "At the end of your turn, gain an Endurance Charge.", "At the end of your turn, gain a Frenzy Charge."]
criticalMods=["Critical Strike: Restore this pack to full life.", "Critical Strike: Shatter the Critically Struck pack.", "Critical Strike: This pack Charges."]
defenseSMods=["Leech", "Range"]
flaskMods=["At the end of your turn, target a flask. That flask gains X charges."]
lifeGainmods=["At the end of your turn, restore X life to the allied Exile."]
lootMods=["Loot: Draw X cards.", "Loot: Give allied packs +X/X/0.", "Loot: Spawn X 1/1/0 Unique Parasites."]
offenseSMods=["Bleed", "Poison", "Focused"]

# masterlist=[['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Loot: Allied exiles regain 1 life.', 'N/A', 'N/A', 'N/A', 'Gain 1 Rage when this pack attacks.', 'At end of turn, Charges', 'N/A', 'N/A', 'Guard', 'Ignites', 'N/A', 'N/A', 'N/A', 'N/A', 'Critical Strike: Gain 1 damage', 'N/A', '+1/0/0', '+0/1/0', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
#             ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Loot: Allied exiles regain 1 life.', 'At the end of your turn, restore 1 life to allied exiles.', 'N/A', 'N/A', 'Gain 1 Rage when this pack attacks.', 'At end of turn, Charges', 'N/A', ' Leech', 'Guard', 'Ignites', 'N/A', 'N/A', 'Poison 1', 'Bleed 1', 'Critical Strike: Gain 1 damage', 'N/A', '+1/0/0', '+0/1/0', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A'],
#             ['N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Loot: Gain an Endurance Charge.', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Loot: Allied exiles regain 2 life.', 'At the end of your turn, restore 1 life to allied exiles.', 'N/A', 'N/A', 'Gain 1 Rage when this pack attacks.', 'At end of turn, Charges', 'Focused', ' Leech', 'Guard', 'Ignites', 'Chills', 'Shocks', 'Poison 1', 'Bleed 1', 'Critical Strike: Gain 1 damage', 'Critical Strike: Restore 1 life.', '+1/0/0', '+0/1/0', '+0/0/1', '+1/1/0', 'N/A', 'N/A', 'N/A'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 2 extra Alteration orbs.', 'At the start of your turn, gain an extra Alteration orb.', 'Loot: Gain a Frenzy Charge', 'N/A', 'Loot: Gain an Endurance Charge.', 'N/A', 'N/A', 'N/A', 'N/A', 'N/A', 'Loot: Allied exiles regain 2 life.', 'At the end of your turn, restore 2 life to allied exiles.', 'N/A', 'Range', 'Gain 2 Rage when this pack attacks.', 'At end of turn, Charges', 'Focused', ' Leech', 'Guard, at the end of your turn Fortify: 1.', 'Ignites', 'Chills', 'Shocks', 'Poison 1', 'Bleed 1', 'Critical Strike: Gain 2 damage', 'Critical Strike: Restore 1 life.', '+2/0/0', '+0/2/0', '+0/0/1', '+1/1/0', 'N/A', 'N/A', 'N/A'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 2 extra Alteration orbs.', 'At the start of your turn, gain an extra Alteration orb.', 'Loot: Gain a Frenzy Charge', 'N/A', 'Loot: Gain an Endurance Charge.', 'At the end of your turn gain an Endurance Charge.', 'N/A', 'N/A', 'Loot: Restore a flask charge.', 'N/A', 'Loot: Allied exiles regain 3 life.', 'At the end of your turn, restore 2 life to allied exiles.', 'Loot: Draw a card.', 'Range', 'Gain 2 Rage when this pack attacks.', 'At end of turn, Charges', 'Focused', ' Leech', 'Guard, at the end of your turn Fortify: 1.', 'Ignites', 'Chills', 'Shocks', 'Poison 1', 'Bleed 1', 'Critical Strike: Gain 2 damage', 'Critical Strike: Restore 2 life.', '+2/0/0', '+0/2/0', '+0/0/2', '+1/1/0', '+2/0/1', '+0/1/1', 'N/A'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 2 extra Alteration orbs.', 'At the start of your turn, gain an extra Alteration orb.', 'Loot: Gain a Frenzy Charge', 'At the end of your turn, gain a Frenzy Charge.', 'Loot: Gain an Endurance Charge.', 'At the end of your turn gain an Endurance Charge.', 'N/A', 'N/A', 'Loot: Restore a flask charge.', 'N/A', 'Loot: Allied exiles regain 3 life.', 'At the end of your turn, restore 3 life to allied exiles.', 'Loot: Draw a card.', 'Range', 'Gain 2 Rage when this pack attacks.', 'At end of turn, Charges', 'Focused, gain 1 life.', ' Leech', 'Guard, at the end of your turn Fortify: 2.', 'Ignites, gain 1 damage', 'Chills, gain 1 life', 'Shocks, gain 1 energy shield', 'Poison 2', 'Bleed 2', 'Critical Strike: Gain 2 damage', 'Critical Strike: Restore 2 life.', '+2/0/0', '+0/2/0', '+0/0/2', '+2/2/0', '+2/0/2', '+0/2/1', '+1/1/1'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 2 extra Alteration orbs.', 'At the start of your turn, gain an extra Alteration orb and Chaos orb..', 'Loot: Gain a Frenzy Charge', 'At the end of your turn, gain a Frenzy Charge.', 'Loot: Gain an Endurance Charge.', 'At the end of your turn gain an Endurance Charge.', 'Loot: Gain a Power Charge.', 'N/A', 'Loot: Restore a flask charge.', 'At the start of your turn, choose a flask. Give that flask 1 charge.', 'Loot: Allied exiles regain 3 life.', 'At the end of your turn, restore 3 life to allied exiles.', 'Loot: Draw a card.', 'Range', 'Gain 3 Rage when this pack attacks.', 'At the end of your turn, Charges', 'Focused, gain 1 life.', ' Leech', 'Guard, at the end of your turn Fortify: 2.', 'Ignites, gain 1 damage', 'Chills, gain 1 life', 'Shocks, gain 1 energy shield', 'Poison 2', 'Bleed 2', 'Critical Strike: Gain 3 damage', 'Critical Strike: Restore 2 life.', '+3/0/0', '+0/3/0', '+0/0/2', '+2/2/0', '+2/0/2', '+0/2/2', '+1/1/1'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 2 extra Alteration orbs.', 'At the start of your turn, gain an extra Alteration orb and Chaos orb..', 'Loot: Gain a Frenzy Charge', 'At the end of your turn, gain a Frenzy Charge.', 'Loot: Gain an Endurance Charge.', 'At the end of your turn gain an Endurance Charge.', 'Loot: Gain a Power Charge.', 'At the end of your turn gain a Power Charge.', 'Loot: Restore 2 flask charges.', 'At the start of your turn, choose a flask. Give that flask 1 charge.', 'Loot: Allied exiles regain 4 life.', 'At the end of your turn, restore 4 life to allied exiles.', 'Loot: Draw 2 cards.', 'Range', 'Gain 3 Rage when this pack attacks.', 'At the end of your turn, Charges', 'Focused, gain 2 life.', ' Leech', 'Guard, at the end of your turn Fortify: 2.', 'Ignites, gain 1 damage', 'Chills, gain 1 life', 'Shocks, gain 1 energy shield', 'Poison 3', 'Bleed 3', 'Critical Strike: Gain 3 damage', 'Critical Strike: Restore 3 life.', '+3/0/0', '+0/3/0', '+0/0/3', '+2/2/0', '+3/0/2', '+0/2/2', '+2/1/1'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 3 extra Alteration orbs and 2 extra Chaos orbs.', 'At the start of your turn, gain 2 extra Alteration orbs and 1 extra Chaos orb.', 'Loot: Gain a Frenzy Charge', 'At the end of your turn gain a Frenzy Charge.', 'Loot: Gain an Endurance Charge.', 'At the end of your turn gain an Endurance Charge', 'Loot: Gain a Power Charge.', 'At the end of your turn gain a Power Charge.', 'Loot: Restore 2 Flask charges', 'At the start of your turn choose a flask and give that flask a charge', 'Loot: Allied exiles regain 4 life.', 'At the end of your turn, restore 4 life to allied exiles.', 'Loot: Draw 2 cards.', 'Range', 'Gain 3 Rage when this pack attacks.', 'At the end of your turn, Charges.', 'Focused, Gain 2 Life', ' Leech', 'Guard, At the end of your turn Fortify: 3', 'Ignites, gain 2 damage', 'Chills, gain 2 Life', 'Shocks, gain 2 energy shield', 'Poison 3', 'Bleed 3', 'Critical Strike: Gain 3 damage', 'Critical Strike: Restore 3 life', '+4/0/0', '+0/4/0', '+0/0/3', '+3/3/0', '+3/0/2', '+0/3/2', '+2/2/1'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gain 3 extra Alteration orbs and 2 extra Chaos orbs.', 'At the start of your turn, gain 2 extra Alteration orbs and 1 extra Chaos orb.', 'Loot: Gain a Frenzy Charge', 'At the end of your turn gain a Frenzy Charge', 'Loot: Gain an Endurance Charge', 'At the end of your turn gain an Endurance Charge', 'Loot: Gain a Power Charge', 'At the end of your turn gain a Power Charge', 'Loot: Restore 3 Flask Charges', 'At the start of your turn choose a flask give that flask 2 Charges', 'Loot: Allied exiles regain 4 life.', 'At the end of your turn, restore 4 life to allied exiles.', 'Loot: Draw 2 cards', 'Range', 'Gain 3 Rage when this pack attacks.', 'At the end of your turn, Charges', 'Focused, Gain 2 Life', ' Leech', 'Guard, At the end of your turn Fortify: 3', 'Ignites, gain 2 damage', 'Chills, gain 2 Life', 'Shocks, gain 2 energy shield', 'Poison 4', 'Bleed 4', 'Critical Strike: Gain 4 damage', 'Critical Strike: Restore 3 life', '+4/0/0', '+0/4/0', '+0/0/3', '+3/3/0', '+3/0/2', '+0/3/2', '+2/2/1'],
#             ['The next mods this pack rolls are Lucky.', 'Loot: Gains 3/3/1 extra Alteration/Chaos/Exalted', 'At the start of your turn, gain 2/1/1 extra Alteration/Chaos/Exalted', 'Loot: Gain a Frenzy Charge', 'At the end of your turn gain a Frenzy Charge', 'Loot: Gain an Endurance Charge', 'At the end of your turn gain an Endurance Charge', 'Loot: Gain a Power Charge', 'At the end of your turn gain a Power Charge', 'Loot: Restore 3 Flask Charges', 'At the start of your turn choose a flask give that flask 2 Charges', 'Loot: Allied exiles regain 5 life.', 'At the end of your turn, restore 5 life to allied exiles.', 'Loot: Draw 3 cards', 'Range', 'Gain 4 Rage when this pack attacks.', 'At the end of your turn, Charges', 'Focused, Gain 3 Life', ' Leech', 'Guard, At the end of your turn Fortify: 3', 'Ignites, gain 3 damage', 'Chills, gain 3 Life', 'Shocks, gain 3 energy shield', 'Poison 4', 'Bleed 4', 'Critical Strike: Gain 4 damage', 'Critical Strike: Restore 4 life', '+5/0/0', '+0/5/0', '+0/0/4', '+4/4/0', '+4/0/2', '+0/3/3', '+2/2/2']]

prefixList=[["N/A",
"N/A",
"N/A",
"Ignites",
"Shocks",
"N/A",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 1 Rage.",
"+1/0/0",
"+0/1/0",
"N/A",
"N/A",
"N/A",
"N/A",
"N/A"],
            ["Guards",
"N/A",
"At the end of your turn, this pack restores 1 life to itself.",
"Ignites",
"Shocks",
"N/A",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 1 Rage.",
"+1/0/0",
"+0/1/0",
"+0/0/1",
"N/A",
"N/A",
"N/A",
"N/A"],
            ["Guards",
"N/A",
"At the end of your turn, this pack restores 1 life to itself.",
"Ignites",
"Shocks",
"N/A",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 1 Rage.",
"+1/0/0",
"+0/1/0",
"+0/0/1",
"+1/1/0",
"N/A",
"+1/0/1",
"N/A"],
            ["Guards",
"N/A",
"At the end of your turn, this pack restores 1 life to itself.",
"Ignites",
"Shocks",
"N/A",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 1 Rage.",
"+2/0/0",
"+0/2/0",
"+0/0/1",
"+1/1/0",
"+0/1/1",
"+1/0/1",
"N/A"],
            ["Guards",
"At the end of your turn, Fortify: 1.",
"At the end of your turn, this pack restores 2 life to itself.",
"Ignites",
"Shocks",
"N/A",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 2 Rage.",
"+2/0/0",
"+0/2/0",
"+0/0/2",
"+1/1/0",
"+0/1/1",
"+1/0/1",
"N/A"],
            ["Guards",
"At the end of your turn, Fortify: 1.",
"At the end of your turn, this pack restores 2 life to itself.",
"Ignites",
"Shocks",
"Freezes",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 2 Rage.",
"+2/0/0",
"+0/2/0",
"+0/0/2",
"+1/1/0",
"+0/1/1",
"+1/0/1",
"+1/1/1"],
            ["Guards",
"At the end of your turn, Fortify: 1.",
"At the end of your turn, this pack restores 2 life to itself.",
"Ignites",
"Shocks",
"Freezes",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 2 Rage.",
"+2/0/0",
"+0/2/0",
"+0/0/2",
"+1/1/0",
"+0/1/1",
"+1/0/1",
"+1/1/1"],
            ["Guards",
"At the end of your turn, Fortify: 1.",
"At the end of your turn, this pack restores 3 life to itself.",
"Ignites",
"Shocks",
"Freezes",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 3 Rage.",
"+3/0/0",
"+0/3/0",
"+0/0/3",
"+2/2/0",
"+0/2/2",
"+2/0/2",
"+1/1/1"],
            ["Guards",
"At the end of your turn, Fortify: 2.",
"At the end of your turn, this pack restores 3 life to itself.",
"Ignites",
"Shocks",
"Freezes",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 3 Rage.",
"+3/0/0",
"+0/3/0",
"+0/0/3",
"+2/2/0",
"+0/2/2",
"+2/0/2",
"+1/1/1"],
            ["Guards",
"At the end of your turn, Fortify: 2.",
"At the end of your turn, this pack restores 3 life to itself.",
"Ignites",
"Shocks",
"Freezes",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 3 Rage.",
"+3/0/0",
"+0/3/0",
"+0/0/3",
"+2/2/0",
"+0/2/2",
"+2/0/2",
"+1/1/1"],
            ["Guards",
"At the end of your turn, Fortify: 2.",
"At the end of your turn, this pack restores 4 life to itself.",
"Ignites",
"Shocks",
"Freezes",
"Chills",
"At the end of your turn, this pack Charges",
"When this pack attacks, gain 4 Rage.",
"+4/0/0",
"+0/4/0",
"+0/0/4",
"+2/2/0",
"+0/2/2",
"+2/0/2",
"+2/2/2"]]

suffixList=[["N/A",
"N/A",
"At the end of your turn, gain a Frenzy Charge.",
"N/A",
"N/A",
"N/A",
"N/A",
"Range",
"N/A",
"N/A",
"Loot: Draw 1 card.",
"N/A",
"N/A",
"Bleed",
"Poison",
"N/A"],
            ["N/A",
"N/A",
"At the end of your turn, gain a Frenzy Charge.",
"N/A",
"N/A",
"N/A",
"N/A",
"Range",
"N/A",
"At the end of your turn, restore 1 life to the allied Exile.",
"Loot: Draw 1 card.",
"Loot: Give allied packs +1/1/0.",
"Loot: Spawn 1 1/1/0 Unique Parasite.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"N/A",
"N/A",
"Leech",
"Range",
"N/A",
"At the end of your turn, restore 1 life to the allied Exile.",
"Loot: Draw 1 card.",
"Loot: Give allied packs +1/1/0.",
"Loot: Spawn 1 1/1/0 Unique Parasite.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"N/A",
"N/A",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 1 charge.",
"At the end of your turn, restore 1 life to the allied Exile.",
"Loot: Draw 1 card.",
"Loot: Give allied packs +1/1/0.",
"Loot: Spawn 1 1/1/0 Unique Parasite.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"N/A",
"N/A",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 1 charge.",
"At the end of your turn, restore 1 life to the allied Exile.",
"Loot: Draw 1 card.",
"Loot: Give allied packs +1/1/0.",
"Loot: Spawn 1 1/1/0 Unique Parasite.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"Critical Strike: Shatter the Critically Struck pack.",
"N/A",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 1 charge.",
"At the end of your turn, restore 2 life to the allied Exile.",
"Loot: Draw 2 cards.",
"Loot: Give allied packs +1/1/0.",
"Loot: Spawn 2 1/1/0 Unique Parasites.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"Critical Strike: Shatter the Critically Struck pack.",
"N/A",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 2 charges.",
"At the end of your turn, restore 2 life to the allied Exile.",
"Loot: Draw 2 cards.",
"Loot: Give allied packs +2/2/0.",
"Loot: Spawn 2 1/1/0 Unique Parasites.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"Critical Strike: Shatter the Critically Struck pack.",
"Critical Strike: This pack Charges.",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 2 charges.",
"At the end of your turn, restore 2 life to the allied Exile.",
"Loot: Draw 2 cards.",
"Loot: Give allied packs +2/2/0.",
"Loot: Spawn 2 1/1/0 Unique Parasites.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"Critical Strike: Shatter the Critically Struck pack.",
"Critical Strike: This pack Charges.",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 2 charges.",
"At the end of your turn, restore 2 life to the allied Exile.",
"Loot: Draw 2 cards.",
"Loot: Give allied packs +2/2/0.",
"Loot: Spawn 2 1/1/0 Unique Parasites.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"Critical Strike: Shatter the Critically Struck pack.",
"Critical Strike: This pack Charges.",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 3 charges.",
"At the end of your turn, restore 2 life to the allied Exile.",
"Loot: Draw 2 cards.",
"Loot: Give allied packs +2/2/0.",
"Loot: Spawn 3 1/1/0 Unique Parasites.",
"Bleed",
"Poison",
"Focused"],
            ["At the end of your turn, gain a Power Charge.",
"At the end of your turn, gain an Endurance Charge.",
"At the end of your turn, gain a Frenzy Charge.",
"Critical Strike: Restore this pack to full life.",
"Critical Strike: Shatter the Critically Struck pack.",
"Critical Strike: This pack Charges.",
"Leech",
"Range",
"At the end of your turn, target a flask. That flask gains 3 charges.",
"At the end of your turn, restore 3 life to the allied Exile.",
"Loot: Draw 3 cards.",
"Loot: Give allied packs +2/2/0.",
"Loot: Spawn 3 1/1/0 Unique Parasites.",
"Bleed",
"Poison",
"Focused"]]


modListPrefs=prefixList[turnCounter-1]
modListSufs=suffixList[turnCounter-1]

#modlist=masterlist[turnCounter-1]
#modlist=metaMods+chargeMods+flaskMods+lifeGainMods+cardDrawMods+offenseKeywordMods+defenseKeywordMods+ailmentMods+physAilmentMods+critMods+damageMods+lifeMods+defenseMods+hybridMods

def turnUp():
    global turnCounter
    global modlist
    global modListPrefs
    global modListSufs

    if turnCounter!=11:
        turnCounter += 1
        modListPrefs = prefixList[turnCounter - 1]
        modListSufs = suffixList[turnCounter - 1]
    turnButton.config(text="Turn: "+str(turnCounter))

def createPack():
    global modTypesPrefix
    global modTypesSuffix
    global packNames
    global packPrefs
    global packSufs
    global packTypesPrefs
    global packTypesSufs
    global packNumber

    packPrefs.append([])
    packSufs.append([])
    rarity.append("Normal")


    if playerName == 'Singletary':
        options=['arse','ass','asshole','bastard','bitch','bollocks','brotherfucker','bugger','bullshit','child-fucker','Christ on a bike','Christ on a cracker','crap','cunt','damn','effing','fatherfucker','frigger','fuck','goddamn','godsdamn','hell','holy shit','horseshit','Jesus Christ','Jesus fuck','Jesus H. Christ','Jesus Harold Christ','Jesus wept','Jesus, Mary and Joseph','Judas Priest','motherfucker','nigga','prick','shit','shit ass','shitass','sisterfucker','slut','son of a bitch','son of a whore','sweet Jesus','anal','anus','arse','ass','ballsack','balls','bastard','bitch','biatch','bloody','blowjob','blow job','bollock','bollok','boner','boob','bugger','bum','butt','buttplug','clitoris','cock','coon','crap','cunt','damn','dick','dildo','dyke','fag','feck','fellate','fellatio','felching','fuck','f u c k','fudgepacker','fudge packer','flange','Goddamn','God damn','hell','homo','jerk','jizz','knobend','knob end','labia','lmao','lmfao','muff','nigger','nigga','omg','penis','piss','poop','prick','pube','pussy','queer','scrotum','sex','shit','s hit','sh1t','slut','smegma','spunk','tit','tosser','turd','twat','vagina','wank','whore','wtf''a55','a55hole','aeolus','ahole','anal','analprobe','anilingus','anus','areola','areole','arian','aryan','ass','assbang','assbanged','assbangs','asses','assfuck','assfucker','assh0le','asshat','assho1e','ass hole','assholes','assmaster','assmunch','asswipe','asswipes','azazel','azz','b1tch','babe','babes','ballsack','bang','banger','barf','bastard','bastards','bawdy','beaner','beardedclam','beastiality','beatch','beater','beaver','beer','beeyotch','beotch','biatch','bigtits','big tits','bimbo','bitch','bitched','bitches''bitchy','blow job','blow','blowjob','blowjobs','bod','bodily','boink','bollock','bollocks','bollok','bone','boned','boner','boners','bong','boob','boobies','boobs','booby','booger','bookie','bootee','bootie','booty','booze','boozer','boozy','bosom','bosomy','bowel','bowels','bra','brassiere','breast','breasts','bugger','bukkake','bullshit','bull shit','bullshits','bullshitted','bullturds','bung','busty','butt','butt fuck','buttfuck','buttfucker','buttfucker','buttplug','c.0.c.k','c.o.c.k.','c.u.n.t','c0ck','c-0-c-k','caca','cahone','cameltoe','carpetmuncher','cawk','cervix','chinc','chincs','chink','chink','chode','chodes','cl1t','climax','clit','clitoris','clitorus','clits','clitty','cocain','cocaine','cock','c-o-c-k','cockblock','cockholster','cockknocker','cocks','cocksmoker','cocksucker','cock sucker','coital','commie','condom','coon','coons','corksucker','crabs','crack','cracker','crackwhore','crap','crappy','cum','cummin','cumming','cumshot','cumshots','cumslut','cumstain','cunilingus','cunnilingus','cunny','cunt','cunt','c-u-n-t','cuntface','cunthunter','cuntlick','cuntlicker','cunts','d0ng','d0uch3','d0uche','d1ck','d1ld0','d1ldo','dago','dagos','dammit','damn','damned','damnit','dawgie-style','dick','dickbag','dickdipper','dickface','dickflipper','dickhead','dickheads','dickish','dick-ish','dickripper','dicksipper','dickweed','dickwhipper','dickzipper','diddle','dike','dildo','dildos','diligaf','dillweed','dimwit','dingle','dipship','doggie-style','doggy-style','dong','doofus','doosh','dopey','douch3','douche','douchebag','douchebags','douchey','drunk','dumass','dumbass','dumbasses','dummy','dyke','dykes','ejaculate','enlargement','erect','erection','erotic','essohbee','extacy','extasy','f.u.c.k','fack','fag','fagg','fagged','faggit','faggot','fagot','fags','faig','faigt','fannybandit','fart','fartknocker','fat','felch','felcher','felching','fellate','fellatio','feltch','feltcher','fisted','fisting','fisty','floozy','foad','fondle','foobar','foreskin','freex','frigg','frigga','fubar','fuck','f-u-c-k','fuckass','fucked','fucked','fucker','fuckface','fuckin','fucking','fucknugget','fucknut','fuckoff','fucks','fucktard','fuck-tard','fuckup','fuckwad','fuckwit','fudgepacker','fuk','fvck','fxck','gae','gai','ganja','gay','gays','gey','gfy','ghay','ghey','gigolo','glans','goatse','godamn','godamnit','goddam','goddammit','goddamn','goldenshower','gonad','gonads','gook','gooks','gringo','gspot','g-spot','gtfo','guido','h0m0','h0mo','handjob','hard on','he11','hebe','heeb','hell','hemp','heroin','herp','herpes','herpy','hitler','hiv','hobag','hom0','homey','homo','homoey','honky','hooch','hookah','hooker','hoor','hootch','hooter','hooters','horny','hump','humped','humping','hussy','hymen','inbred','incest','injun','j3rk0ff','jackass','jackhole','jackoff','jap','japs','jerk','jerk0ff','jerked','jerkoff','jism','jiz','jizm','jizz','jizzed','junkie','junky','kike','kikes','kill','kinky','kkk','klan','knobend','kooch','kooches','kootch','kraut','kyke','labia','lech','leper','lesbians','lesbo','lesbos','lez','lezbian','lezbians','lezbo','lezbos','lezzie','lezzies','lezzy','lmao','lmfao','loin','loins','lube','lusty','mams','massa','masterbate','masterbating','masterbation','masturbate','masturbating','masturbation','maxi','menses','menstruate','menstruation','meth','m-fucking','mofo','molest','moolie','moron','motherfucka','motherfucker','motherfucking','mtherfucker','mthrfucker','mthrfucking','muff','muffdiver','murder','muthafuckaz','muthafucker','mutherfucker','mutherfucking','muthrfucking','nad','nads','naked','napalm','nappy','nazi','nazism','negro','nigga','niggah','niggas','niggaz','nigger','nigger','niggers','niggle','niglet','nimrod','ninny','nipple','nooky','nympho','opiate','opium','oral','orally','organ','orgasm','orgasmic','orgies','orgy','ovary','ovum','ovums','p.u.s.s.y.','paddy','paki','pantie','panties','panty','pastie','pasty','pcp','pecker','pedo','pedophile','pedophilia','pedophiliac','pee','peepee','penetrate','penetration','penial','penile','penis','perversion','peyote','phalli','phallic','phuck','pillowbiter','pimp','pinko','piss','pissed','pissoff','piss-off','pms','polack','pollock','poon','poontang','porn','porno','pornography','pot','potty','prick','prig','prostitute','prude','pube','pubic','pubis','punkass','punky','puss','pussies','pussy','pussypounder','puto','queaf','queef','queef','queer','queero','queers','quicky','quim','racy','rape','raped','raper','rapist','raunch','rectal','rectum','rectus','reefer','reetard','reich','retard','retarded','revue','rimjob','ritard','rtard','r-tard','rum','rump','rumprammer','ruski','s.h.i.t.','s.o.b.','s0b','sadism','sadist','scag','scantily','schizo','schlong','screw','screwed','scrog','scrot','scrote','scrotum','scrud','scum','seaman','seamen','seduce','semen','sex','sexual','sh1t','s-h-1-t','shamedame','shit','s-h-i-t','shite','shiteater','shitface','shithead','shithole','shithouse','shits','shitt','shitted','shitter','shitty','shiz','sissy','skag','skank','slave','sleaze','sleazy','slut','slutdumper','slutkiss','sluts','smegma','smut','smutty','snatch','sniper','snuff','s-o-b','sodom','souse','soused','sperm','spic','spick','spik','spiks','spooge','spunk','steamy','stfu','stiffy','stoned','strip','stroke','stupid','suck','sucked','sucking','sumofabiatch','t1t','tampon','tard','tawdry','teabagging','teat','terd','teste','testee','testes','testicle','testis','thrust','thug','tinkle','tit','titfuck','titi','tits','tittiefucker','titties','titty','tittyfuck','tittyfucker','toke','toots','tramp','transsexual','trashy','tubgirl','turd','tush','twat','twats','ugly','undies','unwed','urinal','urine','uterus','uzi','vag','vagina','valium','viagra','virgin','vixen','vodka','vomit','voyeur','vulgar','vulva','wad','wang','wank','wanker','wazoo','wedgie','weed','weenie','weewee','weiner','weirdo','wench','wetback','wh0re','wh0reface','whitey','whiz','whoralicious','whore','whorealicious','whored','whoreface','whorehopper','whorehouse','whores','whoring','wigger','womb','woody','wop','wtf','x-rated','xxx','yeasty','yobbo','zoophile']
        n = random.choice(options)
    else:
        n = easygui.enterbox("Pack Name? ")

    packNames.append(n)
    packs.append(Label(m, text=rarity[packNumber]+ ' ' + packNames[packNumber] + ' ' +str(packNumber+1)+'\nPrefixes: '+'\nSuffixes: '))
    packs[packNumber].pack()
    packNumber+=1

    packTypesPrefs.append([])
    packTypesSufs.append([])

def removePack():
    global packs
    global packNumber
    global rarity

    n = easygui.enterbox("Pack #? ")
    packs[int(n)-1].pack_forget()

def rollMods(packNumber, reps):
    global modTypesPrefix
    global modTypesSuffix
    global packNames
    global packPrefs
    global packSufs
    global packTypesPrefs
    global packTypesSufs
    global prefOrSuff

    prefOrSuff=2

    if len(packPrefs[packNumber])==0 and len(packSufs[packNumber])==0:
        prefOrSuff=random.randint(0,1)

    elif len(packPrefs[packNumber])==0 and len(packSufs[packNumber])==1:
        prefOrSuff=0

    elif len(packPrefs[packNumber])==1 and len(packSufs[packNumber])==0:
        prefOrSuff=1

    elif len(packPrefs[packNumber])==1 and len(packSufs[packNumber])==1:
        prefOrSuff=random.randint(0,1)

    elif len(packPrefs[packNumber])!=2 and len(packSufs[packNumber])==2:
        prefOrSuff=0

    elif len(packPrefs[packNumber])==2 and len(packSufs[packNumber])!=2:
        prefOrSuff=1

    elif len(packPrefs[packNumber])==2 and len(packSufs[packNumber])==2:
        easygui.textbox("Packs cannot have more than 4 mods.")


    a=random.randint(0,15)

    if prefOrSuff == 0:
        while modListPrefs[a] in packPrefs[packNumber] or modListPrefs[a] == 'N/A':
            a = random.randint(0, 15)

        if modTypesPrefix[a] not in packTypesPrefs[packNumber]:
                packTypesPrefs[packNumber].append(modTypesPrefix[a])
                packPrefs[packNumber].append(modListPrefs[a])
                packs[packNumber].config(text=str(rarity[packNumber]+ ' ' + packNames[packNumber] + ' ' +str(packNumber+1)+'\nPrefixes: '+str(packPrefs[packNumber])+'\nSuffixes: '+str(packSufs[packNumber])))
        else:
            if reps > 0:
                rollMods(packNumber, reps - 1)
            else:
                rollMods(packNumber, 0)

    if prefOrSuff==1:
        while modListSufs[a] in packSufs[packNumber] or modListSufs[a] == 'N/A':
            a = random.randint(0, 15)

        if modTypesSuffix[a] not in packTypesSufs[packNumber]:
                packTypesSufs[packNumber].append(modTypesSuffix[a])
                packSufs[packNumber].append(modListSufs[a])
                packs[packNumber].config(text=str(rarity[packNumber]+ ' ' + packNames[packNumber] + ' ' +str(packNumber+1)+'\nPrefixes: '+str(packPrefs[packNumber])+'\nSuffixes: '+str(packSufs[packNumber])))
        else:
            if reps > 0:
                rollMods(packNumber, reps - 1)
            else:
                rollMods(packNumber, 0)

    if reps > 0:
        rollMods(packNumber, reps - 1)


def trans():
    global rarity
    global packs

    n = easygui.enterbox("Pack #? ")
    if rarity[int(n)-1]!="Normal":
        easygui.textbox("listen here tranny, that's not a normal pack")
    else:
        a = random.randint(1, 2)
        rarity[int(n) - 1] = "Magic"
        rollMods(int(n)-1,a-1)

def alt():
    global packPrefs
    global packSufs
    global packTypesPrefs
    global packTypesSufs

    n = easygui.enterbox("Pack #? ")
    if rarity[int(n)-1]=="Magic":
        packPrefs[int(n)-1]=[]
        packTypesPrefs[int(n)-1]=[]
        packSufs[int(n)-1]=[]
        packTypesSufs[int(n)-1]=[]

        a=random.randint(1,2)
        rollMods(int(n)-1,a-1)
    else:
        easygui.textbox("RAHHHHHHHHHHHH NOT MAGIC")

def regal():
    global rarity
    global packs

    n = easygui.enterbox("Pack #? ")
    if rarity[int(n)-1]=="Magic":
        rarity[int(n) - 1] = "Rare"
        rollMods(int(n) - 1, 0)
    else:
        easygui.textbox("not magique lil slut")

def chaos():
    global whichMods

    n=easygui.enterbox("Pack #? ")
    if rarity[int(n)-1]=="Rare":
        packPrefs[int(n)-1]=[]
        packTypesPrefs[int(n)-1]=[]
        packSufs[int(n)-1]=[]
        packTypesSufs[int(n)-1]=[]

        a=random.randint(3,4)
        print(a)
        rollMods(int(n)-1,a-1)
    else:
        easygui.textbox("REEEEEEEEE NOT RARE")


def alch():
    global rarity
    global packs

    n = easygui.enterbox("Pack #? ")
    if rarity[int(n)-1]!="Normal":
        easygui.textbox("listen here bitch, that's not a normal pack")
    else:
        a = random.randint(3, 4)
        rarity[int(n) - 1] = "Rare"
        rollMods(int(n)-1,a-1)


def aug():
    n = easygui.enterbox("Pack #? ")
    if len(packPrefs[int(n)-1])+len(packSufs[int(n)-1])!=1:
        easygui.textbox("cannot augment, cunt.")
    else:
        rollMods(int(n)-1,0)

def exalt():
    n = easygui.enterbox("Pack #? ")
    if rarity[int(n)-1]!="Rare":
        easygui.textbox("not rare lil slut")
    elif len(packPrefs[int(n)-1])+len(packSufs[int(n)-1])>3:
        easygui.textbox("too many mods cumwhore")
    else:
        rollMods(int(n)-1,0)

turnButton=tkinter.Button(m, text="Turn: "+str(turnCounter), width=25, command=turnUp)
turnButton.pack()

packButton=tkinter.Button(m, text="Make New Pack", width=25, command=createPack)
packButton.pack()

removePackButton=tkinter.Button(m, text="Remove Pack", width=25, command=removePack)
removePackButton.pack()

modButton=tkinter.Button(m, text="Orb of Transmutation", width=25, command=trans)
modButton.pack()

modButton=tkinter.Button(m, text="Orb of Alteration", width=25, command=alt)
modButton.pack()
#
modButton=tkinter.Button(m, text="Orb of Augmentation", width=25, command=aug)
modButton.pack()
#
modButton=tkinter.Button(m, text="Regal Orb", width=25, command=regal)
modButton.pack()
#
modButton=tkinter.Button(m, text="Orb of Alchemy", width=25, command=alch)
modButton.pack()
#
modButton=tkinter.Button(m, text="Chaos Orb", width=25, command=chaos)
modButton.pack()
#
modButton=tkinter.Button(m, text="Exalted Orb", width=25, command=exalt)
modButton.pack()

# modButton=tkinter.Button(m, text="rolltest", width=25, command=rollMods)
# modButton.pack()

m.mainloop()