# fj's sensors output a range(ex. [7, 13]) means that there is approximately 7-13 cows of traffic inclusive
# highway runs for N miles, and traffic only goes in 1 direction
# for each 1 mile segment there is 1 sensor, and total of N sensors
# each 1 mile segment had at max 1 ramp, either on/off, on meaning that the traffic is going on the highway, and off meaning that the traffic is going off the highway
# if there is no ramp, then he places a sensor on the main highway
# if there is a ramp, then he places a sensor on the ramp
# he has N sensors(1-> 100 max inclusive)
# determine the most speicfic possible ranges that describe the rate of trffix flow 


# test case 1: starting with none
# Input:
# 3
# none 5 10
# on 1 1
# off 2 3
# expected:
# 5 10, no other info
# 3 9

# test case 2: starting with on ramp
# 4
# on 1 1
# none 10 14
# none 11 15
# off 2 3
# 

#import sys
#sys.stdin = open("traffic.in", "r") #redirecting input/output
#sys.stdout = open("traffic.out", "w")

N = int(input()) # number of sensors, and miles
highway = [0] * N
sensors = []
for i in range(N):
    sensor = input().split()
    sensors.append(sensor)

print(sensors)
current_range = [0,0]
previous_range = [0,0]
used_sensor = ''
for i in range(N):
    if sensors[i][0] == 'none':
        current_range[0] = int(sensors[i][1])
        current_range[1] = int(sensors[i][2])
        if used_sensor == 'none':
            current_range = [max(previous_range[0], current_range[0]), min(previous_range[1], current_range[1])]
        used_sensor = 'none'
    elif sensors[i][0] == 'on':
        current_range[0] += int(sensors[i][1]) # i made the msitake of adding [2] instead of [1], look through logic...
        current_range[1] += int(sensors[i][2])
    elif sensors[i][0] == 'off':
        current_range[0] -= int(sensors[i][2])
        current_range[1] -= int(sensors[i][1])
    previous_range = current_range.copy()




# we need to now find the traffic flow rate before mile 1(we found out the after mile 1)

beforeN = [-1,999999999]
for sensor in sensors[::-1]:
	if sensor[0] == 'on':
		beforeN[0]-=int(sensor[2])
		beforeN[1]-=int(sensor[1])
		if beforeN[0]<0:
			beforeN[0]=0
	elif sensor[0] == 'off':
		beforeN[0]+=int(sensor[1])
		beforeN[1]+=int(sensor[2])
	else:
		beforeN[0]=max(int(sensor[1]),beforeN[0])
		beforeN[1]=min(int(sensor[2]),beforeN[1])

print(*beforeN)
print(*current_range) # print after traffic flow