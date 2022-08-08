import typing

from annadb.data_types.journal import QuerySet
from annadb.query.base import FindInterface
from annadb.query.types import Limit

if typing.TYPE_CHECKING:
    from annadb.collection import Collection


class LimitQuery(FindInterface):
    def __init__(
        self, number: int, query_set: QuerySet, collection: "Collection"
    ):
        self.collection = collection
        self.query_set = query_set
        self.query_set.push(Limit(number))