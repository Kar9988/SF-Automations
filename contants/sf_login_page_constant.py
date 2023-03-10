from selenium.webdriver.common.by import By

LOGIN_URL = "https://sportyfriends.com/en/mho"

LOGIN_BUTTON = {"by": By.CSS_SELECTOR, "value": "nav > a"}
EMAIL_FIELD = {"by": By.CSS_SELECTOR, "value": "form > div > input"}
CORRECT_EMAIL = "admin@admin.com"
# CORRECT_PASSWORD =