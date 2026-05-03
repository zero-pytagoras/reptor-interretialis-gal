import sys

url = input("Enter main url: ").strip()
if not url: sys.exit("Error: url cant be empty") # why exit if you need to re-run this ? why not loop ?

subdomains = ['test', 'beta', 'dev', 'staging', 'api']

subs = "\n".join([f"        server {s}.{url};" for s in subdomains])
hosts = "\n".join([f"      - '{s}.{url}:127.0.0.1'" for s in subdomains])

# why not use whole template and insert the values inside ?
conf = f"""events {{
    worker_connections 1024;
}}
http {{
    upstream backend {{
{subs}
    }}
    server {{
        listen 80;
        server_name {url};
        location / {{ proxy_pass http://backend; }}
    }}
}}"""

open("nginx.conf", "w").write(conf)
print("nginx.conf generated.")
# this was not requested
compose = f"""services:
  web:
    build: .
    ports:
      - "8080:80"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
    extra_hosts:
{hosts}
"""

open("docker-compose.yml", "w").write(compose)
print("docker-compose.yml generated")
