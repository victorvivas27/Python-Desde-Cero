import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Se espera que un título "contenga" una subcadena
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Haga clic en el enlace link.
    page.get_by_role("link", name="Get started").click()

    # Espera que la página tenga un encabezado con el nombre de  Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()