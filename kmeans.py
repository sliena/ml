#1.calculate euclidean distances from each centroid to all datapoints
#2.assign datapoints to nearest centroids
#3.calculate for each centroid its center position among assigned datapoints
#4.move each centroid to its new center position
#5.repeat 1-4

import matplotlib.pyplot as plt

def euclidean_distance(datapoint, centroid):
    sum = float()
    for i in range(len(datapoint)):
        sum += (datapoint[i] - centroid[i]) ** 2
    return sum ** 0.5

def assign_centroid(datapoints, centroids):
    res = list()
    for dp in datapoints:
        #print('DATAPOINT: ', (dp[0], dp[1]))
        tmp = (10,0)
        for cent in centroids:
            #print('CENTROID: ', (cent[0], cent[1], cent[2]))
            dist = euclidean_distance(dp, cent)
            #print('EUCLI_DIST: ', (dist))
            if (dist < tmp[0]):
                #print('I AM SMALLER')
                tmp = (dist,cent[2])
                #print('ASSIGNED TMP: ', (tmp[0], tmp[1]))
        #print('BEFORE APPENDING: ', ())
        dp.append(tmp[1])
        res.append(dp)
    #print('BEFORE RETURN: ', (res[0]))
    return res


centroids = [[2.7810836,2.550537003,1],
	[1.465489372,2.362125076,2],
	[3.396561688,4.400293529,3],
	[1.38807019,1.850220317,4],
	[3.06407232,3.005305973,5]]

datapoints = [[2.6810836,2.650537003],
    [1.48807019,1.550220317],
    [1.48807019,4.550220317]]

res = assign_centroid(datapoints, centroids)

# for r in res:
#     print(r)

cent_col = {
  "1": "b",
  "2": "g",
  "3": "r",
  "4": "c",
  "5": "m",
}
#print(thisdict["brand"])

plt.plot([2.7810836], [2.550537003], f'{cent_col["1"]}o')
plt.plot([1.465489372], [2.362125076], f'{cent_col["2"]}o')
plt.plot([3.396561688], [4.400293529], f'{cent_col["3"]}o')
plt.plot([1.38807019], [1.850220317], f'{cent_col["4"]}o')
plt.plot([3.06407232], [3.005305973], f'{cent_col["5"]}o')

for r in res:
    plt.plot(r[0], r[1], f'{cent_col[f"{r[2]}"]}.')
    plt.plot(r[0], r[1])

plt.axis([0, 5, 0, 5])
plt.show()
