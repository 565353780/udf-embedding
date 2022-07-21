#!/usr/bin/env python
# -*- coding: utf-8 -*-

def stepwise_learning_rate_decay(optimizer,
                                 learning_rate,
                                 iteration_number,
                                 steps,
                                 reduce=0.1):
    if iteration_number in steps:
        steps.remove(iteration_number)
        learning_rate *= reduce
        print("Reduce learning rate to {}".format(learning_rate))

        for param in optimizer.param_groups:
            param["lr"] = learning_rate

    return learning_rate

