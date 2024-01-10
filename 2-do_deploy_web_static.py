#!/usr/bin/python3
"""
Fabric script (based on the file 1-pack_web_static.py) that distributes
an archive to your web servers
"""
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['100.26.168.142', '100.25.35.218']
env.user = 'ubuntu'
env.key_filename = 'private_key.txt'


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers
    """
    if not os.path.exists(archive_path):
        return False

    try:
        archive_filename = os.path.basename(archive_path)
        archive_no_ext = os.path.splitext(archive_filename)[0]
        """ Upload the archive to tmp directory on the web server """
        put(archive_path, '/tmp/')

        """ Create the folder for the new version """
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))

        """ Uncompress the archive to the folder """
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_filename, archive_no_ext))

        """ Delete the archive from the web server """
        run('rm /tmp/{}'.format(archive_filename))

        """ Move the contents to the proper directory """
        run('mv / data/web_static/releases/{}/web_static/*
                / data/web_static/releases/{} /'
            .format(archive_no_ext, archive_no_ext))

        """ Delete the uncessary folder """
        run('rm -rf /data/web_static/releases/{}/web_static'
            .format(archive_no_ext))

        """ Delete the symbolic link /data/web_static/current"""
        run('rm -rf /data/web_static/current')

        """ Create a ne symbolic link """
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'
            .format(archive_no_ext))

        print("New version deployed!")
        return True

    except Excetion as e:
        return False
