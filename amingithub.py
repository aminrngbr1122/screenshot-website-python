
title = """
    _     __  __  ___  _   _   ____   _   _   ____  ____   ____     ____  ___  _____  _   _  _   _  ____  
   / \   |  \/  ||_ _|| \ | | |  _ \ | \ | | / ___|| __ ) |  _ \   / ___||_ _||_   _|| | | || | | || __ ) 
  / _ \  | |\/| | | | |  \| | | |_) ||  \| || |  _ |  _ \ | |_) | | |  _  | |   | |  | |_| || | | ||  _ \ 
 / ___ \ | |  | | | | | |\  | |  _ < | |\  || |_| || |_) ||  _ <  | |_| | | |   | |  |  _  || |_| || |_) |
/_/   \_\|_|  |_||___||_| \_| |_| \_\|_| \_| \____||____/ |_| \_\  \____||___|  |_|  |_| |_| \___/ |____/ 

"""

try:

  from selenium import webdriver
  import time
  from selenium.webdriver.common.by import By
  from art import *

  def screen_web():
   #  The function of taking a screenshot from your website is enough,
   #  just call this function and call to be able to use these codes...
   print(title)
   driver = webdriver.Chrome()
   driver.minimize_window()
   url = input('\n url :')
   print('\n pls wait ... \n')
   driver.get(url)
   driver.maximize_window()
   time.sleep(3)
   driver.minimize_window()
   driver.save_screenshot('./screen.png')
   driver.quit()
   print('\n screen saved (: \n')

except:
  print(title)
  print('\n oo no pls install lib selenium and art ! \n pip install selenium \n pip install art \n pip install time')
  
