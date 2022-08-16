import sys
import json

arg_list = sys.argv
new_list = []
fileName = arg_list[0]
list_names = []

for arg in arg_list:
    if arg != fileName:
        new_list.append(arg)
        list_names.append({
            "CNAME": {
                "Host": arg,
                "Value": "url",
            },
            "CNAMEapi": {
                "Host": arg + "api",
                "Value": "url",
            },
            "TXT": {
                "Host":  arg,
                "Value": "txt-value",
            },
            "TXTapi": {
                "Host":  arg + "api",
                "Value": "txt-value",
            }
        })

with open(arg_list[1] + '.txt', 'x') as f:
    for index, item in enumerate(new_list):
        f.write('%s:\n' % (list_names[index]))
        for key, value in item.items():
            f.write('    %s:\n' % (key))
            for nkey, nvalue in value.items():
                f.write("    %s: %s \n" % (nkey, nvalue))
        f.write('\n')
