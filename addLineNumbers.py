# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 10:08:33 2023

@author: sunhwan.an
"""
with open('blink.ino', 'r') as program: #원본 파일 경로를 입력
    data = program.readlines()

with open('blink_with_linenum.ino', 'w') as program: #출력 파일 경로 입력
    for (number, line) in enumerate(data):
        program.write('%4d  %s' % (number + 1, line))
