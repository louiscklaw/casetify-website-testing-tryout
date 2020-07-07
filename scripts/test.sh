#!/usr/bin/env bash

set -ex

# appium-doctor
reset

pipenv run python3 ./test/aut-helloworld.py

# python3 ./test/android-helloworld.py
