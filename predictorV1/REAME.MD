# Stock Direction Predictor

This is an experimental v1 tool that takes a number of engineered features from historical stock price data and uses a logistic regression model to predict whether a stock's closing price will go up or down the next trading day.

## Model
This project uses logistic regression, a model well suited to binary classification problems, since it outputs a probability that naturally maps to a yes/no (in this case, up/down) prediction.

## Tools
- `yfinance` — pulling historical stock price data
- `pandas` — data manipulation and feature engineering
- `scikit-learn` — logistic regression model, train/test splitting, evaluation metrics

## Results
Results were largely inconclusive — accuracy hovered close to a coin flip (50%) across multiple feature combinations and dataset sizes. However, the experiments showed that changing which features are included can noticeably influence which direction the model leans toward predicting, even without producing a genuinely reliable result. A more in-depth analysis — potentially including cross-validation, alternative models, or additional data sources — would be needed to develop a meaningfully more accurate model.