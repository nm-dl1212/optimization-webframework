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
            sampler = qmc.LatinHypercube(d=1)
            submit_designs = sampler.random(
                n=self.optimization_case.max_attempt_number)

        elif self.optimization_case.initial_sampling_method == "random":
            # random sampling
            submit_designs = [random.uniform(0, 1) for _ in range(
                self.optimization_case.max_attempt_number)]

        return submit_designs
