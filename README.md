# G-Research-Crypto-Forecasting Kaggle Competition

Introduction:

Over $40 billion worth of cryptocurrencies are traded every day. They are among the most popular assets for speculation and investment, yet have proven wildly volatile. Fast-fluctuating prices have made millionaires of a lucky few, and delivered crushing losses to others. Could some of these price movements have been predicted in advance?

In this competition, you'll use your machine learning expertise to forecast short term returns in 14 popular cryptocurrencies. We have amassed a dataset of millions of rows of high-frequency market data dating back to 2018 which you can use to build your model. Once the submission deadline has passed, your final score will be calculated over the following 3 months using live crypto data as it is collected.

The simultaneous activity of thousands of traders ensures that most signals will be transitory, persistent alpha will be exceptionally difficult to find, and the danger of overfitting will be considerable. In addition, since 2018, interest in the cryptomarket has exploded, so the volatility and correlation structure in our data are likely to be highly non-stationary. The successful contestant will pay careful attention to these considerations, and in the process gain valuable insight into the art and science of financial forecasting.

G-Research is Europe’s leading quantitative finance research firm. We have long explored the extent of market prediction possibilities, making use of machine learning, big data, and some of the most advanced technology available. Specializing in data science and AI education for workforces, Cambridge Spark is partnering with G-Research for this competition. Watch our introduction to the competition below:
https://www.youtube.com/watch?v=GW84uCnYr30



Data:

The dataset contains information on historic trades for several cryptoassets, such as Bitcoin and Ethereum. Your challenge is to predict their future returns.

As historic cryptocurrency prices are not confidential this will be a forecasting competition using the time series API. Furthermore the public leaderboard targets are publicly available and are provided as part of the competition dataset. Expect to see many people submitting perfect submissions for fun. Accordingly, THE PUBLIC LEADERBOARD FOR THIS COMPETITION IS NOT MEANINGFUL and is only provided as a convenience for anyone who wants to test their code. The final private leaderboard will be determined using real market data gathered after the submission period closes.

train.csv - The training set
  timestamp - A timestamp for the minute covered by the row.
  Asset_ID - An ID code for the cryptoasset.
  Count - The number of trades that took place this minute.
  Open - The USD price at the beginning of the minute.
  High - The highest USD price during the minute.
  Low - The lowest USD price during the minute.
  Close - The USD price at the end of the minute.
  Volume - The number of cryptoasset units traded during the minute.
  VWAP - The volume weighted average price for the minute.
  Target - 15 minute residualized returns. See the 'Prediction and Evaluation' section of this notebook for details of how the target is calculated.
  
example_test.csv - An example of the data that will be delivered by the time series API.

example_sample_submission.csv - An example of the data that will be delivered by the time series API. The data is just copied from train.csv.

asset_details.csv - Provides the real name and of the cryptoasset for each Asset_ID and the weight each cryptoasset receives in the metric.

gresearch_crypto - An unoptimized version of the time series API files for offline work. You may need Python 3.7 and a Linux environment to run it without errors.

supplemental_train.csv - After the submission period is over this file's data will be replaced with cryptoasset prices from the submission period. In the Evaluation phase, the train, train supplement, and test set will be contiguous in time, apart from any missing data. The current copy, which is just filled approximately the right amount of data from train.csv is provided as a placeholder.



Time-series API Details:

Refer to the time series introduction notebook for an example of how to complete a submission. The time-series API has changed somewhat from previous competitions!

Expect to see roughly three months worth of data in the test set. Until the forecasting phase of the competition, the API will just deliver a slice of the training data.

The API will require 0.5 GB of memory after initialization. The initialization step (env.iter_test()) will require meaningfully more memory than that; we recommend you do not load your model until after making that call. The API will also consume less than 30 minutes of runtime for loading and serving the data.

The API loads the data using the following types: Asset_ID: int8, Count: int32, row_id: int32, Count: int32, Open: float64, High: float64, Low: float64, Close: float64, Volume: float64, VWAP: float64
