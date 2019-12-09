import click
import pandas
import json
import uuid

from bayes.util import container


@click.option('--chunksize', default=10, help='The chunk size for csv parser. Default: 10.')
@click.argument('source', metavar='<source>')
def data_producer(chunksize, source):
    try:
        container.logger().info('Connect to rabbitmq')
        rabbitmq_client = container.rabbitmq_client()

        queue = container.config.rabbitmq.data_queue()
        rabbitmq_client.queue_declare(queue=queue)

        container.logger().debug('Parsing data from source: %s', source)
        dataframe = pandas.read_csv(source, chunksize=chunksize)
        for chunk in dataframe:
            for features in chunk.values:
                message = json.dumps({
                    'id': str(uuid.uuid4()), # to be able to identify it on prediction queue
                    'features': features[1:].tolist()
                })
                rabbitmq_client.publish(queue, message)

    except Exception as e:
        container.logger().error(str(e))
