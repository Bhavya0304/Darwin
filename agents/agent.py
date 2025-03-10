import importlib
import os
import importlib.util
from enum import Enum

class AvailableModel(Enum):
    LLAMA3_70b='llama3_70b'
    GEMINI='gemini_2_flash'


def import_module_from_path(path):
    spec = importlib.util.spec_from_file_location("module_name", path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module

class Agent:
    def __init__(self,model):
        root = os.getcwd()
        path = "agents/models/" + model + "/run.py"
        self.model = import_module_from_path(path)
    def Run(self,query):
        return self.model.Run(query)
        
    