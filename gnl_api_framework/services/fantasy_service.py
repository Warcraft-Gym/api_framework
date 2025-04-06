import logging
from gnl_api_framework.services.base_service import BaseGNLBackendService
from gnl_api_framework.model.fantasy_team import FantasyTeam

logger = logging.getLogger(__name__)

class FantasyService(BaseGNLBackendService):
    
    def calculateSeason(self, season_id: int):
        logger.debug(f"Calculating fantasy scores for season id: {season_id}")
        result = self.post(f"fantasy/season/{season_id}/calculate", None)
        logger.debug(f"Received response: {result}")
        return True