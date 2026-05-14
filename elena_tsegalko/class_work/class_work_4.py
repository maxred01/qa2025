import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.onliner.by/")
    page.get_by_text("Принять все cookie").click()
    page.get_by_role("link", name="Эти известные футболисты пролетели мимо ЧМ").click()
    page.get_by_role("link").first.click()
    page.locator(".news-header__image").click()
    page.locator("div").filter(has_text="Вход").nth(5).click()
    page.get_by_role("link", name="Технологии").click()
    page.get_by_role("link", name="Каталог").click()
    page.get_by_role("link", name="‹ Новости").click()
    page.get_by_role("link", name="‹ Новости").click()
    page.get_by_role("link", name="ASUS, Lenovo или MSI").click()
    page.get_by_text("Игровой ноутбук ASUS ROG Strix G16 2025 G614PR-RV007").click()
    page.get_by_text("6990").click()
    page.get_by_text("6990").click()
    page.get_by_role("radio", name="Одним платежом").check()
    page.get_by_role("radio", name="Одним платежом").check()
    page.get_by_role("radio", name="Частями").check()
    page.get_by_role("link", name="Купить").click()
    page.get_by_role("link", name="Перейти в корзину").click()
    page.locator(".button-style.button-style_auxiliary.button-style_small.cart-form__button.cart-form__button_increment").dblclick()
    page.locator(".button-style.button-style_auxiliary.button-style_small.cart-form__button.cart-form__button_increment").click()
    page.locator(".button-style.button-style_auxiliary.button-style_small.cart-form__button.cart-form__button_increment").dblclick()
    page.get_by_role("link").first.click()
    page.get_by_role("link", name="Мобильные телефоны", exact=True).click()
    page.get_by_role("link", name="Телефон Xiaomi Redmi Note 15").first.click()
    page.get_by_role("link", name="Купить").click()
    with page.expect_popup() as page1_info:
        page.get_by_text("Onlíner рекомендует Умные часы Xiaomi Redmi Watch 5").first.click()
    page1 = page1_info.value
    page1.locator(".product-gallery__shaft > div:nth-child(5)").click()
    page1.locator(".product-gallery__thumb.swiper-slide.swiper-slide-next").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)