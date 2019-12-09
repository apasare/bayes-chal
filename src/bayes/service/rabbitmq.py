import pika


class RabbitMQClient(object):
    def __init__(self, connection, logger):
        self.connection = connection
        self.logger = logger
        self.channel = connection.channel()

    def queue_declare(self, queue, durable=True, **kwargs):
        self.logger.debug('Declare queue %s', queue)
        self.channel.queue_declare(queue=queue, durable=durable, **kwargs)

    def publish(self, queue, body):
        self.logger.debug(
            'Sending "%s" to "%s" queue', body, queue)
        self.channel.basic_publish(exchange='',
                                   routing_key=queue,
                                   body=body,
                                   properties=pika.BasicProperties(
                                       delivery_mode=2,  # make message persistent
                                   ))

    def consume(self, queue, **kwargs):
        self.logger.debug('Attach consumer to queue "%s"', queue)
        self.channel.basic_consume(queue=queue, **kwargs)
        pass

    def start_consuming(self):
        self.channel.start_consuming()

    def __del__(self):
        self.logger.debug('Close rabbitmq connection')
        self.connection.close()
