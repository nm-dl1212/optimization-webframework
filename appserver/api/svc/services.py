# services.py
from scipy.stats import qmc
import random


class SamplingService:
    def __init__(self, optimization_case):
        self.optimization_case = optimization_case

    def generate_designs(self):
        submit_designs = []
        if self.optimization_case.initial_sampling_method == "latin":
            # latin hypercube sampling
            sampler = qmc.LatinHypercube(d=2)  # 2
            submit_designs = sampler.random(
                n=self.optimization_case.max_attempt_number)

        elif self.optimization_case.initial_sampling_method == "random":
            # random sampling
            pass

        return submit_designs
