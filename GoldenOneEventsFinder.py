from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#Empty list to hold all events extracted from Golden 1 website
event_names = []

def extractEvents():
    #Using chrome browser
    driver = webdriver.Chrome()

    #Go to Golden 1 website
    driver.get("https://www.golden1center.com/events")

    #Wait up to ten seconds for page to load
    driver.implicitly_wait(10)

    #Try 3 times to click the load more button
    for load_index in range(3):
        try:
            #load more button element
            moreButton = driver.find_element(By.XPATH, "//*[@id='loadMoreEvents']")
            moreButton.click()
            #Wait for page to load more events
            driver.implicitly_wait(5)
        except:
            print("No Load-More Button found")
            #Print remaining number of attempts at pressing load more
            print( str(2 - load_index) + " attempts left...")

    #Place all loaded events into events_elements list
    events_elements = []
    #Up to 40 results may be appeneded (this is an arbitrary number)
    for i in range(1,41):
        try:
            events_elements.append( driver.find_element(By.XPATH, "//*[@id='list']/div[" + str(i) + "]") )
        except:
            #When the next attempt at appending fails (because the next Div does not exist,
            #print number of events which were appeneded, and break out of the for loop
            print( str(i) + " events appended \n")
            break
    
    #For each element in events_elements, extract event name
    for event in events_elements:
        event_names.append( event.text )

    #Print the events names list, this includes the date, have not found how to extract only the name
    for name in event_names:
        print( name + "\n" )

    #Wait to see what happens before closing page and terminating program
    time.sleep(10)

    #Close the Chrome driver and the webpage it opened
    driver.quit()

extractEvents()
