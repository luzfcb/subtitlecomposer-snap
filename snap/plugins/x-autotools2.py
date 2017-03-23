from snapcraft.plugins import autotools


class Autotools2Plugin(autotools.AutotoolsPlugin):
    @classmethod
    def schema(cls):
        schema = super().schema()
        schema['properties']['configflags'] = {
            'type': 'array',
            'minitems': 1,
            'uniqueItems': False,
            'items': {
                'type': 'string',
            },
            'default': [],
        }

        return schema
