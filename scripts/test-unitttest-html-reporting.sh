#!/usr/bin/env bash

set -ex

reset

rm -rf docs

pipenv run python3 test/test-unittest.py
