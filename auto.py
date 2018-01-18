# coding=utf-8

import os, sys
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException

browser = webdriver.Ie()


def sleep(sleep_time_second):
    time.sleep(sleep_time_second)


def open_course_select_page():
    browser.get('http://grdms.bit.edu.cn')
    # login
    elem = browser.find_element_by_xpath('/html/body/form[1]/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[1]/td/a')
    elem.click()

    # print browser.current_url
    # not logged in: https://login.bit.edu.cn/cas/login?service=http%3A%2F%2Fgrdms.bit.edu.cn%2Fyjs%2Flogin_cas.jsp
    # logged in: http://grdms.bit.edu.cn/yjs/application/main.jsp

    sleep(1)

    # 主页 点击“培养管理”
    browser.switch_to.frame('system_iframeMain')
    elem = browser.find_element_by_id('subsystab_href_3')
    elem.click()

    sleep(1)

    # “培养管理”页面 点击“学生选课”
    elem = browser.find_element_by_id('402880d21a75d1be011a75d6691f0003')
    elem.click()

    sleep(1)

    # 选课界面的“关闭”按钮
    browser.switch_to.frame('mainFrame')
    browser.switch_to.frame('stdSelectCourseNoteFrame')
    elem = browser.find_element_by_xpath('/html/body/div[2]/input')
    elem.click()
    browser.switch_to.parent_frame()  # back to mainFrame

    sleep(1)

    # 课程列表
    elem = browser.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/form/table/tbody[2]')
    # or: elem = browser.find_element_by_id('courselist4Select')


# index: 从1开始，和网页上的序号一样
def show_single_course_info(index, function_select_course, function_unselect_course):
    # elem = browser.find_element_by_xpath('/html/body/table/tbody/tr[5]/td/form/table/tbody[2]/tr[{}]'.format(index))
    # content = elem.text
    # 选课/退课按钮
    elem = browser.find_element_by_xpath(
        '/html/body/table/tbody/tr[5]/td/form/table/tbody[2]/tr[{}]/td[13]/input[10]'.format(index))
    btn_class = elem.get_attribute('class')  # class implies state
    if btn_class == 'select-course':    # 选课按钮
        if function_select_course is not None:
            function_select_course(index, elem)
    elif btn_class == 'unselect-course':    # 退课按钮
        if function_unselect_course is not None:
            function_unselect_course(index, elem)


# 选课
def function_select_course(index, select_btn):
    # 获取表格一行中的某一列，col_index从1开始
    def get_column(col_index):
        elem_column = browser.find_element_by_xpath(
            '/html/body/table/tbody/tr[5]/td/form/table/tbody[2]/tr[{}]/td[{}]'.format(index, col_index))
        return elem_column.text

    btn_class = select_btn.get_attribute('class')
    assert btn_class == 'select-course'
    # 课程代码，课程中文名称，教学班名称
    course_id, course_name, class_name = get_column(2), get_column(3), get_column(4)
    print course_id, course_name, class_name
    # 矩阵分析
    if course_id == '1700002' and class_name == '2':
        print u'选课', u'课程代码：{}, 课程名称：{}，教学班：{}'.format(course_id, course_name, class_name)
        select_btn.click()
        try:
            # 等待确认对话框出现，最多等5秒
            WebDriverWait(browser, 5).until(EC.alert_is_present(), 'wait for alert timeout...')
            alert = browser.switch_to.alert
            print 'alert content:', alert.text
            alert.accept()
            print 'alert accepted'
        except TimeoutException:
            print 'alert timeout'


# 退课
def function_unselect_course(index, unselect_btn):
    btn_class = unselect_btn.get_attribute('class')  # class implies state
    assert btn_class == 'unselect-course'


# 遍历表格的所有行
def show_all_course_info():
    i = 1
    while (True):
        try:
            show_single_course_info(i, function_select_course, function_unselect_course)
            i += 1
        except NoSuchElementException:
            break
    print '{} course shown'.format(i - 1)


def main():
    open_course_select_page()
    show_all_course_info()
    # while True:
    #    show_single_course_info(14, function_select_course, None)


if __name__ == '__main__':
    main()
