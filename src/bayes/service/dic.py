import logging
import pika
import pickle
from dependency_injector import containers, providers

from .rabbitmq import RabbitMQClient
from .prediction_model import PredictionModel


# Dependency Injection Container
class DIC(containers.DeclarativeContainer):
    config = providers.Configuration('config')

    logger = providers.Singleton(
        logging.Logger, name='BAYES')

    # rabbitmq
    rabbitmq_credentials = providers.Factory(
        pika.PlainCredentials, username=config.rabbitmq.username, password=config.rabbitmq.password)
    rabbitmq_parameters = providers.Factory(pika.ConnectionParameters, host=config.rabbitmq.host,
                                            port=config.rabbitmq.port, virtual_host=config.rabbitmq.virtual_host, credentials=rabbitmq_credentials)
    rabbitmq_connection = providers.Factory(
        pika.BlockingConnection, parameters=rabbitmq_parameters)
    rabbitmq_client = providers.Singleton(
        RabbitMQClient, connection=rabbitmq_connection, logger=logger)

    # model
    prediction_model = providers.Singleton(
        PredictionModel, file_path=config.prediction_model)
