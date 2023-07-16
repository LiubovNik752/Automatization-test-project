import datetime

class Base():
    def __init__(self, driver_g):
        self.driver_g = driver_g

    """Method get current url"""
    def get_current_url(self):
        get_current_url = self.driver_g.current_url
        print("Current url " + get_current_url)

    """Method Screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver_g.save_screenshot('C:\\Users\\Lubov\\PycharmProjects\\berito\\screen\\' + name_screenshot)
        print("")

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Correct value word")

    """Method assert url"""
    def assert_url(self, result):
        get_current_url = self.driver_g.current_url
        assert get_current_url == result
        print("Correct value url")








