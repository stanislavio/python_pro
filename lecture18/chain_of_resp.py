class Logger:
    INFO = 1
    DEBUG = 2
    ERROR = 3

    def __init__(self, level):
        self.level = level
        self.next_logger = None

    def set_next_logger(self, next_logger):
        self.next_logger = next_logger

    def log_message(self, level, message):
        if self.level <= level:
            self.write(message)
        if self.next_logger is not None:
            self.next_logger.log_message(level, message)

    def write(self, message):
        pass


class ConsoleLogger(Logger):
    def write(self, message):
        print(f"Console Logger: {message}")


class FileLogger(Logger):
    def write(self, message):
        with open("log.txt", "a") as file:
            file.write(f"File Logger: {message}\n")


class ErrorLogger(Logger):
    def write(self, message):
        print(f"Error Logger: {message}")


console_logger = ConsoleLogger(Logger.INFO)
file_logger = FileLogger(Logger.DEBUG)
error_logger = ErrorLogger(Logger.ERROR)

console_logger.set_next_logger(file_logger)
file_logger.set_next_logger(error_logger)

console_logger.log_message(Logger.INFO, "This is an information.")
console_logger.log_message(Logger.DEBUG, "This is a debug level information.")
console_logger.log_message(Logger.ERROR, "This is an error information.")

breakpoint()