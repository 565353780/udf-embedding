#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torch.utils.data import Dataset

from Data.udf_class import UDFClass

class UDFDataset(Dataset):
    def __init__(self, udf_root_folder_path):
        super().__init__()

        self.udf_root_folder_path = udf_root_folder_path
        if self.udf_root_folder_path[-1] != "/":
            self.udf_root_folder_path += "/"

        self.udf_class = UDFClass(self.udf_root_folder_path)
        return

