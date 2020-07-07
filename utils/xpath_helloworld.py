#!/usr/bin/env python3

import os,sys
from pprint import pprint

from io import StringIO

from lxml import etree


# f = StringIO('<foo><bar></bar></foo>')
# f = ''.join(open('./helloworld.xml','r').readlines())
tree = etree.parse('./debug.xml')
# tree = etree.parse('./helloworld.xml')


r = tree.xpath('//android.view.View[@text="CUSTOM STUDIO"]')
print(r[0].tag)


# r = tree.xpath('bar')
# print(r[0].tag)