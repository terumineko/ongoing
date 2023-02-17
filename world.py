# choose your own adventure and scuffed dating sim in the works


# Races: Human, Elf.
# Unlock-able race: Halflings.
# Halflings have sub-races giving them different downsides and "buffs". Fish, felines, canines and birds.
#
# Fish: Works on a buff/de-buff system, needs water or will begin to be slow
# (higher chances of bad) and if past x time will straight up die
#
# Feline: Agile/lucky (higher chances of good overall), can't swim,
# untrustworthy (they pay more for their items from merchants or inns)
#
# Canine: Loyal (opposite of feline pays less), strong physical (higher crit chance), bad liar (low chance in deceit),
# gluttony (dies faster without eating, if not eaten more than twice the day before loses crit)
#
# Bird: Learns quicker (higher change in intellect),  can fly X amount, fragile (lower chance of dodge in combat),
# use feathers in combat max X (reset with rest)


player_name = None
race = None
halfling_unlocked = False
races = [
    {'e-name': 'Elf', 'e-desc': '''Elf
    The tall and pointy eared sexy humans, cough I mean elf... 
    Proficient in magic and with high intellect, masters of art they are often seen amongst the royal army!
    Or you know, in a bar... jamming out... you do whatever you please! 
    May it be spreading your art or climbing through the ranks as an elf you will do so with elegance.''',
     'unlocked': True},
    {'h-name': 'Human', 'h-desc': '''Human
     Also known as the basic bitch of any game, but hey we don't judge here (I am judging you).
     Humans are well... humans, they have endless but limited options. Sounds confusing? Well to put it simply, 
     you can be an adventurer that picks up magic as his weapon, or a simple trade merchant selling apples.
     However due to your endless options it is hard to truly master any like other races.''', 'unlocked': True},
    {'ha-name': 'Halfling', 'sub-races': [{'name': 'Fish', 'desc': '''Fish
    These halflings have fin like ears and their skin glimmers under the sun.
    Eyes glowing like the ocean they can't survive fully on land or in the sea. 
    Needing water but also not being able to breathe in water, they have good underwater mobility and have the
    ability of swapping between fish and human like legs which is why they were used as fishers.'''},
                                       {'name': 'Feline', 'desc': '''Feline
    With cat like ears and hands resembling paws, these halflings are agile and quick on their feet.
    Making them perfect for combat, being used as bodyguards for long travels and other dirty jobs.
    Which due to the type of jobs they are commonly found in they are considered untrustworthy by the average joe.
    These felines are also terrified of water and so do not possess the ability to swim.'''},
                                       {'name': 'Canine', 'desc': '''Canine
    The ones where females and males are the most distinct. 
    Males usually having strong features and builds and females being softer and skinnier. 
    While males are often seen in heavy duty jobs like construction, the females tend to be maids due to their loyalty. 
    Easily trusted however due to their habit of working hard they require more food than others in their everyday.'''},
                                       {'name': 'Bird', 'desc': '''Bird
    Scrawny looking with wings for arms and talons for feet, commonly found in stores working for merchants.
    They are quick to pick up basic knowledge and that's why they are fit to work with the public.
    They can fly however when humans pluck their feathers they are unable to fight back as they use them for combat.
    Having restricted combat everyday due to their fragile builds they found it easier to comply.'''}], 'ha-desc':
        '''Halfling
    Originally slaves due to their "bizarre" looks, halflings are half human half animal.
    Since they have been treated so roughly they have developed good senses and good resistances.
    Now finally given a chance, they excel at physical combat and are the perfect fit to be adventurers.
    Sadly due to their nature they still suffer from lack of knowledge and are not accepted into every establishment.
    ''', 'unlocked': False}]
yes = ['yes', 'y', 'yea', 'yeah', 'yep']
no = ['no', 'nope', 'nah', 'n']


while not player_race:
    print('Welcome to my game, this is a choose your own adventure text game')
    if not halfling_unlocked:
        choice = input().lower()
        print('''You have currently 3 options for your starter race.
              Human, Elf and Halfling. 
              Please pick what race you would like by typing choose followed by the desired race.
              To learn more about each race please write their respective names. ''')
        if choice == 'human':
            print(race['h-desc'])
        elif choice == 'halfling' and halfling_unlocked:
            print(race['ha-desc'])
        elif choice == 'elf':
            print(race['e-desc'])
        elif player_name.startswith('choose '):
            race = player_name.replace('choose ', '')
            if race == 'human':
                print()
            elif race == 'elf':
                print()
            elif race == 'halfling' and halfling_unlocked:
                print()
            else:
                print('Invalid option, please pick one of the available races.')
        else:
            print('Invalid option, please choose one of the available races.')


while not player_name:
    temp_name = input('What would you like to be called? ')
    name_correct = input(f'Is {temp_name} correct? (yes/no) ').lower()
    if name_correct in yes:
        player_name = temp_name
    elif name_correct not in no:
        print('Invalid option, please pick yes or no.')
