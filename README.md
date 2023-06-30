![built with Python3](https://img.shields.io/badge/built%20with-Python3-red.svg)
![built with Selenium](https://img.shields.io/badge/built%20with-Selenium-yellow.svg)

# LinkedIn Automation Tool

This tool is designed for automating tasks on LinkedIn. It leverages technologies such as Scrapy, Selenium WebDriver, Chromium (in headless mode), Docker, and Python3.

### Sponsor:

[![Proxycurl APIs enrich people and company profiles with structured data](https://github.com/josephlimtech/linkedin/blob/master/Proxycurl%20logo.png?raw=true)](https://bit.ly/proxycurl-api)

Scrape public LinkedIn people and company profile data at scale with [Proxycurl APIs](https://bit.ly/proxycurl-api).

- Scraping Public profiles are battle tested in court in HiQ VS LinkedIn case
- GDPR, CCPA, SOC2 compliant
- High rate limit - 300 requests/minute
- Fast - APIs respond in ~2s
- Fresh data - 88% of data is scraped real-time, other 12% are not older than 29 days
- High accuracy
- Tons of data points returned per profile

Built for developers, by developers.

## Features

### LinkedIn Spider

The LinkedIn Spider is designed to visit as many LinkedIn user pages as possible. The goal is to increase the visibility of your account, as LinkedIn notifies users when their profile has been viewed.

### Companies Spider

The Companies Spider is designed to gather information about all users working for a specific company on LinkedIn. It operates by:

1. Navigating to the company's LinkedIn page.
2. Clicking on the "See all employees" button.
3. Collecting user-related data.

## Installation and Setup

You will need the following:

- Docker
- Docker Compose
- A VNC viewer (e.g., Vinagre for Ubuntu)
- Python 3.6
- Virtualenv

### Steps

1. **Prepare your environment**: Install Docker from the [official website](https://www.docker.com/). If you don't have a VNC viewer, install one. For Ubuntu, you can use Vinagre:

```bash
sudo apt-get update
sudo apt-get install vinagre
```

2. **Set up LinkedIn login and password**: Copy `conf_template.py` to `conf.py` and fill in your LinkedIn credentials.

3. **Run and build containers with Docker Compose**: This step only applies to the LinkedIn random spider, not the companies spider. Open your terminal, navigate to the project folder, and type:

```bash
make up
```

4. **Monitor the browser's activity**: Open Vinagre and connect to `localhost:5900`. The password is `secret`. Alternatively, you can use the command:

```bash
make view
```

5. **Stop the scraper**: To stop the scraper, use the command:

```bash
make down
```

## Testing and Development

Set up your Python virtual environment:

```bash
virtualenvs -p python3.6 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

To create the Selenium server, open the VNC window, and launch the tests, type the following in three different terminals in the project folder:

```bash
make dev
make view
make tests
```

For more details, refer to the Makefile. Here are some commands you can use for development:

```bash
scrapy crawl companies -a selenium_hostname=localhost -o output.csv
scrapy crawl random -a selenium_hostname=localhost -o output.csv
scrapy crawl byname -a selenium_hostname=localhost -o output.csv
```

## Legal Disclaimer

This code is not affiliated with, authorized, maintained, sponsored, or endorsed by LinkedIn or any of its affiliates or subsidiaries. This is an independent and unofficial project. Use at your own risk.

This project violates LinkedIn's User Agreement Section 8.2. As a result, LinkedIn may temporarily or permanently ban your account. We are not responsible for any actions taken by LinkedIn in response to the use of this tool.

---