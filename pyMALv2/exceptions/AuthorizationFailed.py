class AuthorizationFailed(Exception):
    def __init__(self, message):
        self.message = message
        self.__init__(self.message)

