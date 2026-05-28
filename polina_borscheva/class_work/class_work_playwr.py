import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hoster.by/")
    page.get_by_role("button", name="Принять").click()
    page.get_by_text("Серверы", exact=True).click()
    page.get_by_role("link", name="Разовые работы").click()
    page.get_by_text("Веб-сервер и окружение").first.click()
    page.locator("span").filter(has_text="IIS").first.click()
    page.get_by_role("img").nth(5).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
