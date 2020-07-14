#!/usr/bin/env bash

set -ex

python3 gen_page_structure.py

dot -Tsvg site-structure.dot > site-structure.svg