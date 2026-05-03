# Reptor-Interretialis

A DevOps class task.

The Python script dynamically generates an Nginx configuration file and a Docker Compose environment. It configures Nginx to route incoming traffic to popular upstream subdomains (test, beta, dev, staging, api) based on a user provided main URL.


## How to Run

1. Run, enter the URL and Generate the configuration files:

```bash
python3 setup.py
```

2. Build the image and start the container:

```bash
docker-compose up -d --build # this will not work if you did not run the script first -> logical error...
```
>>> you either provide the whole project in full or  provide single script that wraps it all. everything in between makes you look unprofessional.
