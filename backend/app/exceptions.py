class NotFoundError(Exception):
    pass

class InvalidUUIDError(Exception):
    pass

class JsonParseError(Exception):
    pass

class EmptyBodyError(Exception):
    pass

class DatabaseError(Exception):
    pass