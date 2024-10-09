#Created by Ryan McKiernan, 2024
#This File grabs the current power ratings/unit grades of each team
#Make sure to have webdriver extension installed on chrome

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time

# Replace with your login credentials (PFF login info)
EMAIL = "..."
PASSWORD = "..."

# Initialize WebDriver and navigate to the login page
# Elements are determined by inspecting through browser interface
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    driver.get("https://www.pff.com/login")
    email = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "login[email]")))
    email.send_keys(EMAIL)

    passw = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "login[password]")))
    passw.send_keys(PASSWORD)

    login = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login.click()

    time.sleep(20) #for captcha 
    try:
        WebDriverWait(driver, 25).until(EC.url_contains("https://www.pff.com/"))
        driver.get("https://premium.pff.com/ncaa/teams/2024/REGPO")  #Current data
        
    except Exception as e:
        print(f"Main page load error: {e}")
    
    try:
        table_element = WebDriverWait(driver, 40).until(EC.presence_of_element_located((By.CLASS_NAME, "kyber-table-body__rows")))
        
        #Locates the row limit options, makes adjustment to get all 134 FBS teams instead of page default of 50
        row_limit_options = WebDriverWait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "kyber-filter-strip__option")))
        
        for option in row_limit_options:
            if option.text == "200":  
                option.click()
                break
    
        # Wait for the table to refresh, if needed
        time.sleep(5)
    
        # Retrieve the table body
        table_body = driver.find_element(By.CLASS_NAME, "kyber-table-body__rows") 
        
        rows = table_body.find_elements(By.CLASS_NAME, "kyber-table-body__row")

        table_data = []

        # Extract data from each row
        for row in rows:
            # Extract the cells in the current row
            row_data = []
            cells = row.find_elements(By.CLASS_NAME, "kyber-table-body-cell")
            cells = cells[:-1] #dont need the button at the end of each row
            
            for i, cell in enumerate(cells):
                # If it's a grade cell, we look for the grade text
                try:
                    if i >= 3:  # assuming the first 2 columns are Team and Record which use different classes
                        grade_text = cell.find_element(By.CLASS_NAME, "kyber-grade-badge__info-text").text
                        row_data.append(grade_text)
                    else:
                        # Handle the regular text (Team, Record, PF, PA)
                        text_value = cell.text
                        row_data.append(text_value)
                except Exception as e:
                    # Handle any exceptions or missing data
                    print(f"Error processing cell: {e}")
                    row_data.append(None)
        
            # Add the extracted row data to the main table data list
            table_data.append(row_data)

        # Create a DataFrame from the collected data with column names added on
        column_names = ["Record", "PF", "PA", "OVER", "OFF", "PASS", "PBLK", "RECV", "RUN", "RBLK", "DEF", "RDEF", "TACK", "PRSH", "COV", "SPEC"]  # "Rank", "Team", 
        df = pd.DataFrame(table_data, columns=column_names)

        print(df)

    except Exception as e:
        print(f"Error locating the table: {e}")
    
except Exception as e:
    print(f"Error occurred: {e}")
    driver.save_screenshot('error_screenshot.png')

finally:
    driver.quit()   
    
df.to_csv("pff_week_colGrades.csv")
