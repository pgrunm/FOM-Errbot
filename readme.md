# Errbot for Example purposes

## Setting up the bot

- Create a virtual environment in Python like this:

```shell
python -m virtualenv .venv
./venv/Scripts/Activate.sh
pip3 installl errbot
```

- Run the command `errbot --init`.
- Enter the bot with the command `errbot`.

## Adding the Telegram Backend

- Install the require Python package with `pip install python-telegram-bot`.
- Follow the tutorial as described [here](https://errbot.readthedocs.io/en/latest/user_guide/configuration/telegram.html)

## Interesting plugins

- [Gitbot](https://github.com/errbotio/err-gitbot)
- [Jenkins Plugin](https://github.com/ESSS/err-jenkins)
- [ChatOps Plugin](https://github.com/andrewthetechie/errbot-chatopsanything)
- [Prometheus Alertmanager](https://github.com/Voronenko/errbot-prometheus-alertmanager) (see [here](https://prometheus.io/docs/alerting/alertmanager/) for information on the Prometheus Alertmanager)

## Plugin Development

- [General overview](https://errbot.readthedocs.io/en/latest/user_guide/plugin_development/index.html)
