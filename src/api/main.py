from flask import Flask,request
import configuration

app = Flask(__name__)

white_list_ip = list()

@app.route('/greet/<string:name>')
def greet(name:str):
    
    if not is_whitelist_ip(request.remote_addr):
        return ""
    
    return "Hello "+name

"""
check whether is it a ip we have white list
"""
def is_whitelist_ip(remote_ip:str)->bool:
    return remote_ip in white_list_ip

def main():
    
    print(f"SERVICE IP:{configuration.LOCAL_IP}",flush=True)

    white_list_ip.append(configuration.WHITE_LIST_IP)
    
    app.run("0.0.0.0",
            port=configuration.SERVER_PORT)

if __name__ == "__main__":
    main()