import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

HAUTS_DE_SEINE_GOUV_FR = "http://www.hauts-de-seine.gouv.fr/booking/create/4462/2"


def selenium_naturalisation():
    browser = webdriver.Chrome()

    send_notification = False
    while (not send_notification):  # TODO add timer
        browser.get(HAUTS_DE_SEINE_GOUV_FR)

        # issue with chrome driver, need to scroll manualy to the location
        position = browser.find_element_by_id("condition").location
        browser.execute_script("window.scrollTo(" + str(position['x']) + ", " + str(position['y']) + ")")
        # click on check box to accept condition
        browser.find_element_by_id("condition").click()

        # click on next
        browser.find_element_by_name("nextButton").click()

        # check if that there are no booking date
        try:
            form = browser.find_element_by_id("FormBookingCreate")
            if not form or "Veuillez recommencer" not in form.text:
                # no form? or not the annoying message? send notification
                send_notification = True
            else:
                # retry in 1 second
                time.sleep(1)
        except NoSuchElementException:
            # the element does not exist? notify
            send_notification = True


if __name__ == '__main__':
    selenium_naturalisation()
