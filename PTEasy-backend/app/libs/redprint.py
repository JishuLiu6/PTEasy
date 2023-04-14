class Redprint:
    def __init__(self, name):
        """
        初始化 Redprint 类。

        :param name: Redprint 的名称。
        """
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        """
        路由装饰器，用于将规则和选项添加到 self.mound 中。

        :param rule: 路由规则。
        :param options: 路由选项。
        :return: 装饰器。
        """
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        """
        将 Redprint 中的路由注册到蓝图（Blueprint）。

        :param bp: 要注册的蓝图（Blueprint）。
        :param url_prefix: URL 前缀，默认为 /name。
        """
        if url_prefix is None:
            url_prefix = f'/{self.name}'
        for f, rule, options in self.mound:
            endpoint = self.name + '+' + options.pop("endpoint", f.__name__)
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
