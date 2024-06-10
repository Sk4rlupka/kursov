#!/bin/bash
docker-compose -f docker-compose.yml down
#git pull
docker-compose -f docker-compose.yml up
