import requests
import RiotConsts as Consts

class RiotAPI(object):

    def __init__(self,api_key,region=Consts.Regions['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self,api_url,params={}):
        args = {'api_key':self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            Consts.URL['base'].format(
                proxy=self.region,
                url=api_url
                ),
                params = args
        )
        print (response.url)
        return response.json()

    def get_champion(self):
        api_url = Consts.URL['champion'].format(
            region=self.region,
            version = Consts.API_VERSIONS['champion']
        )
        return self._request(api_url)

    def get_champion_by_id(self,champId):
        api_url = Consts.URL['champion_by_id'].format(
        region=self.region,
            version = Consts.API_VERSIONS['champion'],
            id = champId
        )
        return self._request(api_url)

    def get_current_game(self,platform,id):
        api_url = Consts.URL['current_game'].format(
            platformId = platform,
            summonerId = id
        )
        return self._request(api_url)

    def get_featured_game(self):
        api_url = Consts.URL['featured_game']
        return self._request(api_url)

    def get_game_by_summoner_id(self,id):
        api_url = Consts.URL['game_by_summoner_id'].format(
            region=self.region,
            version = Consts.API_VERSIONS['game'],
            summonerID = id
        )
        return self._request(api_url)

    def get_league_by_summoner_id(self,id,entry=False):
        if entry == True:
            api_url = Consts.URL['league_by_summoner_id_entry'].format(
                region=self.region,
                version = Consts.API_VERSIONS['league'],
                summonerIds = id
            )
        else:
            api_url = Consts.URL['league_by_summoner_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['league'],
                summonerIds = id
            )
        return self._request(api_url)

    def get_league_by_team_id(self,id,entry=False):
        if entry == True:
            api_url = Consts.URL['league_by_team_ids_entry'].format(
                region=self.region,
                version = Consts.API_VERSIONS['league'],
                teamIds = id
            )
        else:
            api_url = Consts.URL['league_by_team_ids'].format(
                region=self.region,
                version = Consts.API_VERSIONS['league'],
                teamIds = id
            )
        return self._request(api_url)

    def get_league_challanger(self):
        api_url = Consts.URL['league_challenger'].format(
            region=self.region,
            version=Consts.API_VERSIONS['league']
        )
        return self.request(api_url)

    def get_league_master(self):
        api_url = Consts.URL['league_master'].format(
            region=self.region,
            version=Consts.API_VERSIONS['league']
        )
        return self.request(api_url)

    def get_champion_static(self,champId=-1):
        if champId == -1:
            api_url = Consts.URL['champions_static'].format(
                region=self.region,
                version=Consts.API_VERSIONS['lol-static-data']
            )
        else:
            api_url = Consts.URL['champion_by_id_static'].format(
                region=self.region,
                version=Consts.API_VERSIONS['lol-static-data'],
                id = champId
            )
        return self._request(api_url)

    def get_items_static(self,itemId = -1):
        if itemId == -1:
            api_url = Consts.URL['items_static'].format(
                region=self.region,
                version=Consts.API_VERSIONS['lol-static-data']
            )
        else:
            api_url = Consts.URL['item_by_id_static'].format(
                region=self.region,
                version=Consts.API_VERSIONS['lol-static-data'],
                id = itemId
            )
        return self._request(api_url)

    def get_langauge_strings_static(self):
        api_url = Consts.URL['language_strings_static'].format(
            region=self.region,
            version = Consts.API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_languages_static(self):
        api_url = Consts.URL['languages_static'].format(
            region=self.region,
            version = Consts.API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_map_static(self):
        api_url = Consts.URL['map_static'].format(
            region=self.region,
            version = Consts.API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_mastery_static(self,masteryId = -1):
        if masteryId == -1:
            api_url = Consts.URL['mastery_static'].format(
                region=self.region,
                version = Consts.API_VERSIONS['lol-static-data']
            )
        else:
            api_url = Consts.URL['mastery_by_id_static'].format(
                region=self.region,
                version = Consts.API_VERSIONS['lol-static-data'],
                id = masteryId
            )
        return self._request(api_url)

    def get_realm_static(self):
        api_url = Consts.URL['realm_static'].format(
            region=self.region,
            version = Consts.API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_rune_static(self,runeID=-1):
        if runeID == -1:
            api_url = Consts.URL['rune_static'].format(
                region=self.region,
                version = Consts.API_VERSIONS['lol-static-data']
            )
        else:
            api_url = Consts.URL['rune_by_id_static'].format(
                region=self.region,
                version = Consts.API_VERSIONS['lol-static-data'],
                id = runeId
            )
        return self._request(api_url)

    def get_summoner_spell_static(self, spellId=-1):
        if spellId == -1:
            api_url = Consts.URL['summoner_spell_static'].format(
                region=self.region,
                version = Consts.API_VERSIONS['lol-static-data']
            )
        else:
            api_url = Consts.URL['summoner_spell_by_id_static'].format(
                region=self.region,
                version = Consts.API_VERSIONS['lol-static-data'],
                id = spellId
            )
        return self._request(api_url)

    def get_versions(self):
        api_url = Consts.URL['versions_static'].format(
            region=self.region,
            version = Consts.API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_shards(self,r=""):
        if r=="":
            api_url = Consts.URL['shards']
        else:
            api_url = Consts.URL['shards_by_region'].format(
                region=self.region,
            )

    def get_match(self,matchID):
        api_url = Consts.URL['match_by_id'].format(
            region=self.region,
            version = Consts.API_VERSIONS['match'],
            id = matchID
        )
        return self._request(api_url)

    def get_match_history(self,id,list=False):
        if list == True:
            api_url = Consts.URL['match_list_by_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['matchlist'],
                summonerID = id
            )
        else:
            api_url = Consts.URL['match_history_by_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['matchhistory'],
                summonerID = id
            )
        return self._request(api_url)

    def get_stats(self,id,ranked=False):
        if ranked == True:
            api_url = Consts.URL['stats_ranked_by_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['stats'],
                summonerId = id
            )
        else:
            api_url = Consts.URL['stats_summary_by_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['stats'],
                summonerId = id
            )
        return self._request(api_url)

    def get_summoner_by_name(self,name):
        api_url = Consts.URL['summoner_by_name'].format(
            region=self.region,
            version = Consts.API_VERSIONS['summoner'],
            names = name
        )
        return self._request(api_url)

    def get_summoner_by_id(self,id):
        api_url = Consts.URL['summoner_by_id'].format(
            region=self.region,
            version = Consts.API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_summoner_mastery(self,id):
        api_url = Consts.URL['summoner_mastery_by_id'].format(
            region=self.region,
            version = Consts.API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_summoner_name(self,id):
        api_url = Consts.URL['summoner_name_by_id'].format(
            region=self.region,
            version = Consts.API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_summoner_runes(self,id):
        api_url = Consts.URL['summoner_runes_by_id'].format(
            region=self.region,
            version = Consts.API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_team(self,id,summoner=False):
        if summoner==True:
            api_url = Consts.URL['team_by_summoner_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['team'],
                summonerId = id
            )
        else:
            api_url = Consts.URL['team_by_team_id'].format(
                region=self.region,
                version = Consts.API_VERSIONS['team'],
                summonerId = id
            )
        return self._request(api_url)
