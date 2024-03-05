#!/usr/bin/python3
"""__inti__ intializes the models directory by
importing the FileStrage Class to create a storage object 
then reloads the storage object."""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload

