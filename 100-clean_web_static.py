#!/usr/bin/python3
"""
a python script to create a targ file of all my static files
"""
from fabric.api import *

env.hosts = ['52.206.18.131', '54.157.130.186']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'

def do_clean(number=0):
    number = 1 if int(number) == 0 else int(number)

    # Local cleanup
    local('ls -t versions/*.tgz | tail -n +{} | xargs rm -rf'.format(number + 1))

    # Remote cleanup
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs rm -rf'.format(number + 1))

