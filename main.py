from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
from selenium.webdriver.support.wait import WebDriverWait

CHROMEDRIVER_PATH = r"C:\Users\DGP-Yoga1\PycharmProjects\chromedriver.exe"
FORM_URL = "https://forms.gle/digRZNGwKGnFUaAGA"
NAME = "Marcus Lam"
NUMBER = "98765432"
text = "1.05pm - 3.55pm"


def main():
    print("Script started running successfully.")
    print("Setting up selenium options...")
    # set up selenium functions
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    # run chrome driver
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=option)
    # open URL of form
    browser.get(FORM_URL)
    # find name and number text inputs
    name = browser.find_elements_by_class_name('quantumWizTextinputPaperinputInput')
    # key in name and number accordingly
    name[0].send_keys(NAME)
    name[1].send_keys(NUMBER)

    # Click on the dropdown box
    selectBox = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//div[@role='listbox']")))
    action = ActionChains(browser);
    action.move_to_element(selectBox).perform()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='listbox']")))
    selectBox.click()
    # Click on the option
    selectionXpath = "//div[@class='exportSelectPopup quantumWizMenuPaperselectPopup appsMaterialWizMenuPaperselectPopup']//span[@class='quantumWizMenuPaperselectContent exportContent' and text()='1.05pm - 3.55pm']"
    selection = WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, selectionXpath)))
    selection.click()
    # Click on first timer option
    firstTimeXpath = "//div[@class='appsMaterialWizToggleRadiogroupEl exportToggleEl'][@data-value='No']"
    firstTime = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, firstTimeXpath)))
    action.move_to_element(firstTime).perform()
    firstTime.click()
    # Click on entry pass type
    entryPassXpath = "//div[@class='appsMaterialWizToggleRadiogroupEl exportToggleEl'][@data-value='Multi-pass']"
    entryPass = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, entryPassXpath)))
    action.move_to_element(entryPass).perform()
    entryPass.click()
    # go through all checkboxes and click them accordingly
    checkBox1Xpath = "//span[@class='docssharedWizToggleLabeledLabelText exportLabel freebirdFormviewerComponentsQuestionCheckboxLabel']"
    checkBox1 = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located((By.XPATH, checkBox1Xpath)))
    for element in checkBox1:
        action.move_to_element(element).perform()
        element.click()
        time.sleep(0.5)

    # Find and click on the submit button
    submitXpath = "//span[contains(text(), 'Submit')]"
    submitButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, submitXpath)))
    action.move_to_element(submitButton).perform()
    submitButton.click()
    time.sleep(10)


if __name__ == '__main__':
    main()

