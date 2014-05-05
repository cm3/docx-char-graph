
# python webbrowser.open(url) - Stack Overflow http://stackoverflow.com/questions/2634235/python-webbrowser-openurl

import http.server
import threading
import webbrowser

port = 8000
    
def start_browser(server_ready_event, url):
    print("[Browser Thread] Waiting for server to start")
    server_ready_event.wait()
    print("[Browser Thread] Opening browser")
    webbrowser.open(url)

url = 'http://localhost:'+str(port)+'/'
server_ready = threading.Event()
browser_thread = threading.Thread(target=start_browser, args=(server_ready, url))
browser_thread.start()

print("[Main Thread] Starting server")
httpd = http.server.HTTPServer(('', port), http.server.SimpleHTTPRequestHandler)
print("[Main Thread] Server started")
server_ready.set()

httpd.serve_forever()
browser_thread.join()