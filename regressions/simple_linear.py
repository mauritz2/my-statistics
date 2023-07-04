import pandas as pd

class SimpleLinear:
    
    def __init__(self):
        self.b0 = None
        self.b1 = None
    
    @staticmethod
    def validate_x_y(x, y):
        if x.shape[0] != y.shape[0]:
            raise ValueError("x and y need to have the same amount of rows")

    def fit(self, x: pd.Series, y:pd.Series) -> None:
        self.validate_x_y(x, y)

        n = x.shape[0]
        x = x
        y = y
        x_mean = x.mean()
        y_mean = y.mean()
        numerator = 0
        denominator = 0

        for i in range(n):
            numerator += (x[i] - x_mean) * (y[i] - y_mean)
            denominator += (x[i] - x_mean) ** 2
        
        self.b1 = numerator / denominator
        self.b0 = y_mean - self.b1 * x_mean

    def predict(self, x:pd.Series) -> pd.Series:
        if self.b0 == None or self.b1 == None:
            raise Exception("Can't predict before fitting model")
        
        predictions = []
        for val in x:
            prediction = self.b0 + (val * self.b1)
            predictions.append(prediction)
        
        predictions = pd.Series(predictions) 
        return predictions

