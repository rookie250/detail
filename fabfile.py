

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "git@github.com:rookie250/detail.git"

env.user = 'root'
env.password = 'mmix1009'

# 填写你自己的主机对应的域名
env.hosts = ['www.zhoublog.kim']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '26421'


def deploy():
    source_folder = '/home/zhou/sites/www.zhoublog.kim/detail'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('restart gunicorn-www.zhoublog.kim')
    sudo('service nginx reload')
