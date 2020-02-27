# Supervisor
Pip module that checks some running processes from a supervisor.json file in /etc/supervisor directory

### Installation guide
```
    You would need minimum python 2.7 to install this and generally pip 9+
    To install clone this repo and from the repo root run : `pip install -e .`
```

### Operations
To start watching processes, add the processes in the json key commands in listed format.
Then run the binary post install
```
For default supervisor.json location(/etc/supervisor/supervisor.json) run `supervisor`
To run in background run `nohup supervisor &`
Tail the logs : `tail -f /etc/supervisor/log/app.log`
For a custom supervisor json path run as : 
`supervisor -p | --jsonpath <path-to-supervisor.json>`
``` 