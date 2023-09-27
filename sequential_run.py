import logging
import time

from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import defer, reactor

from linkedin.integrations.selenium import build_driver, is_security_check
from linkedin.spiders.companies import CompaniesSpider

file_name = f"data/companies/data.csv"


@defer.inlineCallbacks
def run_spiders_sequentially(runner, urls, driver):
    for url in urls:
        yield runner.crawl(CompaniesSpider, start_url=url, driver=driver)
    yield driver.close()


if __name__ == "__main__":
    driver = build_driver(login=True)
    if is_security_check(driver):
        # Define the number of seconds for the security check
        SECURITY_CHECK_DURATION = 30

        # Print instructions with fancy characters for user attention
        logging.info("***** SECURITY CHECK IN PROGRESS *****")
        logging.info(
            f"Please perform the security check on selenium, you have {SECURITY_CHECK_DURATION} seconds..."
        )

        for _ in range(SECURITY_CHECK_DURATION):
            time.sleep(1)

        logging.info("***** SECURITY CHECK COMPLETED *****")

        # Erase the past content of the file
        open(file_name, "w").close()

        settings = get_project_settings()
        settings.set("FEEDS", {file_name: {"format": "csv"}})

        runner = CrawlerRunner(settings)
        urls = [url.strip() for url in open("data/companies.txt", "r")]

        # Run the spiders sequentially
        sequential_spiders = run_spiders_sequentially(runner, urls, driver)
        sequential_spiders.addBoth(
            lambda _: reactor.stop()
        )  # Stop the reactor when all spiders are done
        reactor.run()  # Start the reactor
