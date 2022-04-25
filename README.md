# Channels Redis connection leak demo

Demo of `AsyncWebsocketConsumer` Redis connection leak discussed in django/channels_redis#279.

## Setup

Tweak `requirements.txt` to select `channels_redis` and `aioredis` versions, install deps.

## Run server

```
daphne -v 0 --ping-interval 2000 --ping-timeout 2000 testapp.channels:application
```

(pings disabled here for testing with Tsung)

## Test

Use your favorite WebSocket load testing framework, or test with Tsung using the included `tsung.xml` config:

```
tsung -kf tsung.xml start
```

The Redis connection count can be monitored with:

```
netstat -tn|grep ":6379 *ESTAB"|wc -l
```

By default `tsung.xml` will start 500 client connections in one second, which leaks around 300 Redis connections on my system.

Modify `arrivalrate` to change the arrival rate, or `maxnumber` and `global_number` for the total number of client connections.

Tsung can be installed with `sudo apt install tsung` on Debian, or from source at http://tsung.erlang-projects.org/
