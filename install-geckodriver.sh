#!/usr/bin/env bash

wget --quiet https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz --output-document geckodriver.tar.gz
tar -zxf geckodriver.tar.gz
rm geckodriver.tar.gz
ls -alh geckodriver
echo 'Awesome! geckodriver is available'