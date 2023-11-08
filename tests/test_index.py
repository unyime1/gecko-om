import pytest

from tests.conftest import CarModel
from gecko.index import Initializer


pytestmark = pytest.mark.asyncio


class TestGetFields:
    async def test_get_model_fields(self):
        field_with_types = Initializer.get_model_fields(CarModel)
        for field, type in field_with_types.items():
            if field == "model":
                assert type == str
            if field == "age":
                assert type == int
            if field == "faulty":
                assert type == bool
