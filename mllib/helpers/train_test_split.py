import math

def train_test_split(X, y, test_size = 0.2):
    if len(X) != len(y):
        raise RuntimeError # TODO change errors
    X_train = []
    y_train = []
    X_test = []
    y_test = []

    for i in range(math.floor(len(X) * test_size)):
        # training
        X_train.append(X[i])
        y_train.append(y[i])
    for i in range(math.floor(len(X) * test_size), len(X)):
        # testing
        X_test.append(X[i])
        y_test.append(X[i])

    return X_train, y_train, X_test, y_test

if __name__ == "__main__":
    import unittest
    # testing
    class TestTTS(unittest.TestCase):
        def test_1d(self):
            X = [1,2,3,4,5]
            y = [1,2,3,4,5]
            X_train, y_train, X_test, y_test = train_test_split(X, y)
            self.assertEqual(len(X_train) + len(X_test), len(X), "The resulting feature array should be the same size")
            self.assertEqual(len(y_train) + len(y_test), len(y), "The resulting target array should be the same size")
        # TODO add more tests
    unittest.main()