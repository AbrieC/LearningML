import numpy as npclass Perceptron(object):def __init__(self, learn, itr):
        """
        :param learn: learning rate
        :type learn: float
        :param itr: number of iterations
        :type itr: integer
        """
        self.learn = learn
        self.itr = itrdef train(self, x, y):
        """
        Train the weights with data set x for outputs y
        :param x: training data features
        :type x: array (matrix) of n-samples, n-features
        :param y: training data outputs
        :type y: array of n-samples
        :return: weights (w) and errors for each iteration
        """
        self.w = np.zeros(1 + x.shape[1])
        self.error = []
        for _ in range(self.itr):
            errors = 0
            for xi, target in zip(x, y):
                update = self.learn*(target - self.predict(xi))
                self.w[1:] += update*xi
                self.w[0] += update
                errors += int(update != 0)
            self.error.append(errors)
        return selfdef predict(self, x):
        """
        :param x: input vector of features
        :type x: ndarray
        :return: int 1 or -1
        """
