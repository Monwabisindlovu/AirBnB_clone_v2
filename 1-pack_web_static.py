#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents of the
web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents ofthe web_static folder
    """
    try:
        """ Create the version folder if it doesnt exist"""
        if not os.path.exists("versions"):
            local("mkdir -p versions")

        """ Create the archive filename """
        now = datetime.now()
        archive_name = "web_static_{}{}{}{}{}{}.tgz".format(
                now.year, now.month, now.day, now.hour, now.minute, now.second)

        """ Compress the contents of the web_static folder """
        local("tar -cvzf versions/{} web_static".format(archive_name))

        """ Return the archive path if generated successfully"""
        return "versions/{}".format(archive_name)

    except Exception as e:
        return None
