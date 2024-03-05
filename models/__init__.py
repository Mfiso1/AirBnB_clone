#!/usr/bin/python3
"""__init__ intializes the models directory by
importing the FileStrage Class to create a storage object 
then reloads the storage object."""
from models.engine.file_storage import FileStorage

storage = file_storage.FileStorage()
storage.reload

