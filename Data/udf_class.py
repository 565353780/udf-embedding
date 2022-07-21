#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from Data.udf import UDF

class UDFClass(object):
    def __init__(self, udf_class_folder_path):
        self.udf_class_folder_path = udf_class_folder_path
        if self.udf_class_folder_path[-1] != "/":
            self.udf_class_folder_path += "/"

        self.class_udf_dict = {}
        self.class_name_list = []
        self.class_udf_name_list_list = []

        self.loadUDFClass()
        return

    def loadClassName(self):
        folder_name_list = os.listdir(self.udf_class_folder_path)
        for folder_name in folder_name_list:
            folder_path = self.udf_class_folder_path + folder_name + "/"
            if not os.path.isdir(folder_path):
                continue

            self.class_udf_dict[folder_name] = {}
        return True

    def loadClassUDF(self):
        for class_name in self.class_udf_dict.keys():
            class_folder_path = self.udf_class_folder_path + class_name + "/"

            for root, _, files in os.walk(class_folder_path):
                if "udf.npy" not in files:
                    continue

                class_udf_folder_label = root.replace(class_folder_path, "")

                udf = UDF(root + "/")
                self.class_udf_dict[class_name][class_udf_folder_label] = udf
        return True

    def updateDictKeys(self):
        self.class_name_list = list(self.class_udf_dict.keys())

        for i in range(len(self.class_name_list)):
            class_name = self.class_name_list[i]
            class_udf_folder_label_list = list(self.class_udf_dict[class_name].keys())
            self.class_udf_name_list_list.append(class_udf_folder_label_list)
        return True

    def loadUDFClass(self):
        if not os.path.exists(self.udf_class_folder_path):
            print("[ERROR][UDFClass::loadUDFClass]")
            print("\t udf_class_folder not exist!")
            return False

        if not self.loadClassName():
            print("[ERROR][UDFClass::loadUDFClass]")
            print("\t loadClassName failed!")
            return False

        if not self.loadClassUDF():
            print("[ERROR][UDFClass::loadUDFClass]")
            print("\t loadClassUDF failed!")
            return False

        if not self.updateDictKeys():
            print("[ERROR][UDFClass::loadUDFClass]")
            print("\t updateDictKeys failed!")
            return False
        return True

