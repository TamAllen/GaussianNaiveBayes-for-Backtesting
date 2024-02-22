# GaussianNaiveBayes-for-Backtesting
This is just a practice project 

Method

Universe Selection

Following Lu (2016), we use a proprietary universe selection methodology to identify the largest stocks in the technology sector. We limit our universe to a size of 10, but this may be readily changed using the fine_size parameter in the constructor.

Alpha Construction

The GaussianNaiveBayesAlphaModel predicts which direction each security will take from one day's open to the next. When we built this Alpha model, we created a dictionary with a SymbolData object for each symbol in the universe and a flag to indicate that the universe had changed.

Alpha Securities Management

When a new security is added to the universe, we build a SymbolData object to contain information specific to that security. The Alpha model's OnSecuritiesChanged function manages the SymbolData objects. In this technique, because we train the Gaussian Naive Bayes classifier using the historical returns of the securities in the universe, we specify that the model be trained every time the universe changes.

SymbolData Class

The SymbolData class stores training data for the GaussianNaiveBayesAlphaModel and manages a consolidator subscription. In the constructor, we define the training parameters, initialize the consolidator, and warm up the training data.

The update_features method is used to update our training features with the most recent data provided to the algorithm. It returns True/False, indicating whether the features are in place to begin updating the training labels.

Model Training

The GNB model is trained every day as the cosmos changes. By default, it trains with 100 examples. The characteristics are the historical open-to-close returns of the universe constituents. The labels represent the returns from the open at T+1 to the open at T+2 for each time step for each security.

Alpha Update.

As new TradeBars are added to the Alpha model's Update function, we gather the open-to-close return of the most recent TradeBar for each securities in the universe. We then use the GNB model for each security to anticipate its direction and return Insight objects accordingly.






