# region imports
from AlgorithmImports import *

from clr import AddReference
AddReference("System")
AddReference("Quantconnect.Algorithm")
AddReference("Quantconnect.Common")

from System import *
from QuantConnect import *
from QuantConnect.Algorithm import *

from universe import BigTechUniverseSelectionModel
from alpha import GaussianNaiveBayesAlphaModel


class GaussianNaiveBayesClassificationAlgorithm(QCAlgorithm):
    
    def Initialize(self):
        self.SetStartDate(2010, 1, 1)
        self.SetEndDate(2024,1, 1)
        self.SetCash(1000)

        self.SetUniverseSelection(BigTechUniverseSelectionModel())
        self.UniverseSettings.Resolution = Resolution.Daily

        self.SetAlpha(GaussianNaiveBayesAlphaModel())

        self.SetPortfolioConstruction(InsightWeightingPortfolioConstructionModel())

        self.SetExecution(ImmediateExecutionModel())
        
        self.SetBrokerageModel(AlphaStreamsBrokerageModel())