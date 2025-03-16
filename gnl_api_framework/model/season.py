class Season:
    def __init__(self, data: dict):
        self.id = data.get('id')
        self.name = data.get('name')
        self.number_weeks = data.get('number_weeks')

    def to_dict(self):
        return {
            'name': self.name,
            'number_weeks': self.number_weeks
        }
    
    def __str__(self):
        return (
            f"Season(id={self.id}, "
            f"name={self.name}, "
            f"number_weeks={self.number_weeks})"
        )