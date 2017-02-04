import import_utils

test = import_utils.import_module('copy')
print dir(test)

test = import_utils.import_module_from('copy.copy')
print dir(test)
