from importlib import import_module


class Resource():

    _resources = {
        'signature': 'resources.signature.SignatureResource',
    }

    def __init__(self):
        self.__resources = {}

    def __load_resource(self, name):
        if name not in self._resources:
            raise Exception('Resource not found: %s' % name)
        module_name, class_name = self._resources[name].rsplit('.', 1)
        module = import_module(module_name)
        return getattr(module, class_name)

    def __call__(self, name, *args, **kwargs):
        if name not in self.__resources:
            self.__resources[name] = self.__load_resource(
                name)(
                    *args,
                    **kwargs
            )
        return self.__resources[name]


get_resource = Resource()
