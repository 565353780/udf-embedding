#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class UDF(object):
    def __init__(self, udf_folder_path):
        self.udf_folder_path = udf_folder_path
        if self.udf_folder_path[-1] != "/":
            self.udf_folder_path += "/"

        self.udf_file_name_list = []

        self.loadUDFFileName()
        return

    def loadUDFFileName(self):
        if not os.path.exists(self.udf_folder_path):
            print("[ERROR][UDF::getSourceUDFFilePath]")
            print("\t udf_folder not exist!")
            return False

        file_name_list = os.listdir(self.udf_folder_path)
        for file_name in file_name_list:
            if file_name[:3] != 'udf' or file_name[-4:] != '.npy':
                continue
            self.udf_file_name_list.append(file_name)
        return True

    def getSourceUDFFilePath(self):
        if 'udf.npy' not in self.udf_file_name_list:
            print("[ERROR][UDF::getSourceUDFFilePath]")
            print("\t udf.npy not found!")
            return None

        return self.udf_folder_path + 'udf.npy'

    def getUDFFilePath(self, udf_idx):
        if udf_idx >= len(self.udf_file_name_list):
            print("[WARN][UDF::getUDFFilePath]")
            print("\t udf_idx out of range! use \% to filter as default!")
            udf_idx = udf_idx % len(self.udf_file_name_list)

        return self.udf_folder_path + self.udf_file_name_list[udf_idx]

