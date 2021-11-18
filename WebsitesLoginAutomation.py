from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import timeit
import sys

start = timeit.default_timer()
# ---------------------------------- Variable Initialization --------------------------------
codeField = "//div[@id='payx-wrap']/div[@id='appPlaceHolder']/div[@class='ng-scope']/div[@class='container ng-scope']/form[@class='form ng-pristine ng-invalid ng-invalid-required']/div[@class='row form-group']/div[@class='col-xs-4']/*[@name='otpCode']"
codeSubmitButton = "//div[@id='payx-wrap']/div[@id='appPlaceHolder']/div[@class='ng-scope']/div[@class='container ng-scope']/div[@class='row']"
passwordField = "//div[@id='payx-wrap']/div[@id='appPlaceHolder']/div[@class='ng-scope']/div[@class='container ng-scope']/div[@class='row']/div[@class='col-sm-8 col-sm-offset-4']/form[@class='ng-pristine ng-invalid ng-invalid-required']/div[@class='form-group']/div[@class='row'][2]/div[@class='col-sm-6'][1]/*[@name='PASSWORD']"
passwordSubmitButton = "//div[@id='payx-wrap']/div[@id='appPlaceHolder']/div[@class='ng-scope']/div[@class='container ng-scope']/div[@class='row']/div[@class='col-sm-8 col-sm-offset-4']/form[@class='ng-pristine ng-invalid ng-invalid-required']/div[@class='form-group']/div[@class='row'][2]/div[@class='col-sm-6'][2]/*[@type='submit']"

# these are the xpaths for the buttons that are pressed to clock in and to clock out

clockIn = "//html/body[@id='body']/payx-landing/main[@id='appContainer']/div[@id='main-content']/div[@id='subapp-container']/div[@class='angular-subapp-wrapper loaded']/div[@class='sub-app']/div[@class='full-height']/div/div[@class='custom-dashboard-app-container']/*[@id='app-dashboard-custom']/div[@class='cd-grid']/div[@class='custom-dash___grid muuri']/*[@class='cd-grid__item -w-sm muuri-item muuri-item-shown']/div[@class='cd-grid__item-content']/custom-dashboard-grid-item-content/div/div[@class='common-dashboard-tile viewport-small-hide']/png-card/div[@class='paychex-component png-card']/div[@class='png-card-collapse-target']/png-card-content/div/div[@class='progress-indicator-content']/time-punch/div[@class='pngreusableerror']/png-reusable-error[@id='punchwidgetreusableerror']/div[@class='png-error-container full-height']/div[@class='png-error-transclude full-height']/div[@class='punchwidget-png-progress-indicator']/div[@class='progress-indicator-content']/div[@class='wholebox']/div[@class='pw-button-container layout-row flex']/div[@class='pw-buttons default animated']/div[@class='pw-buttons-packaged']/div[@class='layout-row flex']/div[@class='pw-button-box flex']/div[@class='pw-button-padding']/div[@class='tooltip']/div"

# These options allow chromium to run better on the Raspberry pi
options = webdriver.ChromeOptions()
prefs = {'profile.managed_default_content_settings.images':2}
options.add_experimental_option("prefs", prefs)
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

# the string is the actual folder path to the chromium web driver on the disk
driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver', options=options)

#print("Connecting...")

#initializes the driver to be the landing page of the url
driver.get('https://myapps.paychex.com/landing_remote/html')

#print("Connected")

driver.switch_to.default_content()
time.sleep(1)
driver.switch_to.frame(0)


def clockOut():
    clock_out_button = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#punchwidgetreusableerror > div > div.png-error-transclude.full-height > div > div.progress-indicator-content > div.wholebox > div.pw-button-container.layout-row.flex > div:nth-child(1) > div > div > div:nth-child(1) > div > div > md-icon")))
    clock_out_button.click()
    time.sleep(1)
    driver.get_screenshot_as_file("clocked_out.png")
    print("In the clock out Function")


def clockIn():
    clock_out_button = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "")))
    clock_out_button.click()
    clock_out_button = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#punchwidgetreusableerror > div > div.png-error-transclude.full-height > div > div.progress-indicator-content > div.wholebox > div.pw-button-container.layout-row.flex > div:nth-child(1) > div > div > div:nth-child(1) > div > div > md-icon")))
    #time.sleep(1)
    driver.get_screenshot_as_file("clocked_in.png")
    print("In the clock in Function")
    #clock_in_button = driver.find_element_by_xpath("//html/body[@id='body']/payx-landing/main[@id='appContainer']/div[@id='main-content']/div[@id='subapp-container']/div[@class='angular-subapp-wrapper loaded']/div[@class='sub-app']/div[@class='full-height']/div/div[@class='custom-dashboard-app-container']/*[@id='app-dashboard-custom']/div[@class='cd-grid']/div[@class='custom-dash___grid muuri']/*[@class='cd-grid__item -w-sm muuri-item muuri-item-shown']/div[@class='cd-grid__item-content']/custom-dashboard-grid-item-content/div/div[@class='common-dashboard-tile viewport-small-hide']/png-card/div[@class='paychex-component png-card']/div[@class='png-card-collapse-target']/png-card-content/div/div[@class='progress-indicator-content']/time-punch/div[@class='pngreusableerror']/png-reusable-error[@id='punchwidgetreusableerror']/div[@class='png-error-container full-height']/div[@class='png-error-transclude full-height']/div[@class='punchwidget-png-progress-indicator']/div[@class='progress-indicator-content']/div[@class='wholebox']/div[@class='pw-button-container layout-row flex']/div[@class='pw-buttons default animated']/div[@class='pw-buttons-packaged']/div[@class='layout-row flex']/div[@class='pw-button-box flex']/div[@class='pw-button-padding']/div[@class='tooltip']/div")
    #clock_in_button.click()
    time.sleep(1)

def userCode(code):
    driver.switch_to.frame(0)
    code_field = driver.find_element_by_xpath(codeField)
    submit_button = driver.find_element_by_xpath(codeSubmitButton)
    code_field.send_keys(code)
    submit_button.click()
    time.sleep(3)

def userPassword(passwd):
    driver.switch_to.frame(0)

    passwd_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input.form-control.ng-pristine.ng-invalid.ng-invalid-required")))

    passwd_submit = driver.find_element_by_css_selector('#appPlaceHolder > div > div > div > div > form > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)')
    passwd_field.send_keys(passwd)
    
    passwd_submit.click()

def userLogin(username):
    username_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#USER")))
    submit_button = driver.find_element_by_css_selector('#usernameForm > div > div:nth-child(2) > div:nth-child(3) > button')

    username_field.send_keys(username)
    
    submit_button.click()
    #print("button clicked")

def userSecurityQuestion():
    question_1 = "What color was the interior of your first car?"
    question_2 = "What was the last name of your first grade teacher?"
    question_3 = "What color was your first car?"
    question_4 = "What model was your first car?"

    frame = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login")))
    driver.switch_to.frame(frame)
    
    #print("before")
    continue_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#appPlaceHolder > div.ng-scope > div > div.row > div > div > button:nth-child(2)")))
    continue_button.click()
    #print("after")
    driver.switch_to.default_content()
    time.sleep(1)
    frame = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login")))
    driver.switch_to.frame(frame)

    input_value = driver.find_element_by_css_selector('#appPlaceHolder > div.ng-scope > div > form > div:nth-child(1) > div > div:nth-child(1) > div > label')
    question_asked = input_value.text
    form = driver.find_element_by_css_selector('#answer')
    #print("The value is: ", question_asked)
    if question_asked == question_1:
        answer = "ANSWER1"
        form.send_keys(answer)
    elif question_asked == question_2:
        answer = "ANSWER2"
        form.send_keys(answer)
    elif question_asked == question_3:
        answer = "ANSWER3"
        form.send_keys(answer)
    elif question_asked == question_4:
        answer = "ANSWER4"
        form.send_keys(answer)

    security_submit = driver.find_element_by_css_selector('#appPlaceHolder > div.ng-scope > div > form > div:nth-child(2) > div > div > button:nth-child(2)')
    security_submit.click()


def signIn(username, passwd):
    #print("Argument is: ", sys.argv[1])
    userLogin(username)
    driver.switch_to.default_content()
    userSecurityQuestion()
    time.sleep(1)
    
    driver.switch_to.default_content()
    userPassword(passwd)
    driver.switch_to.default_content()
    
    time.sleep(1)
    
    driver.get_screenshot_as_file("We_are_in_bois.png")
    #print("done waiting")
    
    if sys.argv[1] == "in":
        #print("You selected in")
        clockIn()
    elif sys.argv[1] == "out":
        #print("You selected out")
        clockOut()

signIn("USERNAME", "PASSWORD")

#print("success!")
stop = timeit.default_timer()
print('Time: ', stop - start)
driver.quit()

if __name__ == '__signIn__':
    signIn()
