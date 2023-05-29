# Welcome to SEE ALL

This is a small script to monitor your Services EASILY.

> This will need ip and port to monitor the service

>Update available.
>1. ipv4 and ipv6 both supported
>2. tcp and udp supported

## To install all the things here are the steps

Download the zip of this project or clone using the command
```
git clone git@github.com:melgiritechnology/see-all.git
```

>To install requirements (if you want discord notification) run
>
>```
>pip install -r requirements.txt
>```

Go to `config.json` to config.

If you want discord notification when service is Inactive do the following things.

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

> Whenever you run the python script note that it will run constantly and show the status of the services in the console. If you stop it, it will not work. It is recommended to run it in background. Also if you put intervel to very low number it may harm your system and services.

### Thank you for using SEE ALL