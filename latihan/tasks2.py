import os
from robocorp.tasks import task
from robocorp import browser
from RPA.HTTP import HTTP   #to download file from remote web server

@task
def robot_spare_bin_python():
    """Insert the sales data for the week and download file"""
    browser.configure(
        slowmo=100,
    )
    open_the_intranet_website()
    log_in()
    download_excel_file()
    fill_and_submit_sales_form()

def open_the_intranet_website():
    """Navigates to the given URL"""
    # Set the ROBOCORP_BROWSER environment variable to the path of your Chrome executable
    os.environ["ROBOCORP_BROWSER"] = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")

def download_excel_file():
    """Downloads excel file from the given URL"""
    http = HTTP()
    http.download(url="https://robotsparebinindustries.com/SalesData.xlsx", overwrite=True)

def fill_and_submit_sales_form():
    """Fills in the sales data and click the 'Submit' button"""
    page = browser.page()

    page.fill("#firstname", "Ina")
    page.fill("#lastname", "Nur")
    page.fill("#salesresult", "345")
    page.select_option("#salestarget", "50000")
    page.click("text=Submit")