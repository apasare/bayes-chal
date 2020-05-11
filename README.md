### Challenge requirements

For the code challenge we would like you to implement the following scenario in Python:

Data is being fed via RabbitMQ to a predictor. The predictor returns the probability that the data belongs to class 1. This probability is being sent back to the queue. The predictor is able to accept values from two different data sources. The sources are switched via a parameter. The design of the switch is up to you.

In the attached zip file you will find a serialized model and two sets of data, representing the two data sources. The model is a logistic regressor and was generated using sklearn 0.20.0. Its input is 3-dimensional numpy array of [feature1, feature2, feature3]. No further transformations need to be done on the data. We added a python file that takes care of the predict() function for you, but you don't have to use it if you have a better idea.

Goals:
- Run RabbitMQ in a docker container (preferably with a docker-compose setup)
- Publish sources data to RabbitMQ
- Consume messages from RabbitMQ in the predictor
- Run predictions based on the data
- Switch between two data sources
- Bonus: logging
- Bonus: make it robust

### Instalation

```bash
git clone git@github.com:godvsdeity/bayes-chal.git
cd bayes-chal
python3 -m venv venv
source venv/bin/activate
pip install .
```

### Usage

#### 1. Run RabbitMQ docker container

```bash
docker-compose up
```

#### 2. Run the consumer

```bash
source venv/bin/activate # make sure you are on the right venv
bayes rabbitmq:consumer:data
```

#### 3. Run the producers

```bash
source venv/bin/activate # make sure you are on the right venv
bayes rabbitmq:producer:data data/code_challenge_data1.csv
bayes rabbitmq:producer:data data/code_challenge_data2.csv
```
