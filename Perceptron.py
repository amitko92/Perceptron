from Neural import Neural
import random as rand


class Perceptron:

    def __init__(self, dimension, threshold):
        self._weight = [rand.randint(1, 9) for i in range(dimension)]  # "starting_weights"
        self._threshold = threshold

    def val(self, point):
        sum_w = 0
        for x_i, w_i in zip(point, self._weight):
            sum_w += x_i * w_i
        if sum_w <= self._threshold:
            return 0
        else:
            return 1

    def calc_Z_i(self, point):
        # print(true_type)
        sum_w = 0
        for x_i, w_i in zip(point, self._weight):
            sum_w += x_i * w_i
        if sum_w >= self._threshold:
            result = 1
        else:
            result = 0
        return result, sum_w

    def train_valo(self, point, true_type):
        i = 0
        result, sum_w = self.calc_Z_i(point)

        if true_type != result:
            if sum_w > self._threshold:
                for i in range(len(self._weight)):
                    self._weight[i] = self._weight[i] - point[i]
            else:
                # print("The sum_w is: ", sum_w)
                for i in range(len(self._weight)):
                    self._weight[i] = self._weight[i] + point[i]
            return False
        else:
            return True
        i += 1


    def training(self, train_data, true_type):
        flag = False
        index = 0
        while not flag:
            flag = True
            index += 1
            j = 0
            for insetence in train_data:
                if not self.train_valo(insetence, true_type[j]):
                    flag = False
                j += 1



