#coding=utf-8

import os, sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


browser = webdriver.Ie()


def open_course_select_page():
    browser.get('http://grdms.bit.edu.cn')
    # login
    elem = browser.find_element_by_xpath('/html/body/form[1]/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[1]/td/a')
    elem.click()

    # 主页 点击“培养管理”
    browser.switch_to.frame('system_iframeMain')
    elem = browser.find_element_by_id('subsystab_href_3')
    elem.click()

    # “培养管理”页面 点击“学生选课”
    elem = browser.find_element_by_id('402880d21a75d1be011a75d6691f0003')
    elem.click()

    # 选课界面的“关闭”按钮
    browser.switch_to.frame('mainFrame')
    browser.switch_to.frame('stdSelectCourseNoteFrame')
    elem = browser.find_element_by_xpath('/html/body/div[2]/input')
    elem.click()
    browser.switch_to.parent_frame() # back to mainFrame

    # 课程列表
    elem = browser.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/form/table/tbody[2]')
    #or: elem = browser.find_element_by_id('courselist4Select')


def show_course_info():
    i = 1
    while(True):
        try:
            elem = browser.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/form/table/tbody[2]/tr[{}]'.format(i))
            content = elem.text
            elem = browser.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/form/table/tbody[2]/tr[{}]/td[13]/input[10]'.format(i))
            btn_class = elem.get_attribute('class')   # class implies state
            if btn_class == 'select-course':
                print u'该课程未选'
                # elem.click()
                # alert = browser.switch_to.alert
                # print alert.text
                # alert.accept()
            elif btn_class == 'unselect-course':
                print u'该课程已选'
                # elem.click()  # select or unselect course
            i += 1
        except:
            break


def main():
    open_course_select_page()
    show_course_info()
    
if __name__ == '__main__':
    main()

