# @Time    : 2018/3/12 16:42
# @Author  : Niyoufa


import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 服务器调试模式, 值为False时不自动重启服务器
DEBUG = False

# 变更自动重启
AUTORELOAD = True

# cookie secret key
COOKIE_SECRET = "test"

# 是否开启csrf攻击防范
XSRF_COOKIES = True

# 允许访问的HOST配置
ALLOWED_HOSTS = []

# 模块配置，可以在配置文件中配置，也可以在ModuleModel存储模块信息
MODULES = {
    "default": {
        "name":"默认模块",
        "module_path": ["test_port.handlers.test_handlers"],
        "description": "默认模块",
        "port": 8069,
        "command_path":"test_port",
    },
}

# 安装第三方模块
INSTALLED_MODULES = [
    "torserver.addons.user"
]

# 数据库
DATABASES = {

}
