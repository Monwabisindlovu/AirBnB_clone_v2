#!/usr/bin/env python3
"""
Fabric script (based on 1-pack_web_static.py) that distributes an archive
to your web servers, using the function do_deploy.
"""

from fabric.api import local, put, run, env
from datetime import datetime
import os

env.hosts = ['52.206.18.131', '54.157.130.186']
env.user = 'ubuntu'
env.key_filename = 'private-key.txt'

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir versions")
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception as e:
        return None

def do_deploy(archive_path):
    """
    Deploys an archive to the web servers.
    """
    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')

        archive_filename = os.path.basename(archive_path)
        release_folder = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0]
        )
        run('mkdir -p {}'.format(release_folder))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))

        run('rm /tmp/{}'.format(archive_filename))

        """ Move contents to proper location and clean up """
        run('mv {}/web_static/* {}'.format(release_folder, release_folder))
        run('rm -rf {}/web_static'.format(release_folder))

        """ Delete the current symbolic link """
        run('rm -rf /data/web_static/current')

        run('ln -s {} /data/web_static/current'.format(release_folder))

        print("New version deployed!")
        return True
    except Exception as e:
        return False

