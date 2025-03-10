from gnl_api_framework.services.base_service import BaseGNLBackendService
from gnl_api_framework.model.series import Series

class SeriesService(BaseGNLBackendService):
    
    def get_series(self, series_id : int):
        return Series(self.get(f"series/{series_id}"))
    
    def update_series(self, series_id, series: Series):
        if not series or not series_id:
            raise Exception(f"Series or series id not defined: {series}")
        return Series(self.put(f"series/{series_id}", series.to_dict()))
    
    def create_series(self, series: Series):
        if not series:
            raise Exception(f"Series not defined: {series}")
        return Series(self.post("series", series.to_dict()))
    
    def delete_series(self, series_id):
        if not series_id:
            raise Exception(f"Series id not defined: {series_id}")
        self.delete(f"series/{series_id}")
        return True
    
    def get_all_series(self):
        series_l = self.get("series")
        l = []
        for series in series_l:     
            l.append(Series(series))
        return l

    def search_series(self, search_string):
        if not search_string:
            raise Exception(f"Search String not defined: {search_string}")
        series_l = self.search("series/search", search_string)
        l = []
        for series in series_l:     
            l.append(Series(series))
        return l