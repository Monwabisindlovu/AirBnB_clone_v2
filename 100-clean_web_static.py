#!/usr/bin/env python3
"""
Fabric script that deletes out-of-date archives.
"""

from fabric.api import env, local, run, lcd
import os

env.hosts = ['52.206.18.131', '54.157.130.186']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'

def do_clean(number=0):
    """
    Deletes out-of-date archives.
    """
    try:
        number = int(number)
    except ValueError:
        return False

    if number < 0:
        return False

    # Local cleaning
    with lcd('versions'):
        local('ls -t | tail -n +{} | xargs -I {{}} rm {{}}'.format(number + 1))

    # Remote cleaning
    with cd('/data/web_static/releases'):
        run('ls -t | tail -n +{} | xargs -I {{}} rm -r {{}}'.format(number + 1))

    return True

