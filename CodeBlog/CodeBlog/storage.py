from django.contrib.staticfiles.storage import ManifestStaticFilesStorage

from pipeline.storage import GZIPMixin


class GZIPManifestStorage(GZIPMixin, ManifestStaticFilesStorage):
    pass