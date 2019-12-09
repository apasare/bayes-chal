import click
import pandas
import pika
import json
import numpy

from bayes.util import container


def data_callback(channel, method, properties, body):
    data = json.loads(body)
    features = numpy.array(data['features'])
    prediction = container.prediction_model().predict(features.reshape(1, -1))

    prediction_message = json.dumps({
        'id': data['id'],
        # i'm assuming that the prediction vector looks like this: [[class1prob, class2prob]]
        'class_1_probability': prediction[0, 0]
    })
    container.rabbitmq_client().publish(
        container.config.rabbitmq.prediction_queue(), prediction_message)

    channel.basic_ack(delivery_tag=method.delivery_tag)


def data_consumer():
    try:
        container.logger().info('Connect to rabbitmq')
        rabbitmq_client = container.rabbitmq_client()

        # declare queues
        data_queue = container.config.rabbitmq.data_queue()
        prediction_queue = container.config.rabbitmq.prediction_queue()
        rabbitmq_client.queue_declare(data_queue)
        rabbitmq_client.queue_declare(prediction_queue)

        # start data consumer
        rabbitmq_client.consume(
            data_queue, on_message_callback=data_callback)
        rabbitmq_client.start_consuming()
    except Exception as e:
        container.logger().error(str(e))
