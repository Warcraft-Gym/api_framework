from gnl_api_framework.model.season import Season
class SeasonInfo:
    def __init__(self, data : dict):
        self.season_id = data.get('season_id')
        self.final_score = data.get('final_score')
        self.points_available = data.get('points_available')
        self.points_against = data.get('points_against')
        season = data.get('season')
        if season:
            season = Season(season)
        self.season = season