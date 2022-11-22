from selene import by, be
from selene.support.shared import browser


def test_github():
    browser.open("https://github.com")
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").type("qa_guru_hw_2_8").press_enter()
    browser.element(by.link_text("AndrewVasutenko/qa_guru_hw_2_8")).click()
    browser.element("#issues-tab").should(be.visible)
