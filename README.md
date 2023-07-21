# Tutorial 

From [oss.redis.com/redisgears/intro.html](oss.redis.com/redisgears/intro.html)


## Run Redis Gears Docker Container


	docker run -d --name redisgears -p 6379:6379 redislabs/redisgears:latest

## Run redis-cli Docker Container


	docker exec -it redisgears redis-cli

## Execute Python (on redis-cli)


### First execution


	RG.PYEXECUTE "GearsBuilder().run()"


### Add some keys


	hset person:1 name "Rick Sanchez" age 70
	hset person:2 name "Morty Smith" age 14

	RG.PYEXECUTE "GearsBuilder().run()"

	RG.PYEXECUTE "GearsBuilder().run('person:*')"


### Filtering keys


	RG.PYEXECUTE "GB().filter(lambda x: x['key'].startswith('person:')).run()"


### Executing from outside redis-cli


	cat mygear.py | docker exec -i redisgears redis-cli -x RG.PYEXECUTE


### Executing accumulate.py


	cat accumulate.py | docker exec -i redisgears redis-cli -x RG.PYEXECUTE


### Executing avg_and_count.py


	cat avg_and_count.py docker exec -i redisgears redis-cli -x RG.PYEXECUTE


### Nonblocking execution


	RG.PYEXECUTE "GB().run()" UNBLOCKING
	RG.DUMPEXECUTIONS
	RG.GETRESULTS <id> -- <id> returned by DUMPEXECUTIONS




