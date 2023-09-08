from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import undetected_chromedriver as uc

options = uc.ChromeOptions()
options.binary_location = "C:\\Users\\Lazaro B\\AppData\\Local\\Chromium\\Application\\chrome.exe"
driver = uc.Chrome(options=options)

url = 'https://bo3.gg/matches/into-the-breach-vs-espionage-16-08-2023'
driver.get(url)

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "u-relative.c-widget-match-scoreboard-wrap")))

parent_div = driver.find_element(By.CLASS_NAME, "u-relative.c-widget-match-scoreboard-wrap")
group_divs = parent_div.find_elements(By.CLASS_NAME, "c-widget-match-scoreboard")
print("Number of table-groups found: ", len(group_divs))

player_data = []

for group_div in group_divs:
    print("Processing table-group")
    rows = group_div.find_elements(By.CLASS_NAME, "table-row")
    print(f'Number of rows found: {len(rows)}')

    span_elements = group_div.find_elements(By.CLASS_NAME, "nickname")
    nicknames = [span.text for span in span_elements]
    print(f'Nicknames found: {nicknames}')

    nickname_index = 0

    for i, row in enumerate(rows):
        if 'total' in row.get_attribute('class'):
            print(f"Skipping 'Total' row at index {i}.")
            continue

        # Skip the first row of each table-group
        if i == 0:
            print(f"Skipping header-like row at index {i}.")
            continue

        print(f"Processing row at index {i}")

        # Check if the row contains the necessary information (like 'kills', 'deaths' etc.)
        try:
            row.find_element(By.CSS_SELECTOR, ".table-cell.kills p")
        except NoSuchElementException:
            print(f"Skipping unusual row at index {i}.")
            continue

        try:
            nickname = nicknames[nickname_index]
        except IndexError:
            print(f"IndexError at row index {i}. Nickname index was {nickname_index}.")
            continue

        nickname_index += 1

        kills = row.find_element(By.CSS_SELECTOR, ".table-cell.kills p").text
        deaths = row.find_element(By.CSS_SELECTOR, ".table-cell.deaths p").text
        assists = row.find_element(By.CSS_SELECTOR, ".table-cell.assists p").text
        adr = row.find_element(By.CSS_SELECTOR, ".table-cell.adr p").text

        player_data.append({
            "Nickname": nickname,
            "Kills": kills,
            "Deaths": deaths,
            "Assists": assists,
            "ADR": adr,
        })

driver.quit()

df = pd.DataFrame(player_data)
try:
    df.to_csv('C:\\Users\\Lazaro B\\Documents\\GitHub\\CSGOProject\\data\\Espionage\\IntoTheBreachVersusEspionage16-08-2023.csv', index=False)
    print("CSV file has been saved.")
except Exception as e:
    print("An error occurred while saving the CSV file: ", str(e))

print(df)
