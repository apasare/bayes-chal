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
