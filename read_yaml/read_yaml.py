import yaml

with open('employee.yaml') as f:
    yaml_contents = yaml.load_all(f, Loader=yaml.FullLoader)
    print(yaml_contents)
    print(list(yaml_contents))