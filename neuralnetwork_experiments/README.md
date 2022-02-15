This folder contains the code that we used for conducting our experiments on neural networks. We used the code provided in U. Simsekli, L. Sagun, M. Gurbuzbalaban, "A Tail-Index Analysis of Stochastic Gradient Noise in Deep Neural Networks", ICML 2019. We are submitting our version for the convenience of the readers.

For the experiments on the VGG networks, we used the code from https://github.com/chengyangfu/pytorch-vgg-cifar10 


The file "run.py" launches all the experiments required for reproducing our results. It mainly trains the neural networks with different step-sizes, batch-sizes, and with different datasets, and finally saves the last 1000 SGD iterates to the disk. 

Once run.py is finished, the file "postprocess_networks.ipynb" loads all the saved networks and computes the tail indices for each setting, then provides a simple visualization. 


