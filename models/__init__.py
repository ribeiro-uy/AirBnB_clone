#!/usr/bin/python3
"""init module"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
