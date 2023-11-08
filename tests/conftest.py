from gecko import RedisModel


class CarModel(RedisModel):
    model: str
    age: int
    faulty: bool
