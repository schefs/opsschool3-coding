"""
 Usage: exercise1.py <FILEPATH>
 Description: read your list of name and buckets and prints it in a new format
"""

import json
import yaml


def read_json_file(file):
    with open(file) as f:
        data = json.load(f)
    return data


def main(path):
    final_dict = {}
    my_json = read_json_file(path)
    buckets = my_json["buckets"]
    buckets.sort()
    ppl_ages = my_json["ppl_ages"]

    # Starting final dict with empty arries
    final_dict[str(buckets[0])] = []
    for i in range(len(buckets) - 1):
        final_dict[str(buckets[i]) + "-" + str(buckets[i + 1])] = []

    for ppl in ppl_ages:
        age = ppl_ages[ppl]
        if age < buckets[0]:
            final_dict[str(buckets[0])].append(ppl)
        else:
            for i in range(len(buckets) - 1):
                if buckets[i] <= age < buckets[i+1]:
                    final_dict[str(buckets[i]) + "-" + str(buckets[i+1])].append(ppl)
                    break

    with open(path.replace(".json", ".yml"), "w") as f:
        yaml.dump(final_dict, f, default_flow_style=False, allow_unicode=True)
    print(final_dict)


if __name__ == '__main__':
    main(sys.argv[1])
