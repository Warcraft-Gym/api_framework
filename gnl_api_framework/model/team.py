from gnl_api_framework.model.user import User
from gnl_api_framework.model.season_info import SeasonInfo

class Team:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.name = data.get('name')
        players = data.get('player_by_season')
        pl = {}
        if players:
            for season_id, player in players.items():
                pl[season_id] = User(player)
        self.players_by_season = pl

        seasons_info = data.get('seasons_info')
        if seasons_info:
            seasons_info = [SeasonInfo(seasons_info) for seasons_info in seasons_info]
        self.seasons_info = seasons_info

    def to_dict(self):
        return {
            'name': self.name
        }

    def __str__(self):
        players_by_season_str = ", ".join(
            f"{season_id}: {player}" for season_id, player in self.players_by_season.items()
        )
        seasons_info_str = ", ".join(str(season_info) for season_info in self.seasons_info) if self.seasons_info else None
        return (
            f"Team(id={self.id}, name={self.name}, "
            f"players_by_season={{ {players_by_season_str} }}, "
            f"seasons_info=[{seasons_info_str}])"
        )
