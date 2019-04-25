import subprocess
import os

# step 1
cmd_1 = 'mpc-info -i /data1 -c 4 | grep Suggested\ Potree-OctTree\ CAABB'
p = subprocess.Popen(cmd_1, stdout=subprocess.PIPE, shell=True)

line = p.stdout.read()

lineList = line.split(',')

caabb = []

for i in range(7):
    if i != 0:
        caabb.append(lineList[i].strip())

caabb[-1] = caabb[-1][:-1]   # remove ')'

# step 2
tileNumber = 4
processNumber = 4

cmd_2 = "mpc-tiling -i /data1/ -o /data2/ -t /data3/ -e \"" + caabb[0] + " " + caabb[1] + " " +  caabb[3] + " " + caabb[4] + "\"" + " -n " + str(tileNumber) + " -p " + str(processNumber)
 
os.system(cmd_2)

# step 3
cmd_3 = "mpc-create-config-pycoeman -i /data2 -o /data1/ParallelPotreeConverter.xml -f LAZ -l 9 -s 83 -e \""

for i in range(len(caabb)):
    cmd_3 += caabb[i] 
    if i != 5:
        cmd_3 += " "
cmd_3 += "\""

os.system(cmd_3)

# step 4
cmd_4 = 'coeman-par-local -d / -c /data1/ParallelPotreeConverter.xml -e /data1/execution -n 4'

os.system(cmd_4)