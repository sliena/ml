#1.calculate euclidean distances from each centroid to all datapoints
#2.assign datapoints its nearest centroid
#3.calculate for each centroid its center position among assigned datapoints
#4.move each centroid to its new center position
#5.repeat 1-4 until nothing changes after 1 iteration

import matplotlib.pyplot as plt
import copy

def euclidean_distance(datapoint, centroid):
    sum = float()
    for i in range(len(datapoint) - 1):
        sum += (datapoint[i] - centroid[i]) ** 2
    return sum ** 0.5

def assign_centroid(datapoints, centroids):
    res = copy.deepcopy(datapoints)
    for dp in res:
        tmp = (10,0)
        for c in centroids:
            dist = euclidean_distance(dp, c)
            if (dist < tmp[0]):
                tmp = (dist,c[2])
        dp[2] = tmp[1]
    return res

def update_centroids(datapoints, centroids):
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

def rename_me(datapoints, centroids):
    changed = True
    tmp_dp = datapoints
    tmp_cents = centroids
    print(tmp_cents)
    while (changed):
        tmp_dp = assign_centroid(tmp_dp, tmp_cents)
        tmp = update_centroids(tmp_dp, tmp_cents)
        tmp_cents = tmp[0]
        changed = tmp[1]
    return tmp_dp, tmp_cents

centroids_1 = [[2.7810836,2.550537003,1],
	[1.465489372,2.362125076,2],
	[3.396561688,4.400293529,3],
	[1.38807019,1.850220317,4],
	[3.06407232,3.005305973,5]]

datapoints_1 = [[3.02494593464871464, 3.36048495624975974, 0],
[2.0163211699988564, 1.4698537144501256, 0],
[1.78071813426441, 2.068853445457007, 0],
[3.029593796670162043, 1.9992747098798942, 0],
[4.3897359190529581, 4.545941882302538, 0],
[2.612878323133237, 1.8390421591925783, 0],
[4.555115697992543, 4.134906308630807, 0],
[2.9895602798236824, 3.2162634169444932, 0],
[4.718696911531623, 1.6740919925674902, 0],
[4.41430499403088, 3.204726684091125, 0],
[2.8327339953334384, 3.1717677675694382, 0],
[4.906932101399594, 3.722640968164732, 0],
[1.639896807053927, 2.6959689197732786, 0],
[3.6139272327822387, 4.478393615267237, 0],
[1.3700244534400188, 1.5663715819839632, 0],
[1.0606531900240008, 4.12836799232493423, 0],
[2.833286839710485, 3.292745731283498, 0],
[1.0555707095074007, 2.5022250437227477, 0],
[3.2630202214004806, 1.4110014368848722, 0],
[3.2069388575396642, 3.6457714528467715, 0],
[3.906137, 3.361724, 0],
[4.115977, 3.382294, 0],
[4.508293, 1.871085, 0],
[4.940708, 2.877789, 0],
[1.814244, 3.426315, 0],
[4.760862, 3.052155, 0],
[3.042034, 2.128135, 0],
[2.315427, 3.402209, 0],
[1.932761, 0.883623, 0],
[3.191374, 0.642309, 0],
[0.686096, 2.874091, 0],
[4.799137, 1.640946, 0],
[2.769040, 3.132980, 0],
[1.329190, 3.980595, 0],
[2.774409, 1.811267, 0],
[2.862281, 3.220915, 0],
[2.827836, 1.914425, 0],
[1.386679, 1.378423, 0],
[1.476733, 4.550113, 0],
[4.291687, 1.058274, 0]]

colors = {
  "0": "k",
  "1": "b",
  "2": "g",
  "3": "r",
  "4": "c",
  "5": "m"
}

final = rename_me(datapoints_1, centroids_1)

# plot1 = plt.figure(1)
# for c in centroids_1:
#     plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
# for r in datapoints_1:
#     plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
# plt.axis([0, 5, 0, 5])




#print(centroids_1)
datapoints_2 = assign_centroid(datapoints_1, centroids_1)
centroids_2 = update_centroids(datapoints_2, centroids_1)[0]
#print(centroids_2)
datapoints_3 = assign_centroid(datapoints_2, centroids_2)
centroids_3 = update_centroids(datapoints_3, centroids_2)[0]
#print(centroids_3)
#datapoints_3 = assign_centroid()

plot1 = plt.figure(1)
for c in centroids_1:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in datapoints_1:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 5, 0, 5])

plot2 = plt.figure(2)
for c in centroids_1:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in datapoints_2:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 5, 0, 5])

plot3 = plt.figure(3)
for c in centroids_2:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in datapoints_2:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 5, 0, 5])

plot4 = plt.figure(4)
for c in centroids_2:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in datapoints_3:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 5, 0, 5])

plot5 = plt.figure(5)
for c in centroids_3:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in datapoints_3:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 5, 0, 5])

plot6 = plt.figure(6)
for c in final[1]:
    plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')
for r in final[0]:
    plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')
plt.axis([0, 5, 0, 5])

plt.show()

# plot2 = plt.figure(2)
# for c in val1[1]:
#     plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')

# for r in val1[0]:
#     plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')

# plt.axis([0, 5, 0, 5])

# plot3 = plt.figure(3)
# for c in val2[1]:
#     plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')

# for r in val2[0]:
#     plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')

# plt.axis([0, 5, 0, 5])



# for c in cents_2:
#     print(c)

# plot1 = plt.figure(1)
# for c in centroids_init:
#     plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')

# for r in datapoints_2:
#     plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')

# plt.axis([0, 5, 0, 5])

# plot2 = plt.figure(2)
# for c in cents_2:
#     plt.plot(c[0], c[1], f'{colors[f"{c[2]}"]}o')

# for r in datapoints_2:
#     plt.plot(r[0], r[1], f'{colors[f"{r[2]}"]}.')

# plt.axis([0, 5, 0, 5])
# plt.show()


