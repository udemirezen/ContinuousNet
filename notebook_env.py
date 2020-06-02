from collections import defaultdict
import functools
from glob import glob
import json
import os
import re
from typing import List

from matplotlib import pylab as plt
import numpy as np
import pandas as pd
import torch
from SimDataDB import SimDataDB
try:
    import tqdm
    progress = tqdm.tqdm
except ModuleNotFoundError:
    progress = lambda x, *args : x

from odenet import refine_train
from odenet import ode_models
from odenet import datasets
from odenet import odenet_cifar10
from odenet import plotting
from odenet import helper

legend_name = lambda fname : re.search(r"ARCH(.*)", fname)[1]

class PostPack:
    """We should've saved Pack instead."""
    model: str
    alpha: int
    scheme: str
    use_skip_init: bool
    use_batch_norms: str
    initial_time_d: int
    n_steps_per: int
    refine: List[int]
    def __init__(self, fname):
        r = re.search(r"""(SingleSegment|Wide|Wide2)-ARCH-([0-9]*)-([A-Za-z]*)-([A-Za-z]*)-([a-z4_]*)-([0-9]*)-[14].0-([0-9]*)-.*-160-(None|\[.*\])""",fname)
        self.model = r.group(1)
        self.alpha = r.group(2)
        self.use_batch_norms = r.group(3)
        self.use_skip_init = (r.group(4)!="NoSkip")
        self.scheme = r.group(5)
        self.initial_time_d = int(r.group(6))
        self.n_steps_per = int(r.group(7))
        if r.group(8) == "None":
            self.refine = []
        else:
            self.refine = json.loads(r.group(8))
        self.final_time_d = self.initial_time_d * 2**len(self.refine)

def set_ode_config(model, n_steps, scheme, use_adjoint=False):
    for net_idx in range(len(model.net)):
        try:
            model.net[net_idx].set_n_time_steps(n_steps)
            model.net[net_idx].scheme = scheme
        except AttributeError:
            pass