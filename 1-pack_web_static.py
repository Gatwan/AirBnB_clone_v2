#!/usr/bin/python3
""" Generates an archive from the web_static folder """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Creates an archive """
    time = datetime.now()
    time_format = time.strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    archive_path = "versions/web_static_{}.tgz".format(time_format)
    execute = local("tar -czvf {} web_static".format(archive_path))

    if execute.failed:
        return None
    else:
        return archive_path
