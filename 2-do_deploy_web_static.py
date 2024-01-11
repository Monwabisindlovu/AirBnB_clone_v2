#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers
"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['52.206.18.131', '54.157.130.186']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'

def do_deploy(archive_path):
    """
    Deploys the archive to web servers
    """
    if not exists(archive_path):
        return False

    # Extract the file name from the archive_path
    file_name = archive_path.split("/")[-1]
    name = file_name.split(".")[0]

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, '/tmp/{}'.format(file_name))

    # Uncompress the archive
    run('mkdir -p /data/web_static/releases/{}/'.format(name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(file_name, name))

    # Delete the archive from the web server
    run('rm /tmp/{}'.format(file_name))

    # Move the content out of the web_static folder
    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(name, name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(name))

    # Delete the current symbolic link
    run('rm -rf /data/web_static/current')

    # Create a new symbolic link
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(name))

    print("New version deployed!")
    return True

