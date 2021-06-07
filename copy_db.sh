#!/bin/bash

# Terminal command to copy local (postgresql) databse to remote server

pg_dump -C -h localhost -U localuser dbname | psql -h remotehost -U remoteuser dbname

# Terminal command to copy remote (postgresql) database to local client

pg_dump -C -h remotehost -U remoteuser dbname | psql -h localhost -U localuser dbname
