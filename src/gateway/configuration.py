from decouple import config
import socket

IS_DOCKER = config("IS_DOCKER",cast=bool)

SERVER_PORT = config("SERVER_PORT",cast=int)

API_NAME = config("API_NAME",cast=str)

LOCAL_IP = socket.gethostbyname(socket.gethostname())

if IS_DOCKER:
    #service ip
    api_ip = socket.gethostbyname(API_NAME)
else:
    #local ip
    api_ip = LOCAL_IP

API_SERVER_IP = config("API_SERVER_IP",
                       default=api_ip,
                       cast=str)
    
API_PORT = config("API_PORT",cast=int)

API_PATH = config("API_PATH",cast=str)

API_KEY = config("API_KEY",cast=str)