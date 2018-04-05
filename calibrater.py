#!/usr/bin/env python3

import cv2
import numpy as np
import copy

'''
A tool for calibrating self_aiming system
'''

width, height = 640, 480
mid_x, mid_y = width // 2, height // 2

cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    frame = cv2.resize(frame, (width, height))
    cv2.circle(img=frame, center=(mid_x, mid_y), radius=30, color=(0, 0, 255), thickness=2, lineType=15)
    cv2.line(frame, (mid_x - 40, mid_y), (mid_x + 40, mid_y), color=(0, 0, 255), thickness=1)
    cv2.line(frame, (mid_x, mid_y - 40), (mid_x, mid_y + 40), color=(0, 0, 255), thickness=1)
    if cv2.waitKey(1) == ord('q'):
        break
    cv2.imshow('Self-aiming System Calibrater', frame)
