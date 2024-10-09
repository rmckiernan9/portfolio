#Created by Ryan McKiernan, 2024
#This version obtains the training dataset by mining the past 10 seasons of most FBS teams
#------------------------------------------------------------------
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

#get teams and years as lists
teamsC = pd.read_csv("team_names.csv",header=None)
teams = teamsC.iloc[:,0].tolist()
years = list(range(2014, 2024))  # Years from 2014 to 2023

# Initialize an empty DataFrame to hold all data
all_data = pd.DataFrame()

# Replace with your PFF login credentials
EMAIL = "..."
PASSWORD = "..."

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # login authentication
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
        
    except Exception as e:
        print(f"Main page load error: {e}")

    # Base URL pattern to iterate through
    base_url = "https://premium.pff.com/ncaa/teams/{year}/REGPO/{team}/schedule"  
    
    #Iteration process (may take a while to run)
    try:
        for team in teams:
            for year in years:
                url = base_url.format(team=team, year=year)
                try:
                    driver.get(url)
                    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "kyber-table-body__rows")))
                except TimeoutException:
                    print(f"Timeout: Table not found for {team} in {year}. Skipping.")
                    continue  
                except Exception as e:
                    print(f"Error loading URL: {url}, Error: {e}. Skipping this team/year.")
                    continue  
                
                #Locate the tables on the page to pull out of
                try:
                    table_bodies = driver.find_elements(By.CLASS_NAME, "kyber-table-body__rows")
                    table_body = table_bodies[0] if table_bodies else None

                    if not table_body:
                        print(f"No table found for {team} in {year}. Skipping...")
                        continue

                    rows = table_body.find_elements(By.CLASS_NAME, "kyber-table-body__row")
                    rows = [row for row in rows if row.is_displayed()]  

                    table_data = []

                    for row_index, row in enumerate(rows):
                        try:
                            cells = row.find_elements(By.CLASS_NAME, "kyber-table-body-cell")

                            if len(cells) < 17:
                                continue

                            if "Week" in cells[0].text or "Date" in cells[0].text:
                                continue

                            row_data = []

                            for i, cell in enumerate(cells[:-1]):  
                                try:
                                    if i < 6:  
                                        row_data.append(cell.text)
                                    else:  
                                        grade_text = cell.find_element(By.CLASS_NAME, "kyber-grade-badge__info-text").text
                                        row_data.append(grade_text)
                                except NoSuchElementException:
                                    row_data.append(None)
                                except Exception as e:
                                    row_data.append(None)
                                    print(f"Error processing cell {i + 1} in row {row_index + 1}: {e}")

                            if any(row_data):  # Append non-empty rows
                                table_data.append(row_data)

                        except StaleElementReferenceException:
                            print(f"Row {row_index + 1} is no longer attached to the DOM.")
                        except Exception as e:
                            print(f"Error processing row {row_index + 1}: {e}")

                    column_names = ["Opponent", "Date", "Time", "W/L", "PF", "PA", "OVER", "OFF", "PASS", "PBLK", "RECV", "RUN", "RBLK", "DEF", "RDEF", "TACK", "PRSH", "COV", "SPEC"]

                    df = pd.DataFrame(table_data, columns=column_names)
                    df["Year"] = year
                    df["Team"] = team

                    all_data = pd.concat([all_data, df], ignore_index=True)

                except Exception as e:
                    print(f"Error processing table data for {team} in {year}: {e}")
                    continue

    except Exception as e:
        print(f"Error occurred: {e}")

finally:
    driver.quit()

# Save the collected data to a CSV file
all_data.to_csv('all_team_data.csv', index=False)
#----------------
