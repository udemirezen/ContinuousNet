# Continuous-in-Depth Neural Networks

Introduction (todo).

This directory contains the implementation of ContinuousNet to accompany the preprint
> [Queiruga, Alejandro F., N. Benjamin Erichson, Dane Taylor and Michael W. Mahoney. “Continuous-in-Depth Neural Networks.” ArXiv abs/2008.02389 (2020)](https://arxiv.org/abs/2008.02389)

<img src="https://github.com/erichson/data/blob/master/img/ContinuousNet_overview.png" width="750">


## Get Started

Just clone the ContinuousNet repository to your local system and you are ready to go:
```
git clone https://github.com/afqueiruga/ContinuousNet
```

Also, you need a fork of `torchdiffeq` that is slightly modified in order to expose additional solver options: 
```
pip install git+https://github.com/afqueiruga/torchdiffeq
```

Note, this implementation best works with [PyTorch 1.6](https://pytorch.org/).

## Training

ContinuousNets can be trained similar to ResNets:
```
python3 cli.py [--dataset] [--batch-size] [--test-batch-size] [--epochs] [--lr] [--lr-decay] [--lr-decay-epoch] [--weight-decay] [--batch-norm] [--device] [--seed]

standard arguments:
--dataset                   you can train on CIFAR10, or CIFAR100 (default: CIFAR10)	
--batch-size                training batch size (default: 128)
--test-batch-size           testing batch size (default:256)
--epochs                    total number of training epochs (default: 180)
--lr                        initial learning rate (default: 0.1)
--lr-decay                  learning rate decay ratio (default: 0.1)
--lr-decay-epoch            epoch for the learning rate decaying (default: 80, 120)
--weight-decay              weight decay value (default: 5e-4)
--batch-norm                do we need batch norm in ResNet or not (default: True)
--device                    do we use gpu or not (default: 'gpu')
--seed                      used to reproduce the results (default: 0)
```




ContinuousNets provide some some extras (todo):
```
python3 cli.py [--model] [--scheme] [--n_time_steps_per] [--initial_time_d] [--time_epsilon] [--use_skipinit]

standard arguments:
--model
--scheme
--n_time_steps_per
--initial_time_d
--time_epsilon
--use_skipinit
```


After training the model checkpoint is saved in a folder called results.

## Examples and Performance on CIFAR-10

(todo)

```
python3 cli.py --model ContinuousNet --scheme euler --dataset CIFAR10 --lr 0.1 --wd 5e-4 --epochs 180 --lr_decay 0.1 --lr_update 80 120 160  --n_time_steps_per 1 --initial_time_d 8 --time_epsilon 8 --seed 0 --use_skipinit 0
```

| Model        | Activation            |  Depth  | Scheme      | #parms  | Test Accuracy |
| -------------|:---------------------:|:-------:|:----------: |:-------:|:-------------:|
| ResNet (v2)  | ReLU before addition  | 8-8-8   | -           | 0.85M   | 93.74%        |
| ContinuousNet| ReLU before addition  | 8-8-8   | Euler       |         | 92.45%        |
| ContinuousNet| full pre-activation   | 8-8-8   | Euler       | 0.85M   | 93.08%        |




## Examples and Performance on CIFAR-100

(todo)

| Model             | Activation            |  Depth  | Scheme      | #parms  | Test Accuracy |
| ------------------|:---------------------:|:-------:|:----------: |:-------:|:-------------:|
| Wide-ResNet       | ReLU before addition  | 8-8-8   | -           |   |         |
| Wide-ContinuousNet| ReLU before addition  | 8-8-8   | Euler       |         |               |
| Wide-ContinuousNet| full pre-activation   | 8-8-8   | Euler       |    |         |



## Evaluation

The training script outputs models to Python pickles. The script,
```
python3 eval_manifestation.py
```
performs a "convergence test" for given models by altering their integrator settings to illustrate the manifestation invariance property.

## License

This implementation is released under the GPL 3, as per LICENSE.

## Additional References

There is a video recording of an acompanying presentation available at [Queiruga, A. F., "Continuous-in-Depth Neural Networks," 1st Workshop on Scientific-Driven Deep Learning, July 1, 2020.](https://www.youtube.com/watch?v=_aX3T1Smg54)

