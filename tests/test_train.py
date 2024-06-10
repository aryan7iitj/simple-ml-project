import unittest
from sklearn.linear_model import LinearRegression
import pickle

class TestTrain(unittest.TestCase):
    def test_model_type(self):
        with open('model/linear_regression_model.pkl', 'rb') as f:
            model = pickle.load(f)
        self.assertIsInstance(model, LinearRegression)

if __name__ == '__main__':
    unittest.main()