#!/usr/bin/env python3

import sys
import re

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]

    matching = re.findall(re.escape(keyword), text)

    if len(matching) > 0:
        print(len(matching))
    else:
        print("none")
else:
    print("none")