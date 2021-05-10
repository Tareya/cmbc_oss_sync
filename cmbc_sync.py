# -*- coding: utf-8 -*-

import os, datetime, arrow, sys, re
import zipfile, shutil

from functools import reduce
from oss_usage import oss_usage
import log_func


class CmbcSync(object):
    '''CMBC 回执单处理功能类'''

    def __init__(self, *args, **kwargs):
        '''初始化类属性'''
        self.oss      = oss_usage()
        self.log      = log_func.debug_log(logger_name='cmbc_sync', log_file=os.path.join(os.getcwd(), 'logs', 'cmbc_sync.log'))
        self.base_dir = 'C:\Program Files\CMB\FbSdk\Receipt'
        


    def get_receipt_path(self, *args, **kwargs):
        '''获取回执单路径'''
        



    def check_receipt(self, path, *args, **kwargs):
        '''检查回执单是否已存在于oss'''

    


    def remove_receipt(self, path, *args, **kwargs):
        '''移除回执单'''




    def deal_with_receipt(self, *args, **kwargs):
        '''处理回执单'''



