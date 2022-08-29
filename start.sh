#!/usr/bin/env bash

docker-compose up --force-recreate -d

echo "Paste: source venv/bin/activate"

echo "To load data into database please run:  python src/main/assignment/load_database.py"

echo "To get a random image please run: python src/main/assignment/main.py"
echo "You will find test.jpg in src/main/assignment"

echo "Run tests using: cd src; python setup.py test "
