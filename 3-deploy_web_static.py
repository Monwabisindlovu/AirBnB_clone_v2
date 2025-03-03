#!/usr/bin/python3
"""
Fabric script to create and distribute an archive to web servers

Usage:
    fab -f 3-deploy_web_static.py deploy -i ~/.ssh/id_rsa -u ubuntu
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

# Update the IP addresses
env.hosts = ['52.206.18.131', '54.157.130.186']

def do_pack():
    """
    Generates a tgz archive of the web_static folder
    """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(e)
        return None

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers
    """
    if exists(archive_path) is False:
        return False
    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        
        # Upload archive
        put(archive_path, '/tmp/')
        
        # Create release folder
        run('mkdir -p {}{}/'.format(path, no_ext))
        
        # Extract files
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        
        # Clean up
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        
        # Create symbolic link
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        
        return True
    except Exception as e:
        print(e)
        return False

def deploy():
    """
    Creates and distributes an archive to the web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

