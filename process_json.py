# -*- coding: utf-8 -*-
import json


with open('./video-json/campus.json') as json_file:
    data = json.load(json_file)
    print(data)

    for i in range(len(data)):
        if (i+1) % 20 == 1:
            print("shipinzhenbianhao#")
            print("\nxiangsubili")

        print(data[i]['0'])
        print("#\n")
        print(data[i]['3'])
        if (i+1) % 20 == 0:
            print("\n")
