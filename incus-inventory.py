#!/usr/bin/env python3

### usage
# chmod +x inventory.py
# ansible-inventory -i inventory.py --list

import subprocess
import json

incus = '/usr/bin/incus'

stream = subprocess.run([ incus, "list", "--format", "json" ], capture_output=True)
hosts = json.loads(stream.stdout)

hostvars = {}

groups = { "ungrouped": { "hosts": [] } }

for h in hosts:
    groups["ungrouped"]["hosts"].append(h["name"])
    hostvars[h["name"]] = {
        "raw": h,
    }

output = json.dumps({
    "_meta": {
        "hostvars": hostvars
    },
    "all": {
        "children": list(groups.keys())
    }
} | groups)

print(output)