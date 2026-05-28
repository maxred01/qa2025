import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://hoster.by/")
    page.get_by_role("banner").get_by_text("Кибербезопасность").click()
    page.get_by_role("link", name="Хостинг для персональных данных хит").click()
    page.get_by_role("banner").get_by_text("IT-аутсорсинг", exact=True).click()
    page.get_by_role("link", name="Отказоустойчивый кластер").click()
    page.get_by_role("heading", name="Каким компаниям нужны отказоустойчивые решения").click()
    page.locator("li:nth-child(2) > .m-accordion-toggle > .plus").click()
    page.locator("li:nth-child(3) > .m-accordion-toggle > .plus").click()
    page.get_by_role("link", name="Настройка файлов cookie").click()
    page.get_by_text("Целевые (аналитические, рекламные) файлы cookie").click()
    page.get_by_role("button", name="Отменить").click()
    page.get_by_role("link", name="Договоры").click()
    page.get_by_role("link", name="5. Публичный договор возмездного оказания услуг защищенного хостинга на выделенном физическом сервере", exact=True).click()
    page.get_by_role("link", name="FAQ").click()
    page.get_by_role("button", name="Поиск").click()
    page.get_by_role("textbox", name="Искать в базе знаний").click()
    page.get_by_role("textbox", name="Искать в базе знаний").fill("dadadad")
    page.get_by_role("button", name="Поиск").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)