## Uses https://github.com/williamgilpin/pypdb
# $ pip install pypdb
from pypdb import *

# all_info accesses the information tied to the pdb entry and stores everything in a JSON format
# To get the most out of it, treat it as a nested key-value map
# e.g. all_info has the keys 'cell' and 'struct'. 'struct' has the key 'keywords' and so on.
all_info = get_info('4DT5')
print(list(all_info.keys()))

print(all_info.get('struct_keywords'))

print(all_info.get('struct_keywords').get('pdbx_keywords'))
