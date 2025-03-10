from gnl_api_framework.services.base_service import BaseGNLBackendService
from gnl_api_framework.model.team import Team

class TeamService(BaseGNLBackendService):
    
    def get_team(self, team_id : int):
        return Team(self.get(f"teams/{team_id}"))
    
    def update_team(self, team_id, team: Team):
        if not team or not team_id:
            raise Exception(f"Team or team id not defined: {team}")
        return Team(self.put(f"teams/{team_id}", team.to_dict()))
    
    def create_team(self, team: Team):
        if not team:
            raise Exception(f"Team not defined: {team}")
        return Team(self.post(f"teams", team.to_dict()))
    
    def delete_team(self, team_id):
        if not team_id:
            raise Exception(f"Team id not defined: {team_id}")
        self.delete(f"teams/{team_id}")
        return True
    
    def search_team(self, search_string):
        if not search_string:
            raise Exception(f"Search String not defined: {search_string}")
        teams = self.search("teams/search", search_string)
        l = []
        for team in teams:     
            l.append(Team(team))
        return l

    def get_all_teams(self):
        teams = self.get("teams")
        l = []
        for team in teams:     
            l.append(Team(team))
        return l
    
    def get_teams_for_season(self, season_id : int):
        teams = self.get(f"teams/season/{season_id}")
        l = []
        for team in teams:     
            l.append(Team(team))
        return l
    
    def get_team_for_season(self, season_id : int, team_id : int):
        return self.get(f"teams/{team_id}/season/{season_id}")

    def add_player(self, team_id, player_ids: list):
        if not team_id:
            raise Exception(f"Team id not defined: {team_id}")
        if not player_ids:
            raise Exception(f"No player ids defined: {player_ids}")
        return Team(self.post(f"teams/addPlayers/{team_id}", player_ids))
    
    def remove_player(self, team_id, player_ids: list):
        if not team_id:
            raise Exception(f"Team id not defined: {team_id}")
        if not player_ids:
            raise Exception(f"No player ids defined: {player_ids}")
        return Team(self.post(f"teams/removePlayers/{team_id}", player_ids))
