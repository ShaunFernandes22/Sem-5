# 10000
# 10000
# 10000
# 11111
# L shape  => 4 x 5 matrix

# 10001
# 11011
# 10101
# 10001
# M shape  => 4 x 5 matrix

import numpy as np
class Perceptron:
    def __init__(self, input_size):
        self.weights = np.random.rand(input_size)
        self.bias = np.random.rand(1)
    
    def activation(self, sum):
        return 1 if sum > 0 else 0
        
    def predict(self, input_arr):
        summation = np.dot(input_arr, self.weights) + self.bias
        return self.activation(summation)
        
    def train(self, X, y, learning_rate, epochs):
        for _ in range(epochs):
            for (input_arr, label) in zip(X, y):
                prediction = self.predict(input_arr)          
                err = label - prediction
                self.weights += learning_rate * err * input_arr
                self.bias += learning_rate * err
        
input_data = np.array([
    [1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,1,1,1,1],
    [1,0,0,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1]
    ])

labels = np.array([0,1])

perceptron = Perceptron(input_size=20)
perceptron.train(input_data, labels, learning_rate=0.1, epochs=100)

for x in input_data:
    pred = perceptron.predict(x)
    char = 'L' if pred == 0 else 'M'
    print(f"Input = {x} , Prediction = {pred}, Letter = {char}")
