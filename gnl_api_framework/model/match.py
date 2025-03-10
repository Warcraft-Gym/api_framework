from gnl_api_framework.model.team import Team
from gnl_api_framework.model.season import Season

class Match:
    def __init__(self, data : dict):
        self.id = data.get('id')
        self.team1_id = data.get('team1_id')
        team1 = data.get('team1')
        if team1:
            team1 = Team(team1)
        self.team1 = team1
        self.team2_id = data.get('team2_id')
        team2 = data.get('team2')
        if team2:
            team2 = Team(team2)
        self.team2 = team2
        self.season_id = data.get('season_id')
        season = data.get('season')
        if season:
            season = Season(season)
        self.season = season
        self.playday = data.get('playday')
        self.score = data.get('score')

    def to_dict(self):
        return {
            'team1_id': self.team1_id,
            'team2_id': self.team2_id,
            'season_id': self.season_id,
            'playday': self.playday,
            'score': self.score
        }