#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:qinxiaoran
@file:data_tmp.py
@time:2018/01/03
"""
from __future__ import division, print_function, absolute_import
import os
import os.path as osp

if __name__ == '__main__':
    lfw_dir = '/data2/qinxiaoran/lfw'
    lfw_deepf_dir = osp.join(lfw_dir, 'lfw-deepfunneled')
    lfw_deepc_dir = osp.join(lfw_dir, 'lfw-deep-MTCNNcrop')
    subdirs = os.listdir(lfw_deepf_dir)
    subdirs.sort()
    for subdir in subdirs:
        f_path = osp.join(lfw_deepf_dir, subdir)
        c_path = osp.join(lfw_deepc_dir, subdir)
        f_imgs = os.listdir(f_path)
        f_len = len(f_imgs)
        c_imgs = os.listdir(c_path)
        c_len = len(c_imgs)
        if f_len != c_len:
            print(subdir)