import dryscrape                                                                                                                                       [13/329]from pyvirtualdisplay import Display                                                                                                                           
                                                                                                                                                               
                                                                                                                                                               
# setup virtual display                                                                                                                                        
display = Display(visible=0, size=(1920, 1080))                                                                                                                
display.start()                                                                                                                                                
#start_xvfb()                                                                                                                                                  
                                                                                                                                                               
                                                                                                                                                               
driver = dryscrape.Session()                                                                                                                                   
                                                                                                                                                               
# "selenify" some methods                                                                                                                                      
                                                                                                                                                               driver.get                   = lambda url : driver.visit(url)


    # singular
driver.find_element_by_id    = lambda id : driver.at_xpath('//*[@id="{}"]'.format(id))
driver.find_element_by_name  = lambda name : driver.at_xpath('//*[@name="{}"]'.format(name))
driver.find_element_by_xpath = lambda xpath :  driver.at_xpath(xpath)


    # plural
driver.find_elements_by_id    = lambda id : driver.xpath('//*[@id="{}"]'.format(id))
driver.find_elements_by_name  = lambda name : driver.xpath('//*[@name="{}"]'.format(name))
driver.find_elements_by_xpath = lambda xpath :  driver.xpath(xpath)


# and add some handy methods

    # singular
driver.find_element_by_class_name  = lambda _class : driver.at_xpath('//*[@class="{}"]'.format(_class))
driver.find_element_by_class_name_and_element_name = lambda _class, element : driver.at_xpath('//{0}[@class="{1}"]'.format(element,_class))

    # plural
driver.find_elements_by_class_name  = lambda _class : driver.xpath('//*[@class="{}"]'.format(_class))
driver.find_elements_by_class_name_and_element_name = lambda _class, element : driver.xpath('//{0}[@class="{1}"]'.format(element,_class))

# find by css

    # singular

driver.find_element_by_css = lambda _css : driver.at_css(_css)

    # plural

driver.find_elements_by_css = lambda _css : driver.css(_css)
