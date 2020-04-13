#!/bin/bash -e

source /home/$(whoami)/setup-env.sh
cd /home/$(whoami)/waveshare-eink/waveshare_eink/server
gunicorn start:app --daemon

cd ../../
python -m waveshare_eink.display --refresh 3600
