#!/usr/bin/env python3

import os,sys
from pprint import pprint

from diffimg import diff

print('diffing different image')
print(diff('_POC/diffimg/helloworld_a.png', '_POC/diffimg/helloworld_b.png'))

print('diffing same image')
print(diff('_POC/diffimg/helloworld_a.png', '_POC/diffimg/helloworld_a.png'))
