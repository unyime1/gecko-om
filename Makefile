format:
	python -m black --line-length 79 .

lint:
	flake8 .

test:
	docker-compose up
	pytest -v -s

build:
	python3 -m build


connect-stack:
	redis-cli -h localhost -p 6380

run-redis:
	docker-compose up
