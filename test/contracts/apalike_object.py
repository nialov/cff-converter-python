from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_author(self, fixture):
        pass

    @abstractmethod
    def test_check_cffobj(self, fixture):
        pass

    @abstractmethod
    def test_doi(self, fixture):
        pass

    @abstractmethod
    def test_as_string(self, fixture):
        pass

    @abstractmethod
    def test_title(self, fixture):
        pass

    @abstractmethod
    def test_url(self, fixture):
        pass

    @abstractmethod
    def test_version(self, fixture):
        pass

    @abstractmethod
    def test_year(self, fixture):
        pass
