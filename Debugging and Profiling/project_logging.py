import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a Debug message ")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("this is critical message")

#log formating
# logging.basicConfig(filename= 'example.log',format= '%(asctime)s - %(levelname)s -%(message)s',level=logging.DEBUG)
# logging.debug("this is Debug Message")

#Creating handlers

file_handler = logging.FileHandler('example2.log')
file_handler.setLevel(logging.DEBUG)
logging.basicConfig(format= '%(asctime)s - %(levelname)s -%(message)s',level=logging.DEBUG,handlers=[file_handler])
logging.debug("this is debug message")