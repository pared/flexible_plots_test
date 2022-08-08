
import yaml
import json
import random

def get_params():
    with open('params.yaml', 'r') as fd:
        return yaml.safe_load(fd)
p = get_params()['some_param']


def prepare_cm(num_classes=3,num_samples=3):
    result = []
    for i in range(num_classes):
        for j in range(num_samples):
            if random.random() <= p:
                result.append({'actual': i, 'predicted': i})
            else:
                result.append({'actual': i, 'predicted': random.choice(list(range(num_samples)))})
    return result

res1=[]
res2=[]
for i in range(1, 11):
    res1.append({'x': i, 'y': i * p})
    res2.append({'x': i, 'z': i * p*2})

with open('res1.json', 'w') as fd:
    json.dump(res1, fd)

with open('res2.json', 'w') as fd:
    json.dump(res2, fd)

with open('metric1.json', 'w') as fd:
    json.dump(res1[-1],fd)

with open('metric2.json', 'w') as fd:
    json.dump(res2[-1],fd)

with open('confusion_matrix.json', 'w') as fd:
    json.dump(prepare_cm(), fd)

import shutil
shutil.copyfile('confusion_matrix.json', 'confusion_matrix2.json')

