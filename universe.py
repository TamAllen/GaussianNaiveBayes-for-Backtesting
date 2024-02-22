#region imports
from AlgorithmImports import *
from Selection.FundamentalUniverseSelectionModel import FundamentalUniverseSelectionModel
#from Selection import FundamentalUniverseSelectionModel

class BigTechUniverseSelectionModel(FundamentalUniverseSelectionModel):
    def __init__(self, fine_size=10):
        self.fine_size = fine_size
        self.month = -1
        super().__init__(True)
    
    def SelectCoarse(self, algorithm, coarse):
        if algorithm.Time.month == self.month:
            return Universe.Unchanged
        return [x.Symbol for x in coarse if x.HasFundamentalData]

    def SelectFine(self, algorithm, fine):
        self.month = algorithm.Time.month
        tech_stocks = [f for f in fine if f.AssetClassification.MorningstarSectorCode == MorningstarSectorCode.Technology ]
        sorted_by_market_cap = sorted(tech_stocks, key=lambda x: x.MarketCap, reverse=True)
        return [x.Symbol for x in sorted_by_market_cap[:self.fine_size]]