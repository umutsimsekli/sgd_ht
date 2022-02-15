import os
import subprocess
import itertools
import time
# folder to save
base_path = 'results_FC'

if not os.path.exists(base_path):
    os.makedirs(base_path)

launcher = ''

# experimental setup
width   = [128]
depth   = [3]
dataset = ['mnist', 'cifar10']
loss    = ['NLL']
model   = ['fc']

eta     = [0.015, 0.02, 0.025, 0.03, 0.04, 0.045, 0.06, 0.070, 0.075, 0.08, 0.09, 0.0001, 0.001, 0.01, 0.05, 0.1]
bs      = [1, 5, 10]

# These are the different seeds used for different initializations
seed = 0
# seed = 42
# seed = 21


iterations = 10000
iter_save_net = 1000

grid = itertools.product(width, depth, dataset, loss, model, eta, bs)
# print(list(grid))

processes = []
for w, dep, d, l, m, lr, bb in grid:

    save_dir = base_path + '/{}_{:04d}_{}_{}_{}_{:E}_{:04d}'.format(dep, w, d, l, m, lr, bb)
    if os.path.exists(save_dir):
        # folder created only at the end when all is done!
        print('folder already exists, quitting')
        continue

    os.makedirs(save_dir)

    cmd = launcher + ' '
    cmd += 'python main.py '
    cmd += '--save_dir {} '.format(save_dir)
    cmd += '--width {} '.format(w)
    cmd += '--depth {} '.format(dep)
    cmd += '--dataset {} '.format(d)
    cmd += '--model {} '.format(m)
    cmd += '--lr {} '.format(lr)
    cmd += '--batch_size_train {} '.format(bb)
    cmd += '--batch_size_eval {} '.format(bb)
    cmd += '--iterations {} '.format(iterations)
    cmd += '--iter_save_net {} '.format(iter_save_net)
    cmd += '--seed {} '.format(seed)

    # print(cmd)

    f = open(save_dir + '.log', 'w')
    subprocess.Popen(cmd.split(), stdout=f, stderr=f)#.wait()
    #time.sleep(0.1)
    # f.close()






