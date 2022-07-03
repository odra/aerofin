# Aerofin Development Environment

To start the dev env:

```sh
docker-compose up
```

Keep in mind that the development environment will start a local kafka instance.

This compose file will start the following components in containers:

* zookeeper (port 2181)
* kafka-broker (port 9092)
* kafka-admin (for running kafka commands but nothing stops you from doing your magic in your host machine)

This compose file was created for local development purposes only and should not be used in production.

## Verification

You can "ssh" into the kafka container using the following command:

```sh
docker exec -it aerofin-kafka-admin /bin/bash
```

Create a topic by running:

```sh
/usr/local/kafka/bin/kafka-topics.sh \
--create \
--bootstrap-server kafka-broker:9092 \
--replication-factor 1 \
--partitions 1 \
--topic org.aerofin.devenv.test
```

Produce data to the topic by running (add messages by writing something and pressing enter, press ctrl + c to stop producing data):

```sh
/usr/local/kafka/bin/kafka-console-producer.sh \
--broker-list \
kafka-broker:9092 \
--topic org.aerofin.devenv.test

> some data
> foobar
^C
```
```sh
docker exec -it aerofin_kafka-admin /bin/bash
Consume the produced data (press ctrl + c to stop):

/usr/local/kafka/bin/kafka-console-consumer.sh \
--bootstrap-server kafka-broker:9092 \
--topic org.aerofin.devenv.test \
--from-beginning

some data
foobar
^CProcessed a total of 2 messages
```
