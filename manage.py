import os
import sys

root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'ecommerce2'))
sys.path.insert(0, root_path)

