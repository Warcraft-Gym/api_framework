from datetime import datetime
from gnl_api_framework.model.user import User
from gnl_api_framework.model.match import Match

class Series:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.match_id = data.get('match_id')
        match = data.get('match')
        if match:
            match = Match(match)
        self.match = match
        dt = data.get('date_time')
        if dt and isinstance(dt, str):
            dt = datetime.fromisoformat(dt)
        self.date_time = dt
        self.caster = data.get('caster')
        self.player1_id = data.get('player1_id')
        player1 = data.get('player1')
        if player1:
            player1 = User(player1)
        self.player1 = player1
        self.player2_id = data.get('player2_id')
        player2 = data.get('player2')
        if player2:
            player2 = User(player2)
        self.player2 = player2
        self.player1_score = data.get('player1_score')
        self.player2_score = data.get('player2_score')
        self.host_player_id = data.get('host_player_id')

    def to_dict(self):
        return {
            'match_id': self.match_id,
            'date_time': self.date_time.isoformat() if isinstance(self.date_time, datetime) else self.date_time,
            'caster': self.caster,
            'player1_id': self.player1_id,
            'player2_id': self.player2_id,
            'player1_score': self.player1_score,
            'player2_score': self.player2_score,
            'host_player_id': self.host_player_id
        }

    def __str__(self):
        return (
            f"Series(id={self.id}, "
            f"match_id={self.match_id}, match={self.match}, "
            f"date_time={self.date_time}, caster={self.caster}, "
            f"player1_id={self.player1_id}, player1={self.player1}, "
            f"player2_id={self.player2_id}, player2={self.player2}, "
            f"player1_score={self.player1_score}, "
            f"player2_score={self.player2_score}, host_player_id={self.host_player_id})"
        )
