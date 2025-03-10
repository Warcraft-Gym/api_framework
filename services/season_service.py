from services.base_service import BaseGNLBackendService
from model.season import Season

class SeasonService(BaseGNLBackendService):
    
    def get_season(self, season_id : int):
        return Season(self.get(f"seasons/{season_id}"))
    
    def update_season(self, season_id, season: Season):
        if not season or not season_id:
            raise Exception(f"Season or season id not defined: {season}")
        return Season(self.put(f"seasons/{season_id}", season.to_dict()))
    
    def create_season(self, season: Season):
        if not season:
            raise Exception(f"Season not defined: {season}")
        return Season(self.post("seasons", season.to_dict()))
    
    def delete_season(self, season_id):
        if not season_id:
            raise Exception(f"Season id not defined: {season_id}")
        self.delete(f"seasons/{season_id}")
        return True
    
    def get_all_seasons(self):
        seasons = self.get("seasons")
        l = []
        for season in seasons:     
            l.append(Season(season))
        return l
    
    def search_seasons(self, search_string):
        if not search_string:
            raise Exception(f"Search String not defined: {search_string}")
        seasons = self.search("seasons/search", search_string)
        l = []
        for season in seasons:     
            l.append(Season(season))
        return l
    
    def add_teams(self, season_id, team_ids: list):
        if not season_id:
            raise Exception(f"Season id not defined: {season_id}")
        if not team_ids:
            raise Exception(f"No team ids defined: {team_ids}")
        return Season(self.post(f"seasons/addTeams/{season_id}", team_ids))
    
    def remove_teams(self, season_id, team_ids: list):
        if not season_id:
            raise Exception(f"Season id not defined: {season_id}")
        if not team_ids:
            raise Exception(f"No team ids defined: {team_ids}")
        return Season(self.post(f"seasons/removeTeams/{season_id}", team_ids))