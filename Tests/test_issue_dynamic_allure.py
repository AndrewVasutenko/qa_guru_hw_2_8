import allure
from selene import by, be
from selene.support.shared import browser


def test_github_with_allure_steps():
    with allure.step("Открываем hitgub")
    browser.open("https://github.com")

    with allure.step("Выполняем поиск и открываем репозиторий")
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").type("qa_guru_hw_2_8").press_enter()
    browser.element(by.link_text("AndrewVasutenko/qa_guru_hw_2_8")).click()

    with allure.step("Находим Issues")
    browser.element("#issues-tab").should(be.visible)

def test_github_with_allure_steps():
