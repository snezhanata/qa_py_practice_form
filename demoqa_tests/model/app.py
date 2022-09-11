from selene import have, command
from selene.support.shared import browser


def given_opened_practice_form():
    """
    this function opens practice-form and removes advertisement banner if it appears
    """
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')
    ads = browser.all('[id^=google_ads_][id$=container__]')
    if ads.wait.until(have.size_less_than_or_equal(3)):
        ads.perform(command.js.remove)