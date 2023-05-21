<br/>
<p align="center">
  <h3 align="center">Real-time Simple Web Checker
</h3>

  <p align="center">
    <a href="https://github.com/BattalFaikAktas/Real-time-Simple-Web-Checker/issues">Report Bug</a>
    .
    <a href="https://github.com/BattalFaikAktas/Real-time-Simple-Web-Checker/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/BattalFaikAktas/Real-time-Simple-Web-Checker?color=dark-green) ![Forks](https://img.shields.io/github/forks/BattalFaikAktas/Real-time-Simple-Web-Checker?style=social) ![Stargazers](https://img.shields.io/github/stars/BattalFaikAktas/Real-time-Simple-Web-Checker?style=social) ![Issues](https://img.shields.io/github/issues/BattalFaikAktas/Real-time-Simple-Web-Checker) ![License](https://img.shields.io/github/license/BattalFaikAktas/Real-time-Simple-Web-Checker) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [License](#license)
* [Authors](#authors)

## About The Project

This script is designed to monitor the status of specified websites and send notifications when a website goes down. It periodically checks the websites and provides real-time information about their status, request rate, and uptime percentage.

## Getting Started

1. Open the `sites` list in the script file.
2. Add the websites you want to monitor along with their names and URLs. For example:
```python
   sites = [
       {"name": "Site A", "url": "https://sitea.com"},
       {"name": "Site B", "url": "http://siteb.com"}
   ]
```
3. Set the `WEBHOOK_URL` variable to the Discord webhook URL where you want to receive notifications. For example:
```python
WEBHOOK_URL = "https://discord.com/api/webhooks/your-webhook-url"
```
### Installation

To install the required dependencies, you can use the following command:
```bash
pip3 install -r requirements.txt
```
or 

[colorama](https://pypi.org/project/colorama/): `pip3 install colorama`

[prettytable](https://pypi.org/project/prettytable/): `pip3 install prettytable`

[requests](https://pypi.org/project/requests/): `pip3 install requests`

## Usage

To run the script, execute the following command in your terminal or command prompt:
```bash
python3 realtime_web_checker.py
```

## License

Distributed under the MIT License. See [LICENSE](https://github.com/BattalFaikAktas/Real-time-Simple-Web-Checker/blob/main/LICENSE) for more information.

## Authors

* **Battal Faik Aktaş** - *Cyber Security Researcher* - [Battal Faik Aktaş](https://github.com/BattalFaikAktas)

