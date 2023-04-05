import time
from termcolor import colored
from data import *
import math

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return copper2gold(personCash['copper']) + silver2gold(personCash['silver']) + personCash['gold'] + platinum2gold(personCash['platinum'])

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_cost_food = ((COST_FOOD_HORSE_COPPER_PER_DAY * horses) + (COST_FOOD_HUMAN_COPPER_PER_DAY * people))* JOURNEY_IN_DAYS
    return round(copper2gold(total_cost_food),2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    test_list = []
    for people in list:
        if people[key] == value:
            test_list.append(people)
    return test_list

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    friends = getAdventuringPeople(friends)
    return getShareWithFriends(friends)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses:int, tents:int) -> float:
    total_horse_price = silver2gold(horses) * COST_HORSE_SILVER_PER_DAY * JOURNEY_IN_DAYS
    total_tent_price = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS / 7)
    total_rent = total_horse_price + total_tent_price
    return total_rent

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    thing_text = ""
    for things in items:
        thing_text +=(f"{things['amount']}{things['unit']} {things['name']}, ")
    thing_text = thing_text[:len(thing_text)-2]
    return thing_text

def getItemsValueInGold(items:list) -> float:
    total_price = 0
    for things in items:
        if things['price']['type'] == 'gold':
            total_price += things['price']['amount'] * things['amount']
        elif things['price']['type'] == 'silver':
            total_price += silver2gold(things['price']['amount'] * things['amount'])
        elif things['price']['type'] == 'copper':
            total_price += copper2gold(things['price']['amount'] * things['amount'])
        elif things['price']['type'] == 'platinum':
            total_price += platinum2gold(things['price']['amount'] * things['amount'])
    return round(total_price, 2)
##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    totaal_cash = 0
    for moneybags in people:
        totaal_cash += platinum2gold(moneybags['cash']['platinum'])
        totaal_cash += moneybags['cash']['gold']
        totaal_cash += silver2gold(moneybags['cash']['silver'])
        totaal_cash += copper2gold(moneybags['cash']['copper'])
    return round(totaal_cash, 2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    interested_people = []
    for people in investors:
        if people['profitReturn'] <= 10:
            interested_people.append(people)
    return interested_people

def getAdventuringInvestors(investors:list) -> list:
    adventuring_people = []
    for people in getInterestingInvestors(investors):
        if people['adventuring'] == True:
            adventuring_people.append(people)
    return adventuring_people

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    TotalInvestors = getAdventuringInvestors(investors)
    horses_invenstors = len(TotalInvestors)
    tents_invenstors = len(TotalInvestors)
    TotalCostInvenstors = getTotalRentalCost(horses_invenstors, tents_invenstors)
    TotalCostInvenstors += getJourneyFoodCostsInGold(len(TotalInvestors), horses_invenstors)
    for invenstor in TotalInvestors:
        TotalCostInvenstors += getItemsValueInGold(gear)
    return TotalCostInvenstors

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    Cost = (silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people) + (copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses)
    AmountofNights = math.floor(leftoverGold / Cost)
    return AmountofNights

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float: 
    cost = (silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people) + (copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses)
    total_cost = cost * nightsInInn
    return round(total_cost, 2)

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()