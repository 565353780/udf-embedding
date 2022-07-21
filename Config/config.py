#!/usr/bin/env python
# -*- coding: utf-8 -*-

CONFIG = {
    'gpu': 'cuda',
    'batch_size': 128,
    'num_epochs': 5000,
    'lr': 1e-3,
    'weight_decay': 5e-4,
    'num_workers': 4,
    'udf_root_folder_path': '/home/chli/scan2cad/im3d_udf/',
    'triplet_margin': 1e-2,
    'log_frequency': 10,
    'validate_frequency': 250,
    'checkpoint_frequency': 1000,
    'output_root': './out/'
}

