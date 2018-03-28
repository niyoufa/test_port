# @Time    : 2018/3/25 下午3:58
# @Author  : Niyoufa
from torserver.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """
    测试
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--param1", "-p1",
            help = ("test"),
            default= 1,
            type = int
        )
        parser.add_argument(
            "p2",
            help=("test"),
            default=1,
            type=lambda x:x.split(".")
        )
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        print("test：{args}, {options}".format(args=args, options=options))
        from tornado.options import options
        print(options.module_name)