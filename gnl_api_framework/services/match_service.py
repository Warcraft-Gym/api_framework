from gnl_api_framework.services.base_service import BaseGNLBackendService
from gnl_api_framework.model.match import Match

class MatchService(BaseGNLBackendService):
    
    def get_match(self, match_id : int):
        return Match(self.get(f"matches/{match_id}"))
    
    def update_match(self, match_id, match: Match):
        if not match or not match_id:
            raise Exception(f"Match or match id not defined: {match}")
        return Match(self.put(f"matches/{match_id}", match.to_dict()))
    
    def create_match(self, match: Match):
        if not match:
            raise Exception(f"Match not defined: {match}")
        return Match(self.post("matches", match.to_dict()))
    
    def delete_match(self, match_id):
        if not match_id:
            raise Exception(f"Match id not defined: {match_id}")
        self.delete(f"matches/{match_id}")
        return True
    
    def search_matches(self, search_string):
        if not search_string:
            raise Exception(f"Search String not defined: {search_string}")
        matches = self.search("matches/search", search_string)
        l = []
        for match in matches:     
            l.append(Match(match))
        return l