#!/usr/bin/env python3

import os
import sys
import cv2
import time

CAMERA_ID = 0       # select camera
LENGTH = 60.0       # length for each video: 60s
TIMES = 60          # quit after 60 sections (1 hour in total) are recorded
SHAPE = (640, 480)


def get_timing():
    start = time.time()
    def timing():
        return time.time() - start
    return timing


if __name__ == '__main__':
    timing = get_timing()
    count = 0
    cap = cv2.VideoCapture(CAMERA_ID)
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    if not os.path.exists(directory):
        print('Create directory:', directory)
        os.makedirs(directory)

    print('Start recording...')

    for count in range(0, TIMES):
        filename = '%s/%s_%d.avi' % (directory, time.strftime('%m-%d_%H-%M-%S'), count + 1)

        # for py3
        out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 30.0, SHAPE)
        # for py2
        # out = cv2.VideoWriter(filename, cv2.cv.CV_FOURCC(*'MJPG'), 30.0, SHAPE)

        timing = get_timing()
        try:
            while timing() < LENGTH:
                ok, frame = cap.read()
                if ok:
                    # frame = cv2.flip(frame, 1) # flip the frame when necessary
                    # cv2.imshow('Live', frame)
                    out.write(frame)
        except KeyboardInterrupt:
            out.release()
            print("\nSaved", filename)
            break
        out.release()
        print("Saved", filename)

    cap.release()
    print('Stop recording')
    #cv2.destroyAllWindows()

