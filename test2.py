# https://martin-thoma.com/configuration-files-in-python/

import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

print(cfg['s1'])
print(cfg['s2'])