import sys
import logging

from ..service import DIC

# TODO the config can be loaded from a file(json/yml) or env variables
container = DIC(config={
    'logging': {
        'level': logging.DEBUG,
        'format': '%(asctime)-15s %(name)s.%(levelname)s %(message)s'
    },
    'rabbitmq': {
        'host': 'localhost',
        'port': 5672,
        'username': 'bayes',
        'password': 'bayes',
        'virtual_host': 'bayes',
        'data_queue': 'data',
        'prediction_queue': 'prediction'
    },
    'prediction_model': 'data/code_challenge_model.p'
})

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(container.config.logging.level())
handler.setFormatter(logging.Formatter(
    container.config.logging.format()
))
container.logger().addHandler(handler)
