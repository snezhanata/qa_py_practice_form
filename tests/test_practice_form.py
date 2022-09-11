from selene import have, command
from selene.support.shared import browser
from demoqa_tests.model import app
from demoqa_tests.utils.files import abs_path_from_project_root


def test_submit_student_registration_form():
    """
    This test checks the submission of the "Student Registration Form"
    """
    app.given_opened_practice_form()
    browser.should(have.title('ToolsQA'))
    browser.element('#firstName').type('Nyan')
    browser.element('#lastName').type('Cat')
    browser.element('#userEmail').type('nyan.cat@mail.com')
    browser.element('#gender-radio-2').double_click()
    browser.element('#userNumber').type('0123401234')
    browser.element('#dateOfBirthInput').click()
    browser.element('[value="7"]').click()  # Calendar: Month
    browser.element('[value="2000"]').click()  # Calendar: Year
    browser.element('[aria-label="Choose Tuesday, August 8th, 2000"]').click()  # Calendar: Day
    # we can set value in Calendar also just using: browser.element('#dateOfBirthInput').type('01 Sep 2001')
    browser.element('#subjectsInput').type('Maths').press_enter().click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(abs_path_from_project_root('resources/pic.jpg'))
    browser.element('#currentAddress').type('https://www.youtube.com/watch?v=QH2-TGUlwu4')
    browser.element('#state').perform(command.js.click)
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#city').perform(command.js.click)
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()

    browser.all('.table-responsive').should(have.texts(
        'Label Values\nStudent Name Nyan Cat\nStudent Email nyan.cat@mail.com\nGender Female\nMobile 0123401234\nDate of Birth 08 August,2000\nSubjects Maths\nHobbies Sports\nPicture pic.jpg\nAddress https://www.youtube.com/watch?v=QH2-TGUlwu4\nState and City Uttar Pradesh Agra'
    ))