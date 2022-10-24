
import yaml
import json
import random

def get_params():
    with open('params.yaml', 'r') as fd:
        return yaml.safe_load(fd)
p = get_params()['some_param']


train_results=[]
test_results=[]
for i in range(1, 4):
    train_results.append({'x_value': i, 'accuracy': i*p, 'other_metric_train': i*p*0.5})
    test_results.append({'x_value': i, 'accuracy': i*p*2, 'other_metric_test': i*p})

with open('train_results.json', 'w') as fd:
    json.dump(train_results, fd)

with open('test_results.json', 'w') as fd:
    json.dump(test_results, fd)


