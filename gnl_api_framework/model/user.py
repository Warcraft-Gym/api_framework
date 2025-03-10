class User:
    def __init__(self, data : dict):
        self.id = data.get('id')
        self.name = data.get('name')
        self.battleTag = data.get('battleTag')
        self.discordTag = data.get('discordTag')
        self.race = data.get('race')
        self.mmr = data.get('mmr')
        self.country = data.get('country')

    def to_dict(self):
        return {
            'name': self.name,
            'battleTag': self.battleTag,
            'discordTag': self.discordTag,
            'race': self.race,
            'mmr': self.mmr,
            'country': self.country
        }