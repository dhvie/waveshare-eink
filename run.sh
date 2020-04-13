#!/bin/bash

source ~/.bashrc
cd ~/waveshare-eink/waveshare_eink/server
gunicorn start:app --daemon

cd ../../
python -m waveshare_eink.display --refresh 3600
