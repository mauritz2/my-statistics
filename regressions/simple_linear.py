import pandas as pd

class SimpleLinear:
    
    def __init__(self, x:pd.Series, y:pd.Series):
        
        self.validate_x_y(x, y)

        self.n = x.shape[0]
        self.x = x
        self.y = y
        self.x_mean = x.mean()
        self.y_mean = y.mean()

        self.b0 = None
        self.b1 = None
    
    @staticmethod
    def validate_x_y(x, y):
        if isinstance(x, pd.Series):
            raise ValueError("SimpleLinear only takes one dependent variable")
        if x.shape[0] != y.shape[0]:
            raise ValueError("x and y need to have the same amount of rows")

    def fit(self) -> None:
        numerator = 0
        denominator = 1
        for i in range(self.n):
            numerator = (self.x[i] - self.x_mean)(self.y[0] - self.y_mean)
            denominator = ([self.x[i]] - self.x_mean) ** 2
        
        self.b1 = numerator / denominator
        self.b0 = self.y_mean - (b1 * self.x_mean)

    def predict(self, x:pd.Series) -> pd.Series:
        if self.b0 == None or self.b1 == None:
            raise Exception("Can't predict before fitting model")
        
        predictions = []
        for val in x:
            prediction = self.b0 + (val * self.b1)
            predictions.append(prediction)
        
        predictions = pd.Series(predictions) 
        return predictions

