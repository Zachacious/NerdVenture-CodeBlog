from django.contrib.staticfiles.storage import ManifestStaticFilesStorage, CachedStaticFilesStorage

from django.contrib.staticfiles.storage import CachedFilesMixin, ManifestFilesMixin

from pipeline.storage import PipelineMixin, GZIPMixin

class CustomStorage(PipelineMixin, ManifestStaticFilesStorage):
    manifest_strict = False

class GZIPStorage(GZIPMixin, CachedStaticFilesStorage):
    pass