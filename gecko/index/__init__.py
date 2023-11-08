from typing import Optional, List, Dict

from gecko import RedisModel


class Initializer:
    async def __init__(
        self,
        connection_string: str,
        document_models: Optional[List[RedisModel]] = [],
    ) -> None:
        """
        Gecko initializer. Oversees the processing and indexing of RedisModels

        :param connection_string: str - Redis connection url
        :param document_models: Optional[List[RedisModel]] - RedisModel items
        :return None
        """

        self.document_models = document_models
        self.connection_string = connection_string

    @classmethod
    def get_model_fields(cls, model: RedisModel) -> Dict[str, str]:
        """
        Takes in a model and returns all attributes and associated types.

        :param model: RedisModel - Database model.
        :return List[field, type]
        """
        fields_with_types = model.__annotations__

        item = {}
        for field, field_type in fields_with_types.items():
            item[field] = field_type
        return item


async def index_db(
    connection_string: Optional[str] = None,
    document_models: Optional[List[RedisModel]] = None,
):
    """
    Gecko initialization

    :param connection_string: str - Redis connection string
    :param document_models: List[RedisModel] - model classes
    :return: None
    """

    await Initializer(
        connection_string=connection_string, document_models=document_models
    )