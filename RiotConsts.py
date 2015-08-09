URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{url}',
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
