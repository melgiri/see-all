# Welcome to SEE ALL

This is a small script to monitor your Services EASILY.

> This will need ip and port to monitor the service

## To install all the things here are the steps

Download the zip of this project or clone using the command
```
git clone git@github.com:melgiritechnology/see-all.git
```

> `socket`, `threading`, `requests` are the python packages you need to install if you dont have. You can install using these commands

```
pip install socket
pip install threading
pip install requests
```

Go to `config.json` to config.

If you want discord webhook notification when service is Inactive do the following things.

> Remember, it will keep messaging you if the service is off until you remove the details of that service.

To get discord notification change the code from this

```
"discord" : "True / False",
```
to this

```
"discord" : "True",
```

Also fill your discord user id and webhook url.

`intervel` in the config file is the time which tells the script to check if all the services are up or not.

To setup services follow the patterns followed in the `data.json` file.

> Note: You can use normal ipv4. It also works with domain names.

### Thank you for using SEE ALL