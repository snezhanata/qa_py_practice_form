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
    browser.element('.react-datepicker__year-select').element('[value="2000"]').click()
    browser.element('.react-datepicker__month-select').element('[value="7"]').click()
    browser.element('.react-datepicker__day--008').click()
    # we can set value in Calendar also just using: browser.element('#dateOfBirthInput').type('01 Sep 2001')
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(abs_path_from_project_root('resources/pic.jpg'))
    browser.element('#currentAddress').type('https://www.youtube.com/watch?v=QH2-TGUlwu4')
    browser.element('#state').perform(command.js.click)
    browser.element('#react-select-3-input').type('Uttar Pradesh').press_enter()
    browser.element('#city').perform(command.js.click)
    browser.element('#react-select-4-input').type('Agra').press_enter()
    browser.element('#submit').press_enter()

    # Checking Results
    browser.all('table tr')[1].all('td')[1].should(have.exact_text('Nyan Cat'))
    browser.all('table tr')[2].all('td')[1].should(have.exact_text('nyan.cat@mail.com'))
    browser.all('table tr')[3].all('td')[1].should(have.exact_text('Female'))
    browser.all('table tr')[4].all('td')[1].should(have.exact_text('0123401234'))
    browser.all('table tr')[5].all('td')[1].should(have.exact_text('08 August,2000'))
    browser.all('table tr')[6].all('td')[1].should(have.exact_text('Maths'))
    browser.all('table tr')[7].all('td')[1].should(have.exact_text('Sports'))
    browser.all('table tr')[8].all('td')[1].should(have.exact_text('pic.jpg'))
    browser.all('table tr')[9].all('td')[1].should(have.exact_text('https://www.youtube.com/watch?v=QH2-TGUlwu4'))
    browser.all('table tr')[10].all('td')[1].should(have.exact_text('Uttar Pradesh Agra'))

    # way_2
    # browser.all('.table-responsive').should(have.exact_texts(
    #     'Label Values\nStudent Name Nyan Cat\nStudent Email nyan.cat@mail.com\nGender Female\nMobile 0123401234\nDate of Birth 08 August,2000\nSubjects Maths\nHobbies Sports\nPicture pic.jpg\nAddress https://www.youtube.com/watch?v=QH2-TGUlwu4\nState and City Uttar Pradesh Agra'
    # ))

    # way_3
    # browser.all(".modal-body td:nth-child(even)").should(have.texts(
    #     # 'Label Values\nStudent Name Nyan Cat\nStudent Email nyan.cat@mail.com\nGender Female\nMobile 0123401234\nDate of Birth 08 August,2000\nSubjects Maths\nHobbies Sports\nPicture pic.jpg\nAddress https://www.youtube.com/watch?v=QH2-TGUlwu4\nState and City Uttar Pradesh Agra'
    #     'Nyan Cat',
    #     'nyan.cat@mail.com',
    #     'Female',
    #     '0123401234',
    #     '08 August,2000',
    #     'Maths',
    #     'Sports',
    #     'pic.jpg',
    #     'https://www.youtube.com/watch?v=QH2-TGUlwu4',
    #     'Uttar Pradesh Agra'
    # ))
