from http.server import BaseHTTPRequestHandler,HTTPServer

import configuration
import requests

class ReverseProxyRequestHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_GET(self, body=True):
        try:
                        
            new_path = self.extract_path(self.path)
            
            if new_path is None:
                self.default_message()
                return
                        
            url = f"http://{configuration.API_SERVER_IP}:{configuration.API_PORT}/{new_path}"
            
            print(url,flush=True)
            
            respond = requests.get(url,headers=self.headers,verify=False)
                  
            self.send_response(respond.status_code)
            self.send_respond_header(respond.headers)
            self.wfile.write(respond.content)
        except:
            print("Something went wrong",flush=True)        
        finally:
            pass
            #self.finish()

    """
    Show a default message when there is invalid API format
    """
    def default_message(self):
        self.send_response(200)
        self.send_header("Content","text/html")
        self.end_headers()
        self.wfile.write(bytes("<h1>Sorry API cannot be reach</h1>",encoding="utf-8"))

    """
    Resend the respond header that the api give
    """
    def send_respond_header(self,headers):
        for key in headers:
            if key not in ['Content-Encoding', 'Transfer-Encoding', 'content-encoding',
                            'transfer-encoding', 'content-length', 'Content-Length']:
                self.send_header(key,headers[key])
        
        self.end_headers()

    """
    Get the api path we need to call
    """
    def extract_path(self,path:str)->str:
        blocks = path.split("/")
        
        if len(blocks)<3:
            return None
        
        if blocks[1]!=configuration.API_PATH:
            return None
        
        #check for API key
        
        if blocks[2]!=configuration.API_KEY:
            return None
                
        new_path = "/".join([str(x) for x in blocks[3:]])
                
        return new_path
        
        
def main():
    
    print(f"SERVICE IP:{configuration.LOCAL_IP}",flush=True)

    server_address = ("0.0.0.0",
                      configuration.SERVER_PORT)
    
    http_server = HTTPServer(server_address,ReverseProxyRequestHandler)
    
    print("Server run",flush=True)
    
    http_server.serve_forever()
    
if __name__ == "__main__":
    main()