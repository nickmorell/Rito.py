URL = {
    'base': 'https://{proxy}.api.pvp.net/api/lol/{region}/{url}',
    'champion': '/v{version}/champion',
    'champion_by_id': '/v{version}/champion/{id}',

    'summoner_by_name': 'v{version}/summoner/by-name/{names}',

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
