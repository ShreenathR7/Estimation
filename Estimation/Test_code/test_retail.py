# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from pynput.keyboard import Key,Controller
from time import sleep
from Test_locators import locators
from Test_data import data
import pytest


class Test_Logimax:
    @pytest.fixture
    

    def booting_function(self):
       self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
       self.driver.get(data.Logi_Data().url)
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)
  
    
   
    def test_Estimation(self,booting_function):   
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().username_inputBox).send_keys(data.Logi_Data().username)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().password_inputBox).send_keys(data.Logi_Data().password)
        sleep(8)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().signButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().side_bar).click()
        sleep(8)
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value=locators.Logi_Locators().Estimation).click()
        sleep(15)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Add_Estimation).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Branch).click()
        sleep(5)
        branch = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        branch.send_keys('Head OFFICE')
        branch.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Sales_Employee).click()
        sleep(5)
        employee = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        employee.send_keys('111-Logimax Developer')
        employee.send_keys(Keys.RETURN) 
        sleep(5)
        customer = self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Customer)
        sleep(10)
        customer.send_keys('KANNAN')
        sleep(5)
        customer.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']//li")
        print('Total',len(se_ver))
        customer_name = 'KANNAN -8989854215'
        for element in se_ver:
            if element.text == customer_name:
                element.click()
                break
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Close).click()    
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().tag_checkbox).click()
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Tag_scan).send_keys(data.Logi_Data().tag_scan_code)
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().search).click()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wastage_per).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wastage_per).send_keys(data.Logi_Data().wastage_value)    
        sleep(5)
        MC = Select (self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().MC_Type))
        MC.select_by_value('2')
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation tagged item seleced successfully,   Branch : {a}, Sales_Employee : {b}, custumer : {c}, Tag_scan : {d}, wastage_per : {e}  ".format(a='Head OFFICE', b='111-Logimax Developer', c=customer_name, d = data.Logi_Data().tag_scan_code, e = data.Logi_Data().wastage_value))
        
        
        
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().Non_tag).click()      
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().section).click()
        sleep(5)
        section = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        section.send_keys('GOLD CHAIN')
        section.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Product).click()
        sleep(5)
        product = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        product.send_keys('NON TAG PRODUCT')
        product.send_keys(Keys.RETURN) 
       
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().design).click()
        sleep(5)
        design = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        design.send_keys('MACHINE MADE')
        design.send_keys(Keys.RETURN) 
        sleep(5)
      
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Sub_design).click()
        sleep(5)
        sub_design = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        sub_design.send_keys('HOLLOW ROPE')
        sub_design.send_keys(Keys.RETURN) 
        sleep(5)
        purity_value = Select (self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().purity))
        purity_value.select_by_value('10')
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().size).send_keys(data.Logi_Data().size_No)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().pcs).send_keys(data.Logi_Data().No_of_pcs)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().G_wt).send_keys(data.Logi_Data().G_wt_value)
        sleep(5)
        non_mc = Select (self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Non_mc_type))
        non_mc.select_by_value('2')
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().mc_value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().mc_value).send_keys(data.Logi_Data().non_mc_value)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wastage_percentage).clear() 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().wastage_percentage).send_keys(data.Logi_Data().non_wastage_per)
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation Non tagged item seleced successfully,    section : {a}, Product : {b}, design : {c}, Sub_design : {d}, size : {e}, pcs : {f}, G_wt : {g}, mc_value : {h},wastage_percentage : {i}    ".format(a='GOLD CHAIN', b='NON TAG PRODUCT', c='MACHINE MADE', d = 'HOLLOW ROPE', e =data.Logi_Data().size_No, f = data.Logi_Data().No_of_pcs, g = data.Logi_Data().G_wt_value, h = data.Logi_Data().non_mc_value, i = data.Logi_Data().non_wastage_per ))
        
        
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().home_bill_checkbox).click()
        sleep(5)
        Tag = self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().Tag)
        sleep(10)
        Tag.send_keys('GCG-00')
        sleep(5)
        Tag.send_keys(Keys.BACK_SPACE)
        sleep(10)
        se_ver = self.driver.find_elements(By.XPATH, "//ul[@id='ui-id-5']//li")
        print('Total',len(se_ver))
        tags = 'GCG-00001'
        for element in se_ver:
            if element.text == tags:
                element.click()
                break  
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().home_section).click()
        sleep(6)
        home_section = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        home_section.send_keys('GOLD CHAIN')
        home_section.send_keys(Keys.RETURN) 
        sleep(5)    
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().home_size).send_keys(data.Logi_Data().size_No)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().home_pcs).send_keys(data.Logi_Data().No_of_pcs)
        sleep(5)
        home_mc = Select (self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().home_mc))
        home_mc.select_by_value('2')
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().home_mc_value).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().home_mc_value).send_keys(data.Logi_Data().non_mc_value)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().home_wastage_per).clear()
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().home_wastage_per).send_keys(data.Logi_Data().non_wastage_per)
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation Home bill  completed successfully,     Tag : {a}, home_section : {b}, home_size : {c}, home_pcs : {d}, home_mc_value : {e}, home_wastage_per : {f},".format(a= tags, b='GOLD CHAIN', c=data.Logi_Data().size_No, d = data.Logi_Data().No_of_pcs, e =data.Logi_Data().non_mc_value, f = data.Logi_Data().non_wastage_per))
        
        
        
        sleep(5)
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().old_metal).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Metals).click()
        sleep(5)
        metals = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        metals.send_keys('Gold')
        metals.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Metals_Type).click()
        sleep(5)
        Metals_Type = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Metals_Type.send_keys('BEATEN GOLD')
        Metals_Type.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().Category).click()
        sleep(5)
        Category = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        Category.send_keys('GOLD COIN')
        Category.send_keys(Keys.RETURN) 
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().purity).send_keys(data.Logi_Data().purity_value)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().metal_G_wt).send_keys(data.Logi_Data().G_wt_value)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().metal_D_wt).send_keys(data.Logi_Data().Dust_wt)
        sleep(5)
        self.driver.find_element(by=By.NAME,value=locators.Logi_Locators().metal_wastage_percentage).send_keys(data.Logi_Data().non_wastage_per)
        sleep(5)
        '''self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().purpose).click()
        sleep(5)
        purpose_list = self.driver.find_element(by=By.XPATH,value=locators.Logi_Locators().text_box)
        purpose_list.send_keys('Cash')
        purpose_list.send_keys(Keys.RETURN) '''
        self.driver.find_element(by=By.ID,value=locators.Logi_Locators().save_print).click()
        assert self.driver.title == 'Logimax Technology | Admin'
        print("Estimation old metal  completed successfully,     metals : {a}, Metals_Type : {b}, Category : {c}, purity : {d}, metal_G_wt : {e}, metal_D_wt : {f}, metal_wastage_percentage : {g},".format(a= 'Gold', b='BEATEN GOLD', c='GOLD COIN', d = data.Logi_Data().purity_value, e =data.Logi_Data().G_wt_value, f = data.Logi_Data().Dust_wt, g = data.Logi_Data().non_wastage_per, ))
        
       
        
        
        
        
        
        
        
 