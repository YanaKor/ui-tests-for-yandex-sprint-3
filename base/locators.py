from selenium.webdriver.common.by import By


class Urls:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTRATION_FORM_URL = f'{BASE_URL}/register'
    RECOVERY_FORM_URL = f'{BASE_URL}/forgot-password'


class RegistrationLocators:
    SIGN_IN_BUTTON = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка войти в аккаунт
    REGISTER_LINK = (By.XPATH, ".//a[contains(text(), 'Зарегистрироваться')]")  # Ссылка регистрации на сайте
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # Поле ввода имени
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # Поле ввода email
    PASSWORD_FIELD = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # Поле ввода пароля
    REGISTER_BUTTON = (By.XPATH, ".//button[contains(text(), 'Зарегистрироваться')]")  # Кнопка зарегистрироваться
    ERROR_MESSAGE = (By.XPATH, ".//form//p[contains(@class, 'input__error')]")  # Ошибка ввода пароля
    ORDER_BUTTON = (By.XPATH, ".//main//button[contains(text(), 'Оформить заказ')]")  # Кнопка оформить заказ


class LogInFormLocators:
    LOGIN_BUTTON_ON_MAIN_PAGE = (
        By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")  # Кнопка войти в аккаунт на главной странице
    LOGIN_EMAIL_FIELD = (By.XPATH, ".//form//input[@name='name']")  # Поле ввода email на странице входа
    LOGIN_PASSWORD_FIELD = (By.XPATH, ".//form//input[@type='password']")  # Поле ввода пароля на странице входа
    LOGIN_BUTTON = (By.XPATH, ".//form//button[contains(text(), 'Войти')]")  # Кнопка "Войти" в форме
    HEADER_ON_MAIN_PAGE = (
    By.XPATH, ".//main//h1[contains(text(), 'Соберите бургер')]")  # проверка текста "Соберите бургер" после входа в ЛК
    PERSONAL_ACCOUNT_BUTTON = (
    By.XPATH, ".//nav//p[contains(text(), 'Личный Кабинет')]")  # вход через кнопку «Личный кабинет»
    LOGIN_BUTTON_FROM_REGISTER_AND_RECOVERY_PAGE = (By.XPATH,
                                                    ".//main//a[contains(text(), 'Войти')]")  # вход через кнопку в форме регистрации и в форме восстановления пароля


class PersonalAccountLocators:
    HEADER_OF_THE_FORM = (By.XPATH, ".//main//h2[contains(text(), 'Вход')]")  # Заголовок страницы
    LOGO = (By.XPATH, ".//div[contains(@class, 'header__logo')]")
    CONSTRUCTOR = (By.XPATH, ".//li//p[contains(text(), 'Конструктор')]")


class LogoutLocators:
    LOGOUT_BUTTON = (By.XPATH, ".//li//button[contains(text(), 'Выход')]")  # Кнопка "Выйти"


class ConstructorLocators:
    BUNKS_TAB = (By.XPATH, ".//div//span[contains(text(), 'Булки')]")  # вкладка "Булки"
    SAUCES_TAB = (By.XPATH, ".//div//span[contains(text(), 'Соусы')]")  # вкладка "Соусы"
    STUFFING_TAB = (By.XPATH, ".//div//span[contains(text(), 'Начинки')]")  # вкладка "Начинки"
    BUNKS_SECTION = (By.XPATH, ".//div//h2[contains(text(), 'Булки')]")  # раздел "Булки"
    SAUCES_SECTION = (By.XPATH, ".//div//h2[contains(text(), 'Соусы')]")  # раздел "Соусы"
    STUFFING_SECTION = (By.XPATH, ".//div//h2[contains(text(), 'Начинки')]")  # раздел "Начинки"
