workers = {
    "employer1": {"name": "John", "salary": 7500},
    "employer2": {"name": "Emma", "salary": 8000},
    "employer3": {"name": "Brad", "salary": 500}
}
workers["employer3"]["salary"] = 8500

import pprint
pprint.pprint(workers)