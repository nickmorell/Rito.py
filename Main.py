from RiotAPI import RiotAPI

def main():
    api = RiotAPI('b1f1e449-37bb-4d09-97e7-fecce30b5fb7')
    #r = api.get_summoner_by_name('Pheonxfire')
    r = api.get_summoner_by_name('pheonxfire')
    print(r)

if __name__ == "__main__":
    main()

#iUltforCS = 44924079
