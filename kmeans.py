#1.calculate euclidean distances from each centroid to all datapoints
#2.assign datapoints its nearest centroid
#3.calculate for each centroid its center position among assigned datapoints
#4.move each centroid to its new center position
#5.repeat 1-4 until nothing changes after 1 iteration

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

def update_centroids(datapoints, centroids):
    new_cents = list()
    for c in centroids:
        sumX = 0
        sumY = 0
        cnt = 0
        for dp in datapoints:
            #print('DP class: %d CENTROID class: %d' % (dp[2], c[2]))
            if (dp[2] == c[2]):
                #print('IM IN FIRST IF')
                sumX += dp[0]
                sumY += dp[1]
                cnt += 1
        if (cnt > 0):
            #print('IM IN SECOND IF')
            newX = sumX / cnt
            newY = sumY / cnt
            new_cents.append([newX, newY, c[2]])
        else:
            new_cents.append(c)
    return new_cents



centroids_init = [[2.7810836,2.550537003,1],
	[1.465489372,2.362125076,2],
	[3.396561688,4.400293529,3],
	[1.38807019,1.850220317,4],
	[3.06407232,3.005305973,5]]

datapoints = [[3.02494593464871464, 3.36048495624975974],
[2.0163211699988564, 1.4698537144501256],
[1.78071813426441, 2.068853445457007],
[3.029593796670162043, 1.9992747098798942],
[4.3897359190529581, 4.545941882302538],
[2.612878323133237, 1.8390421591925783],
[4.555115697992543, 4.134906308630807],
[2.9895602798236824, 3.2162634169444932],
[4.718696911531623, 1.6740919925674902],
[4.41430499403088, 3.204726684091125],
[2.8327339953334384, 3.1717677675694382],
[4.906932101399594, 3.722640968164732],
[1.639896807053927, 2.6959689197732786],
[3.6139272327822387, 4.478393615267237],
[1.3700244534400188, 1.5663715819839632],
[1.0606531900240008, 4.12836799232493423],
[2.833286839710485, 3.292745731283498],
[1.0555707095074007, 2.5022250437227477],
[3.2630202214004806, 1.4110014368848722],
[3.2069388575396642, 3.6457714528467715]]

colors = {
  "1": "b",
  "2": "g",
  "3": "r",
  "4": "c",
  "5": "m",
}

datapoints_2 = assign_centroid(datapoints, centroids_init)

cents_2 = update_centroids(datapoints_2, centroids_init)

for c in cents_2:
    print(c)

plot1 = plt.figure(1)
for c in centroids_init:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')

for r in datapoints_2:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')

plt.axis([0, 5, 0, 5])

plot2 = plt.figure(2)
for c in cents_2:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')

for r in datapoints_2:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')

plt.axis([0, 5, 0, 5])
plt.show()


