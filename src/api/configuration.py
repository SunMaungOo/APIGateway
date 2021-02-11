from decouple import config
import socket

IS_DOCKER = config("IS_DOCKER",
                       default=True,
                       cast=bool)

SERVER_PORT = config("SERVER_PORT",cast=int)

WHITE_LIST_SERVICE_NAME = config("WHITE_LIST_SERVICE_NAME",
                                 cast=str)

LOCAL_IP = socket.gethostbyname(socket.gethostname())

if IS_DOCKER:
    #api gateway ip
    white_list_ip = socket.gethostbyname(WHITE_LIST_SERVICE_NAME)
else:
    #local ip
    white_list_ip = LOCAL_IP
    

WHITE_LIST_IP = config("WHITE_LIST_IP",
                       default=white_list_ip,
                       cast=str)
