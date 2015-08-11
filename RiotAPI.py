import requests

URL = {
    'base': 'https://{proxy}.api.pvp.net/{url}',
    'champion': 'api/lol/{region}/v{version}/champion',
    'champion_by_id': 'api/lol/{region}//v{version}/champion/{id}',
    'current_game': 'observer-mode/rest/consumer/getSpectatorGameInfo/{platformId}/{summonerId}',
    'featured_game': 'observer-mode/rest/featured',
    'game_by_summoner_id': 'api/lol/{region}/v{version}/{summonerId}/recent',
    'league_by_summoner_id': 'api/lol/{region}/v{version}/league/by-summoner/{summonerIds}',
    'league_by_summoner_id_entry': 'api/lol/{region}/v{version}/league/by-summoner/{summonerIds}/entry',
    'league_by_team_ids': 'api/lol/{region}/v{version}/league/by-team/{teamIds}',
    'league_by_team_ids_entry': 'api/lol/{region}/v{version}/league/by-team/{teamIds}/entry',
    'league_challenger': 'api/lol/{region}/v{version}/league/challenger',
    'league_master': 'api/lol/{region}/v{version}/league/master',
    'champions_static': 'api/lol/static-data/{region}/v{version}/champion',
    'champion_by_id_static': 'api/lol/static-data/{region}/v{version}/champion/{id}',
    'items_static': 'api/lol/static-data/{region}/v{version}/item',
    'item_by_id_static': 'api/lol/static-data/{region}/v{version}/item/{id}',
    'language_strings_static': 'api/lol/static-data/{region}/v{version}/language-strings',
    'languages_static': 'api/lol/static-data/{region}/v{version}/languages',
    'map_static': 'api/lol/static-data/{region}/v{version}/map',
    'mastery_static': 'api/lol/static-data/{region}/v{version}/mastery',
    'mastery_by_id_static': 'api/lol/static-data/{region}/v{version}/mastery/{id}',
    'realm_static': 'api/lol/static-data/{region}/v{version}/realm',
    'rune_static': 'api/lol/static-data/{region}/v{version}/rune',
    'rune_by_id_static': 'api/lol/static-data/{region}/v{version}/rune/{id}',
    'summoner_spell_static': 'api/lol/static-data/{region}/v{version}/summoner-spell',
    'summoner_spell_by_id_static': 'api/lol/static-data/{region}/v{version}/summoner-spell/{id}',
    'versions_static': 'api/lol/static-data/{region}/v{version}/versions',
    'shards': 'shards',
    'shards_by_region': 'shards/{region}',
    'match_by_id': 'api/lol/{region}/v{version}/match/{matchId}',
    'match_history_by_id': 'api/lol/{region}/v{version}/matchhistory/{summonerId}',
    'match_list_by_id': 'api/lol/{region}/v{version}/matchlist/by-summoner/{summonerId}',
    'stats_ranked_by_id': 'api/lol/{region}/v{version}/stats/by-summoner/{summonerId}/ranked',
    'stats_summary_by_id': 'api/lol/{region}/v{version}/stats/by-summoner/{summonerId}/summary',
    'summoner_by_name': 'api/lol/{region}/v{version}/summoner/by-name/{names}',
    'summoner_by_id': 'api/lol/{region}/v{version}/summoner/{summonerId}',
    'summoner_mastery_by_id': 'api/lol/{region}/v{version}/summoner/{summonerId}/masteries',
    'summoner_name_by_id': 'api/lol/{region}/v{version}/summoner/{summonerId}/name',
    'summoner_runes_by_id': 'api/lol/{region}/v{version}/summoner/{summonerId}/runes',
    'team_by_summoner_id': 'api/lol/{region}/v{version}/team/by-summoner/{summonerId}',
    'team_by_team_id': 'api/lol/{region}/v{version}/team/{teamId}'
}

API_VERSIONS = {
    'champion':'1.2',
    'current-game':'1.0',
    'featured-game':'1.0',
    'game':'1.3',
    'league':'2.5',
    'lol-static-data':'1.2',
    'lol-status':'1.0',
    'match':'2.2',
    'matchhistory':'2.2',
    'matchlist':'2.2',
    'stats':'1.3',
    'summoner':'1.4',
    'team':'2.4'
}

Regions = {
    'brazil': 'br',
    'europe_nordic_and_east': 'eune',
    'europe_west': 'euw',
    'korea': 'kr',
    'latin_america_north': 'lan',
    'latin_america_south': 'las',
    'north_america': 'na',
    'oceania': 'oce',
    'turkey': 'tr',
    'russia': 'rs',
    'public_beta_enviroment': 'pbe',
    'global': 'global'
}


class RiotAPI(object):

    def __init__(self,api_key,region=Regions['north_america']):
        self.api_key = api_key
        self.region = region

    def _request(self,api_url,params={}):
        args = {'api_key':self.api_key}
        for key, value in params.items():
            if key not in args:
                args[key] = value
        response = requests.get(
            URL['base'].format(
                proxy=self.region,
                url=api_url
                ),
                params = args
        )
        print (response.url)
        return response.json()

    def get_champion(self):
        api_url = URL['champion'].format(
            region=self.region,
            version = API_VERSIONS['champion']
        )
        return self._request(api_url)

    def get_champion_by_id(self,champId):
        api_url = URL['champion_by_id'].format(
        region=self.region,
            version = API_VERSIONS['champion'],
            id = champId
        )
        return self._request(api_url)

    def get_current_game(self,platform,id):
        api_url = URL['current_game'].format(
            platformId = platform,
            summonerId = id
        )
        return self._request(api_url)

    def get_featured_game(self):
        api_url = URL['featured_game']
        return self._request(api_url)

    def get_game_by_summoner_id(self,id):
        api_url = URL['game_by_summoner_id'].format(
            region=self.region,
            version = API_VERSIONS['game'],
            summonerID = id
        )
        return self._request(api_url)

    def get_league_by_summoner_id(self,id,entry=False):
        if entry == True:
            api_url = URL['league_by_summoner_id_entry'].format(
                region=self.region,
                version = API_VERSIONS['league'],
                summonerIds = id
            )
        else:
            api_url = URL['league_by_summoner_id'].format(
                region=self.region,
                version = API_VERSIONS['league'],
                summonerIds = id
            )
        return self._request(api_url)

    def get_league_by_team_id(self,id,entry=False):
        if entry == True:
            api_url = URL['league_by_team_ids_entry'].format(
                region=self.region,
                version = API_VERSIONS['league'],
                teamIds = id
            )
        else:
            api_url = URL['league_by_team_ids'].format(
                region=self.region,
                version = API_VERSIONS['league'],
                teamIds = id
            )
        return self._request(api_url)

    def get_league_challanger(self):
        api_url = URL['league_challenger'].format(
            region=self.region,
            version=API_VERSIONS['league']
        )
        return self.request(api_url)

    def get_league_master(self):
        api_url = URL['league_master'].format(
            region=self.region,
            version=API_VERSIONS['league']
        )
        return self.request(api_url)

    def get_champion_static(self,champId=-1):
        if champId == -1:
            api_url = URL['champions_static'].format(
                region=self.region,
                version=API_VERSIONS['lol-static-data']
            )
        else:
            api_url = URL['champion_by_id_static'].format(
                region=self.region,
                version=API_VERSIONS['lol-static-data'],
                id = champId
            )
        return self._request(api_url)

    def get_items_static(self,itemId = -1):
        if itemId == -1:
            api_url = URL['items_static'].format(
                region=self.region,
                version=API_VERSIONS['lol-static-data']
            )
        else:
            api_url = URL['item_by_id_static'].format(
                region=self.region,
                version=API_VERSIONS['lol-static-data'],
                id = itemId
            )
        return self._request(api_url)

    def get_langauge_strings_static(self):
        api_url = URL['language_strings_static'].format(
            region=self.region,
            version = API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_languages_static(self):
        api_url = URL['languages_static'].format(
            region=self.region,
            version = API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_map_static(self):
        api_url = URL['map_static'].format(
            region=self.region,
            version = API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_mastery_static(self,masteryId = -1):
        if masteryId == -1:
            api_url = URL['mastery_static'].format(
                region=self.region,
                version = API_VERSIONS['lol-static-data']
            )
        else:
            api_url = URL['mastery_by_id_static'].format(
                region=self.region,
                version = API_VERSIONS['lol-static-data'],
                id = masteryId
            )
        return self._request(api_url)

    def get_realm_static(self):
        api_url = URL['realm_static'].format(
            region=self.region,
            version = API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_rune_static(self,runeID=-1):
        if runeID == -1:
            api_url = URL['rune_static'].format(
                region=self.region,
                version = API_VERSIONS['lol-static-data']
            )
        else:
            api_url = URL['rune_by_id_static'].format(
                region=self.region,
                version = API_VERSIONS['lol-static-data'],
                id = runeId
            )
        return self._request(api_url)

    def get_summoner_spell_static(self, spellId=-1):
        if spellId == -1:
            api_url = URL['summoner_spell_static'].format(
                region=self.region,
                version = API_VERSIONS['lol-static-data']
            )
        else:
            api_url = URL['summoner_spell_by_id_static'].format(
                region=self.region,
                version = API_VERSIONS['lol-static-data'],
                id = spellId
            )
        return self._request(api_url)

    def get_versions(self):
        api_url = URL['versions_static'].format(
            region=self.region,
            version = API_VERSIONS['lol-static-data']
        )
        return self._request(api_url)

    def get_shards(self,r=""):
        if r=="":
            api_url = URL['shards']
        else:
            api_url = URL['shards_by_region'].format(
                region=self.region,
            )

    def get_match(self,matchID):
        api_url = URL['match_by_id'].format(
            region=self.region,
            version = API_VERSIONS['match'],
            id = matchID
        )
        return self._request(api_url)

    def get_match_history(self,id,list=False):
        if list == True:
            api_url = URL['match_list_by_id'].format(
                region=self.region,
                version = API_VERSIONS['matchlist'],
                summonerID = id
            )
        else:
            api_url = URL['match_history_by_id'].format(
                region=self.region,
                version = API_VERSIONS['matchhistory'],
                summonerID = id
            )
        return self._request(api_url)

    def get_stats(self,id,ranked=False):
        if ranked == True:
            api_url = URL['stats_ranked_by_id'].format(
                region=self.region,
                version = API_VERSIONS['stats'],
                summonerId = id
            )
        else:
            api_url = URL['stats_summary_by_id'].format(
                region=self.region,
                version = API_VERSIONS['stats'],
                summonerId = id
            )
        return self._request(api_url)

    def get_summoner_by_name(self,name):
        api_url = URL['summoner_by_name'].format(
            region=self.region,
            version = API_VERSIONS['summoner'],
            names = name
        )
        return self._request(api_url)

    def get_summoner_by_id(self,id):
        api_url = URL['summoner_by_id'].format(
            region=self.region,
            version = API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_summoner_mastery(self,id):
        api_url = URL['summoner_mastery_by_id'].format(
            region=self.region,
            version = API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_summoner_name(self,id):
        api_url = URL['summoner_name_by_id'].format(
            region=self.region,
            version = API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_summoner_runes(self,id):
        api_url = URL['summoner_runes_by_id'].format(
            region=self.region,
            version = API_VERSIONS['summoner'],
            summonerId = id
        )
        return self._request(api_url)

    def get_team(self,id,summoner=False):
        if summoner==True:
            api_url = URL['team_by_summoner_id'].format(
                region=self.region,
                version = API_VERSIONS['team'],
                summonerId = id
            )
        else:
            api_url = URL['team_by_team_id'].format(
                region=self.region,
                version = API_VERSIONS['team'],
                summonerId = id
            )
        return self._request(api_url)
