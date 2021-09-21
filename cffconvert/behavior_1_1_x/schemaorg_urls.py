from cffconvert.behavior_shared.schemaorg_urls_shared import SchemaorgUrlsShared as Shared


class SchemaorgUrls(Shared):

    def __init__(self, cffobj):
        super().__init__(cffobj)

    def as_tuple(self):
        key = ''.join([
            '_',
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
