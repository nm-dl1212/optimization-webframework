# services.py
from scipy.stats import qmc
import numpy as np


class SamplingService:
    def __init__(self, optimization_case):
        self.optimization_case = optimization_case

    def generate_designs(self):
        designs_dimension = self.optimization_case.designs_dimension
        sampling_method = self.optimization_case.sampling_method
        max_trial_number = self.optimization_case.max_trial_number

        submit_designs = []
        if sampling_method == "latin":
            # latin hypercube sampling
            sampler = qmc.LatinHypercube(d=designs_dimension)
            submit_designs = sampler.random(
                n=max_trial_number)

        elif sampling_method == "random":
            # random sampling
            submit_designs = np.random.random(
                size=(max_trial_number, designs_dimension)
            )

        return submit_designs
