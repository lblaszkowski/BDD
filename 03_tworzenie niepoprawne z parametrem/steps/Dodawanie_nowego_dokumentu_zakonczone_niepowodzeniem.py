# coding=utf-8
from behave import *
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

site_root_url = "https://www.reqview.com/apps/desktop/ReqViewDesktop.html";
###zmiana parametrów w pliku py i feature




@given('Uzytkownik ma uruchomiony program')
def step_impl(context):
    driver = webdriver.Chrome();
    driver.get(site_root_url);
    driver.implicitly_wait(50)

    driver.find_element_by_xpath("//i[@class='icon-ok']").click();
    driver.find_element_by_id("dijit_form_Button_21_label").click();
    driver.find_element_by_id("dijit_form_ValidationTextBox_0").send_keys("wsb");
    driver.find_element_by_id("dijit_form_ValidationTextBox_1").send_keys("wsb@wp.pl");
    driver.find_element_by_id("dijit_form_TextBox_1").send_keys("asas");
    driver.find_element_by_xpath("//i[@class='icon-ok']").click()
    driver.implicitly_wait(80);
    context.driver = driver

@given('Tworzy nowy dokument')
def step_impl(context):
    driver = context.driver
    driver.find_element_by_class_name("hopscotch-bubble-close").click();
    driver.find_element_by_id("projectMenuBarPopup").click();
    driver.find_element_by_xpath("//td[contains(.,'New Project...')]").click();

@when('Uzytkownik wprowadza {project_id} i {document_id} oraz {document_name}')
def step_impl(context, project_id, document_id, document_name):
    driver = context.driver
    driver.find_element_by_id("dijit_form_ValidationTextBox_2").send_keys(project_id);
    driver.find_element_by_id("dijit_form_ValidationTextBox_3").send_keys(document_id);
    driver.find_element_by_id("dijit_form_TextBox_6").send_keys(document_name);

@when('Zapisuje projekt')
def step_impl(context):
    driver = context.driver
    driver.find_element_by_id("dijit_form_Button_32_label").click();


@then('Uzytkownik widzi  stworzony dokument o nazwie {NazwaDokumentu}')
def step_impl(context, NazwaDokumentu):
    driver = context.driver
    time.sleep(5)
    print(driver.find_element_by_id('titleBar').text)
    assert driver.find_element_by_id('titleBar').text == NazwaDokumentu

