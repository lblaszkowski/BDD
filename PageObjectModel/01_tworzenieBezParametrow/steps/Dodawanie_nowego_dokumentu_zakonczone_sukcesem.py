# coding=utf-8
from behave import *
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


@given('Uzytkownik ma uruchomiony program')
def step_impl(context):
    driver = webdriver.Chrome(executable_path=r'../Drivers/ChromeDrive_0_89/chromedriver.exe')
    driver.get("https://www.reqview.com/apps/desktop/ReqViewDesktop.html")
    driver.maximize_window()
    driver.implicitly_wait(50)
    driver.find_element_by_id("dijit_form_Button_20_label").click()
    driver.find_element_by_id("dijit_form_Button_21_label").click()
    driver.find_element_by_id("dijit_form_ValidationTextBox_0").send_keys("wsb")
    driver.find_element_by_id("dijit_form_ValidationTextBox_1").send_keys("wsb@wp.pl")
    cmpany = driver.find_element_by_id("dijit_form_TextBox_2")
    cmpany.click()
    cmpany.send_keys("asas")
    driver.find_element_by_id("dijit_form_Button_21").click()
    driver.implicitly_wait(80)
    context.driver = driver


@given('Tworzy nowy dokument')
def step_impl(context):
    driver = context.driver
    driver.find_element_by_xpath("//*[@id='welcomeDialog']/div[1]/span[2]").click()
    driver.find_element_by_id("projectMenuBarPopup").click()
    driver.find_element_by_xpath("//td[contains(.,'Create Project…')]").click()


@when('Uzytkownik wprowadza ProjektID i DocumentID oraz Document name')
def step_impl(context):
    driver = context.driver
    ProjektID = driver.find_element_by_id("dijit_form_ValidationTextBox_2")
    ProjektID.click()
    ProjektID.clear()
    ProjektID.send_keys("01")
    DocumentID = driver.find_element_by_id("dijit_form_ValidationTextBox_3")
    DocumentID.click()
    DocumentID.clear()
    DocumentID.send_keys("Test")
    DocumentNname = driver.find_element_by_id("dijit_form_TextBox_3")
    DocumentNname.click()
    DocumentNname.clear()
    DocumentNname.send_keys("test_wsb12")

@when('Zapisuje projekt')
def step_impl(context):
    driver = context.driver
    savenProjekt = driver.find_element_by_id("dijit_form_Button_24")
    savenProjekt.click()


@then('Uzytkownik widzi  stworzony dokument o nazwie Nazwa')
def step_impl(context):
    driver = context.driver
    time.sleep(5)
    print(driver.find_element_by_id('titleBar').text)
    assert driver.find_element_by_id('titleBar').text == "01-Test:"





