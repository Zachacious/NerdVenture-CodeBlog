from django.contrib.staticfiles.storage import CachedStaticFilesStorage

from pipeline.storage import GZIPMixin


class GZIPManifestStorage(GZIPMixin, ManifestStaticFilesStorage):
    pass