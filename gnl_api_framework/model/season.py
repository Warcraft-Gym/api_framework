class Season:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.name = data.get('name')
        self.number_weeks = data.get('number_weeks')
        self.pick_ban = data.get('pick_ban')
        self.maps = data.get('maps')

    def to_dict(self):
        return {
            'name': self.name,
            'number_weeks': self.number_weeks,
            'pick_ban': self.pick_ban
        }
    
    def __str__(self):
        maps_str = None
        if self.maps:
            maps_str = ", ".join(
                f"{map}" for map in self.maps
            )
        return (
            f"Season(id={self.id}, "
            f"name={self.name}, "
            f"number_weeks={self.number_weeks}, "
            f"pick_ban={self.pick_ban}, " 
            f"maps={maps_str})"
        )