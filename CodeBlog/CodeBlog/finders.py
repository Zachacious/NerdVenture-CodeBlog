from pipeline.finders import PipelineFinder

from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


class LeftoverPipelineFinder(PipelineFinder):
    """This finder is expected to come AFTER 
    django.contrib.staticfiles.finders.FileSystemFinder and 
    django.contrib.staticfiles.finders.AppDirectoriesFinder in 
    settings.STATICFILES_FINDERS.
    If a path is looked for here it means it's trying to find a file
    that none of the regular staticfiles finders couldn't find.
    """
    def find(self, path, all=False):
        # Before we raise an error, try to find out where,
        # in the bundles, this was defined. This will make it easier to correct
        # the mistake.
        for config_name in 'STYLESHEETS', 'JAVASCRIPT':
            config = settings.PIPELINE[config_name]
            for key in config:
                if path in config[key]['source_filenames']:
                    raise ImproperlyConfigured(
                        'Static file {!r} can not be found anywhere. Defined in '
                        "PIPELINE[{!r}][{!r}]['source_filenames']".format(
                            path,
                            config_name,
                            key,
                        )
                    )
        # If the file can't be found AND it's not in bundles, there's
        # got to be something else really wrong.
        raise NotImplementedError(path)