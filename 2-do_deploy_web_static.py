#!/usr/bin/python3
""" Distributes an archive to the web servers """
from fabric.api import run, put, env, with_settings


env.hosts = ['18.206.202.177', '100.25.31.46']


@with_settings(warn_only=True)
def do_deploy(archive_path):
    file_name = archive_path.split('/')[-1]
    folder_extract = file_name.replace(".tgz", "")

    put(archive_path, '/tmp')
    run('mkdir -p /data/web_static/releases/{}'.format(folder_extract))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(file_name, folder_extract))

    run('rm /tmp/{}'.format(file_name))
    run('mv -f /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}'.format(folder_extract, folder_extract))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(folder_extract))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(folder_extract))
