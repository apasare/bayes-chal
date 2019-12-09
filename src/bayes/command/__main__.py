#!/usr/bin/env python
import click


from bayes.command import data_producer, data_consumer


@click.group()
def cli():
    pass


# TODO there's actually a better way to do this by using a custom multicommand loader
cli.command(name='rabbitmq:producer:data')(data_producer)
cli.command(name='rabbitmq:consumer:data')(data_consumer)


if __name__ == '__main__':
    cli()
