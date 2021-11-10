#1.calculate euclidean distances from each centroid to all datapoints
#2.assign datapoints its nearest centroid
#3.calculate for each centroid its center position among assigned datapoints
#4.move each centroid to its new center position
#5.repeat 1-4 until nothing changes after 1 iteration

import matplotlib.pyplot as plt
import copy
import csv

# Read CSV file and convert to a list
def csv_to_array(path):
    res = []
    with open (path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
        for row in csv_reader:
            res.append(row)
    return res

# Calculate euclidean distance between single datapoint and centroid
def euclidean_distance(datapoint, centroid):
    sum = float()
    for i in range(len(datapoint) - 1):
        sum += (datapoint[i] - centroid[i]) ** 2
    return sum ** 0.5

# Assign each datapoint a centroid it belongs to
def assign_centroid(datapoints, centroids):
    res = copy.deepcopy(datapoints)
    for dp in res:
        tmp = (euclidean_distance(dp, centroids[0]),0)
        for c in centroids:
            dist = euclidean_distance(dp, c)
            if (dist < tmp[0]):
                tmp = (dist,c[2])
        dp[2] = tmp[1]
    return res

# Center single centroid among its belonging datapoints
def center_single_centroid(datapoints, centroids):
    res = list()
    changed = False
    for c in centroids:
        sumX = 0
        sumY = 0
        cnt = 0
        for dp in datapoints:
            if (dp[2] == c[2]):
                sumX += dp[0]
                sumY += dp[1]
                cnt += 1
        if (cnt > 0):
            newX = sumX / cnt
            newY = sumY / cnt
            res.append([newX, newY, c[2]])
            if (c[0] != newX or c[1] != newY):
                changed = True
        else:
            res.append(c)
    return res, changed

# Center all centroids among their belonging datapoints
def center_all_centroids(datapoints, centroids):
    changed = True
    tmp_dp = datapoints
    tmp_cents = centroids
    while (changed):
        tmp_dp = assign_centroid(tmp_dp, tmp_cents)
        tmp = center_single_centroid(tmp_dp, tmp_cents)
        tmp_cents = tmp[0]
        changed = tmp[1]
    return tmp_dp, tmp_cents

# Determine optimal amount of centroids for set of datapoints and spread them evenly
def k_means(datapoints):
    clusters = list()
    first_cluster = [datapoints[0][0], datapoints[0][1], 0]
    clusters.append(first_cluster)
    clusters = center_all_centroids(datapoints, clusters)[1]
    wcss_1 = 0
    wcss_2 = wcss(datapoints, clusters)
    diff = wcss_2
    print('WCSS_1: %f WCSS_2 %f DIFF: %f' % (wcss_1, wcss_2, diff))
    #while (diff > 5):
    for i in range(5):  
        max_dist = 0
        max_dp = [0, 0, 0]
        for dp in datapoints:
            dist = 0
            for c in clusters:
                dist += euclidean_distance(dp, c) ** 2
                if (dist > max_dist):
                    max_dist = dist
                    max_dp = [dp[0], dp[1], len(clusters)]
        clusters.append(max_dp)
        tmp_datapoints, clusters = center_all_centroids(datapoints, clusters)
        wcss_1 = wcss_2
        wcss_2 = wcss(tmp_datapoints, clusters)
        diff = wcss_1 - wcss_2
        print('WCSS_1: %d WCSS_2 %d DIFF: %d' % (wcss_1, wcss_2, diff))
    return center_all_centroids(datapoints, clusters)    

# 
def wcss(datapoints, centroids):
    sum = 0
    for c in centroids:
        for dp in datapoints:       
            if (dp[2] == c[2]):
                sum += euclidean_distance(dp, c) ** 2
    return sum / len(centroids)


dt_test = [[1,1,0],[1,2.5,0],[1,4,0],[4,1,0],[4,2.5,0],[4,4,0]]

colors = {
  "0": "k",
  "1": "b",
  "2": "g",
  "3": "r",
  "4": "c",
  "5": "m",
  "6": "y"
}

datapoints = csv_to_array('test.csv')
my_iris = k_means(datapoints)

#datapoints2 = csv_to_array('iris_plot.csv')
#real_iris = k_means(datapoints2)
#print(datapoints2[0])

# f = open('new_iris.csv', 'w')
# writer = csv.writer(f)
# writer.writerow(final)
# f.close()

plot1 = plt.figure(1)
for c in my_iris[1]:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in my_iris[0]:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 10, 0, 10])

# plot2 = plt.figure(2)
# #for c in datapoints2[1]:
# #    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
# for r in datapoints2:
#     plt.plot(r[0], r[1], f'{colors[f"{int(r[2])}"]}.')
# plt.axis([0, 10, 0, 10])

plt.show()