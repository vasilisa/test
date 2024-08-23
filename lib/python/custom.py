from sklearn.isotonic import IsotonicRegression

class IsotonicWrapper(IsotonicRegression): 
    def fit(self,X,y,sample_weight = None):
        super().fit(X.ravel,y,sample_weight=sample_weight)
        
    def predict(self,T):
        return super().predict(T.ravel())

