alpha = 0.125
beta = 0.25

estRtt = 390
devRtt = 37

sampleRtt = [390, 330, 300]

for i in range (0, 3):
    devRtt = (1 - beta) * devRtt + beta * abs(estRtt - sampleRtt[i])
    estRtt = (1 - alpha) * estRtt + alpha * sampleRtt[i]
    tcp_tt = estRtt + 4*devRtt
    print(f"Est RTT {i+1}: {estRtt} msec")
    print(f"Dev RTT {i+1}: {devRtt} msec")
    print(f"TCP timeout {i+1}: {tcp_tt} msec")

