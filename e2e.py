from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def test_scores_service(url):
    my_driver = webdriver.Chrome(ChromeDriverManager().install())
    my_driver.get(url)
    score = int(my_driver.find_element_by_xpath('//*[@id="score0"]').text)
    print(score)
    return 0 < score < 1000


def main():
    """
    Call our tests function.
    The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed.
    """
    url = "http://127.0.0.1:8777/"
    if test_scores_service(url):
        print("exit(0)")
        return exit(0)
    else:
        print("exit(-1)")
        return exit(-1)


if __name__ == '__main__':
    main()
