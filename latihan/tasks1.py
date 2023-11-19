from robocorp.tasks import task
from robocorp import browser
from robot.libraries.BuiltIn import BuiltIn

@task
def robot_spare_bin_python():
    """Insert the sales data excel for the week to form web"""
    browser.configure(
        slowmo=100,
    )
    open_the_intranet_website()
    log_in()
    fill_and_submit_sales_form()
    BuiltIn().sleep("5m")

def open_the_intranet_website():
    """Navigates to the given URL"""
    browser.goto("https://robotsparebinindustries.com/")

def log_in():
    """Fills in the login form and clicks the 'Log in' button"""
    page = browser.page()
    page.fill("#username", "maria")
    page.fill("#password", "thoushallnotpass")
    page.click("button:text('Log in')")

def fill_and_submit_sales_form():
    """Fills in the sales data and click the 'Submit' button"""
    page = browser.page()

    page.fill("#firstname", "John")
    page.fill("#lastname", "Smith")
    page.fill("#salesresult", "123")
    page.select_option("#salestarget", "10000")
    page.click("text=Submit")