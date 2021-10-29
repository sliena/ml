from math import sqrt
import matplotlib.pyplot as plt

def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)

def get_neighbors(train, test_row, num_neighbors):
	distances = list()
	for train_row in train:
		dist = euclidean_distance(train_row, test_row)
		distances.append((train_row, dist))
	distances.sort(key=lambda tup: tup[1])
	neighbors = list()
	for i in range(num_neighbors):
		neighbors.append(distances[i][0])
	return neighbors

def predict_classification(train, test_row, num_neighbors):
	neighbors = get_neighbors(train, test_row, num_neighbors)
	neighbor_classes = [row[-1] for row in neighbors]
	prediction = max(set(neighbor_classes), key=neighbor_classes.count)
	return prediction

dataset = [[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]]

prediction = predict_classification(dataset, dataset[0], 3)

#print('Predicted: %d Actual: %d' % (prediction, dataset[0][-1]))

plt.plot([2.7810836,1.465489372,3.396561688,1.38807019,3.06407232], [2.550537003,2.362125076,4.400293529,1.850220317,3.005305973], 'b.')
plt.axis([0, 10, 0, 10])
plt.show()