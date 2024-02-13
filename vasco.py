import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Load names from the CSV
file_path = '/Applications/MAMP/Vasco/nomes-registados-2017.csv'
names_df = pd.read_csv(file_path)
names_list = names_df['nome'].tolist()

def enter_text(driver, input_id, text):
    input_field = driver.find_element(By.ID, input_id)
    input_field.clear()
    input_field.send_keys(text)
    print(f"Entered text '{text}' into input field with ID '{input_id}'")

def select_random_option(driver, dropdown_id):
    country_dropdown = Select(driver.find_element(By.ID, dropdown_id))
    countries = country_dropdown.options[1:]
    random_country = random.choice(countries).text
    country_dropdown.select_by_visible_text(random_country)
    print(f"Selected random country '{random_country}' from dropdown with ID '{dropdown_id}'")

# Initialize the Chrome driver
driver = webdriver.Chrome()  # Update this path

for i in range(2500):
    # Open the HTML file
    driver.get("http://localhost/wordpress/")
    print(f"Iteration {i+1}")
    time.sleep(random.randint(2,3))

    # Randomly select first and last names
    first_name = random.choice(names_list)
    last_name = random.choice(names_list)

    # Fill in the form fields
    enter_text(driver, "ff_3_names_first_name_", first_name)
    enter_text(driver, "ff_3_names_last_name_", last_name)

    #pais
    select_random_option(driver, "ff_3_country-list")

    #altura
    random_int = random.randint(150, 210)
    random_string = str(random_int)
    enter_text(driver, "ff_3_numeric-field", random_string)

    random_int = random.randint(50, 120)
    random_string = str(random_int)
    enter_text(driver, "ff_3_numeric-field_1", random_string)

    #genero
    select_random_option(driver, "ff_3_dropdown_8")

    #etnia
    select_random_option(driver, "ff_3_dropdown_1")

    #hair
    select_random_option(driver, "ff_3_dropdown_7")

    #cor dos olhos
    select_random_option(driver, "ff_3_dropdown_11")

    #tamanho da tshirt
    select_random_option(driver, "ff_3_dropdown")

    #tamanho do pé
    random_int = random.randint(35, 48)
    random_string = str(random_int)
    enter_text(driver, "ff_3_numeric-field_2", random_string)

    #fumador
    select_random_option(driver, "ff_3_dropdown_2")

    #bebida
    select_random_option(driver, "ff_3_dropdown_3")

    #salario
    select_random_option(driver, "ff_3_dropdown_5")

    #Religion
    select_random_option(driver, "ff_3_dropdown_6")

    #orientação sexual
    select_random_option(driver, "ff_3_dropdown_9")

    #politica
    select_random_option(driver, "ff_3_dropdown_10")

    # #checkBox
    # checkbox = driver.find_element(By.ID, "terms-n-condition_85c9791db792b873689aed7c6785967e")
    # checkbox.click()

    print("mimimim")
    time.sleep(random.randint(2, 4))
    print("acordou")

    # Submit the form
    print("Submitting form")
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Submit Form')]")
    time.sleep(random.randint(2, 4))
    submit_button.click()
    time.sleep(random.randint(2, 4))


# Close the browser after completing the iterations
driver.quit()
