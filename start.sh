#!/bin/bash
nohup redis-server &
uwsgi --http 0.0.0.0:5000 --module mymodule.wsgi