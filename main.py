import logging
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.list import TwoLineListItem
import os

# Настройка логирования
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class LoginScreen(Screen):
    pass

class RegisterScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class TestSelectionScreen(Screen):
    pass

class QuestionScreen(Screen):
    pass

class ProgressScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class LessonsScreen(Screen):
    pass

class LessonDetailScreen(Screen):
    pass

class QuizApp(MDApp):
    tests = {
        'finance_1': [
            {"question": "Суть поняття фінансова грамотність", "answers": ["Фінансова грамотність", "Фінансова освіта", "Фінансова поведінка"], "correct": "Фінансова грамотність", "detail": "Здатність ефективно планувати і використовувати бюджет, приймати рішення у сфері особистих фінансів, орієнтуватися в послугах ."},
            {"question": "Що таке валова зарплата?", "answers": ["Заробіток після ПДВ", "Загальний заробіток", "Сума доп. виплат"], "correct": "Заробіток після ПДВ", "detail": "Валова зарплата  — це загальна сума доходу працівника до будь-яких відрахувань"},
            {"question": "Що таке чистий заробіток?", "answers": ["Заробіток до ПДВ", "Заробіток з основної ставки", "Сума додаткових виплат"], "correct": "Сума додаткових виплат", "detail": "Чистий заробіток — це сума грошей, яку працівник отримує на руки після відрахування всіх податків та інших утримань."},
            {"question": "Яке призначення податків?", "answers": ["Підвищення доходу працівників", "Зниження витрат уряду", "Фінансування держ. послуг"], "correct": "Фінансування держ. послуг", "detail": "Податки призначені для збору коштів, необхідних для фінансування діяльності уряду та громадських послуг."},
            {"question": "Як податки впливають на доходи працівників?", "answers": ["Збільшують чистий заробіток", "Зменшують чистий заробіток", "Не впливають"], "correct": "Зменшують чистий заробіток", "detail": "Податки зменшують чистий заробіток, адже вони є обов'язковими відрахуваннями з валової зарплати.."},
        ],
        'finance_2': [
            {"question": "Що таке фіксовані витрати?", "answers": ["Витрати що змінюються від рівня доходу", "Витрати, що залишаються незмінними", "Витрати на розваги"], "correct": "Витрати, що залишаються незмінними", "detail": "Фіксовані витрати — це регулярні витрати, сума яких залишається незмінною щомісяця."},
            {"question": "Які витрати називаються змінними?", "answers": ["Витрати на розваги", "Витрати, що завжди зростають", "Витрати, що змінються від рівня доходу"], "correct": "Витрати, що змінються від рівня доходу", "detail": "Витрати, які змінюються залежно від рівня доходу, споживання або інших обставин."},
            {"question": "Що таке заощадження?", "answers": ["Гроші, які витрачаються на розваги", "Гроші, які відкладені для майбутнього використання", "Гроші, які отримують від інвестицій"], "correct": "Гроші, які відкладені для майбутнього використання", "detail": "Це частина доходу, яка не витрачається, а відкладається для майбутнього використання.."},
            {"question": "Яка мета резервного фонду?", "answers": ["Фінансування відпусток", "Інвестування в акції", "Покриття непередбачених витрат"], "correct": "Покриття непередбачених витрат", "detail": "Це грошові заощадження, призначені для покриття непередбачених витрат таких як медичні витрати або ремонт житла."},
            {"question": "Які з наведених витрат належать до змінних?", "answers": ["Орендна плата", "Витрати на продукти", "Медичне страхування"], "correct": "Витрати на продукти", "detail": "Витрати на продукти та розваги є змінними, оскільки можуть значно варіюватися від споживчих потреб"},
        ],
        'finance_3': [
            {"question": "Що таке кредит?", "answers": ["Гроші, які ви даруєте іншій особі", "Позика з поверненням", "Гроші, які не потрібно повертати"], "correct": "Позика грошей або товарів з обов'язковим поверненням через певний час і, як правило, з відсотками", "detail": "Він дозволяє отримати доступ до ресурсів негайно, а не чекати на їх накопичення. "},
            {"question": "Які переваги кредиту?", "answers": ["Додатковий дохід", " Фінансова гнучкість", "Боргове навантаження"], "correct": "Фінансова гнучкість", "detail": "фінансова гнучкість та можливість здійснювати великі покупки або інвестиції без необхідності відкладати кошти."},
            {"question": "Що таке кредитна картка?", "answers": ["Для накопичення балів", "здійснення покупок в креди", "для оплати комунальних послуг"], "correct": "Пластикова картка, що дозволяє здійснювати покупки в кредит", "detail": " Дозволяє власнику здійснювати покупки в кредит в межах встановленого ліміту."},
            {"question": "Які равила користування кредитними картками?", "answers": [" Лише для великих покупок", " Витрачати доступні кошти щомісяця", " Погашати заборгованість вчасно"], "correct": "Погашати заборгованість вчасно, не перевищувати кредитний ліміт, стежити за відсотковими ставками", "detail": "Недопущення перевищення кредитного ліміту, що може вплинути на кредитний рейтинг."},
            {"question": "Що таке кредитний рейтинг?", "answers": ["Оцінка фінансової стабільності країни", "Рейтинг популярності банку", "Оцінка кредитоспроможності "], "correct": "Оцінка кредитоспроможності особи", "detail": "Впливає на можливість отримання кредиту та умови кредитування."},
        ],
        'finance_4': [
            {"question": "Що таке заощадження?", "answers": ["Інвестування грошей", "Витрачання грошей", "Відкладання грошей"], "correct": "Відкладання грошей", "detail": "Це процес відкладання грошей для майбутнього використання, зберігаючи їх у безпечних і надійних формах."},
            {"question": "Що таке інвестування?", "answers": ["Витрачання грошей", "Вкладення грошей", "Зберігання під матрацом"], "correct": "Вкладення грошей", "detail": " Інвестування — це процес вкладення грошей у фінансові інструменти, такі як акції, облігації."},
            {"question": "Яка основна відмінність між інвестуванням та заощадженнями?", "answers": ["Інвестування менш ризиковане", "Заощадження завжди приносять доход", "Інвестування має вищий ризик"], "correct": "Інвестування має вищий ризик", "detail": "Основна відмінність між інвестуванням та заощадженнями полягає у рівні ризику та потенційному доході."},
            {"question": "Які з наведених тверджень є правильною характеристикою заощаджень?", "answers": ["Низький рівень ризику, стабільний дохід", "Залежність від фондового ринку", "Необхідність моніторингу та аналізу"], "correct": "Низький рівень ризику, стабільний дохід", "detail": "Заощадження є низьким рівнем ризику та стабільним доходом, зазвичай зберігаються в банках"},
            {"question": "Які основні фактори впливають на вибір між інвестуванням та заощадженнями?", "answers": ["Лише фінансові цілі", "Лише горизонт інвестування", "Поточний рівень інфляції"], "correct": "Поточний рівень інфляції", "detail": "Вибір між інвестуванням та заощадженнями залежить від кількох факторів, таких як поточний рівень інфляції, рівень доходів, фінансові цілі та горизонт інвестування."},
        ],
        'finance_5': [
            {"question": "Що таке медичне страхування?", "answers": ["Страхування, яке покриває медичне обслуговування", "Страхування від збитків, пов'язаних з транспортними засобами", "Страхування від фінансових втрат"], "correct": "Страхування, яке покриває медичне обслуговування", "detail": "Медичне страхування покриває витрати на медичне обслуговування, включаючи консультації лікарів, лікування."},
            {"question": "Яке з видів страхування захищає від фінансових втрат, пов'язаних з аваріями?", "answers": ["Страхування майна", "Автомобільне страхування", "Життєве страхування"], "correct": "Автомобільне страхування", "detail": "Автомобільне страхування забезпечує захист від фінансових втрат, пов'язаних з дорожньо-транспортними пригодами."},
            {"question": "Що таке страхування відповідальності?", "answers": ["Страхування власного майна від стихійних лих", "Страхування, яке захищає від фінансових втрат через шкоду, завдану іншим особам", "Страхування від втрати доходу через безробіття"], "correct": "Страхування, яке захищає від фінансових втрат через шкоду, завдану іншим особам", "detail": "Страхування відповідальності покриває витрати, пов'язані з відшкодуванням шкоди, завданої іншим особам або їх майну."},
            {"question": "Яке страхування покриває втрати через знищення або пошкодження будинку?", "answers": ["Життєве страхування", "Страхування подорожей", "Страхування майна"], "correct": "Страхування майна", "detail": "трахування майна забезпечує фінансовий захист від втрат через знищення або пошкодження будинку."},
            {"question": "Кто был первым президентом Украины после Революции достоинства?", "answers": ["Страхування від втрати роботи", "Страхування медичних витрат", "Страхування, яке забезпечує виплату у разі смерті страхувальника"], "correct": "Страхування, яке забезпечує виплату у разі смерті страхувальника", "detail": "Життєве страхування забезпечує фінансовий захист родини або інших бенефіціарів у разі смерті страхувальника."},
        ],
    }

    # Смешанный тест
    tests['general_knowledge'] = []
    for key in tests:
        if key != 'general_knowledge':
            tests['general_knowledge'].extend(tests[key])

    current_question_index = 0
    scores = {
        'finance_1': 0,
        'finance_2': 0,
        'finance_3': 0,
        'finance_4': 0,
        'finance_5': 0,
        'general_knowledge': 0,
    }
    is_learning_mode = False
    learning_progress = []
    selected_test = []
    test_topic = ""

    def build(self):
        logging.debug("Building the application...")
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('main.kv')

    def validate_login(self):
        username = self.root.get_screen('login').ids.username.text
        password = self.root.get_screen('login').ids.password.text
        if self.check_credentials(username, password):
            self.root.current = 'menu'
        else:
            dialog = MDDialog(
                title="Помилка входу",
                text="Користувач з таким ім'ям вже існує.",
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())]
            )
            dialog.open()

    def register_user(self):
        username = self.root.get_screen('register').ids.reg_username.text
        password = self.root.get_screen('register').ids.reg_password.text
        if username and password:
            if not os.path.exists('users.txt'):
                with open('users.txt', 'w') as f:
                    pass
            with open('users.txt', 'r') as f:
                users = f.readlines()
            for user in users:
                if user.split(':')[0] == username:
                    dialog = MDDialog(
                        title="Помилка реєстрації",
                        text="Пользователь с таким логином уже существует.",
                        buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())]
                    )
                    dialog.open()
                    return
            with open('users.txt', 'a') as f:
                f.write(f"{username}:{password}\n")
            dialog = MDDialog(
                title="Реєстрація завершена",
                text="Ви успішно зареєструвались. Вітаю.",
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: self.go_to_login(dialog))]
            )
            dialog.open()
        else:
            dialog = MDDialog(
                title="Помилка реєстрації",
                text="Будь ласка, заповніть всі поля",
                buttons=[MDRaisedButton(text="OK", on_release=lambda x: dialog.dismiss())]
            )
            dialog.open()

    def check_credentials(self, username, password):
        if not os.path.exists('users.txt'):
            return False
        with open('users.txt', 'r') as f:
            users = f.readlines()
        for user in users:
            stored_username, stored_password = user.strip().split(':')
            if stored_username == username and stored_password == password:
                return True
        return False

    def go_to_register(self):
        self.root.current = 'register'

    def go_to_login(self, dialog=None):
        if dialog:
            dialog.dismiss()
        self.root.current = 'login'

    def go_to_test_selection(self):
        self.root.current = 'test_selection'

    def go_to_lessons(self):
        self.root.current = 'lessons'
        self.display_lessons()

    def display_lessons(self):
        lessons_screen = self.root.get_screen('lessons')
        lessons_list = lessons_screen.ids.lessons_list
        lessons_list.clear_widgets()

        for test_topic, questions in self.tests.items():
            for question_data in questions:
                lessons_list.add_widget(
                    TwoLineListItem(
                        text=question_data["question"],
                        secondary_text=f"Правильна відповідь: {question_data['correct']}",
                        on_release=lambda x, q=question_data: self.show_lesson_detail(q)
                    )
                )

    def show_lesson_detail(self, question_data):
        lesson_detail_screen = self.root.get_screen('lesson_detail')
        lesson_detail_screen.ids.lesson_detail_title.text = question_data["question"]
        lesson_detail_screen.ids.lesson_detail_content.text = f"Правильна відповідь: {question_data['correct']}\n\n{question_data.get('detail', 'Немає данних')}"
        self.root.current = 'lesson_detail'

    def start_quiz(self, test_topic, learning_mode=False):
        self.current_question_index = 0
        self.is_learning_mode = learning_mode
        self.learning_progress = []
        self.test_topic = test_topic
        self.selected_test = self.tests[test_topic]
        self.show_question()
        self.root.current = 'question'

    def show_question(self):
        if self.current_question_index < len(self.selected_test):
            question_data = self.selected_test[self.current_question_index]
            question_screen = self.root.get_screen('question')
            question_screen.ids.question_label.text = question_data["question"]
            answers_layout = question_screen.ids.answers_layout
            answers_layout.clear_widgets()

            for answer in question_data["answers"]:
                btn = MDRaisedButton(
                    text=answer,
                    pos_hint={"center_x": .5},
                    size_hint_y=None,
                    height=dp(50),
                    on_release=lambda btn: self.check_answer(btn.text)
                )
                answers_layout.add_widget(btn)
        else:
            self.show_result()

    def check_answer(self, selected_answer):
        correct_answer = self.selected_test[self.current_question_index]["correct"]
        if selected_answer == correct_answer:
            self.scores[self.test_topic] += 1

        if self.is_learning_mode:
            self.show_learning_dialog(correct_answer)
        else:
            self.current_question_index += 1
            self.show_question()

    def show_learning_dialog(self, correct_answer):
        self.learning_progress.append({"question": self.selected_test[self.current_question_index]["question"], "correct_answer": correct_answer})
        dialog = MDDialog(
            title="Режим навчання",
            text="Правильна відповідь: {}".format(correct_answer),
            buttons=[
                MDRaisedButton(
                    text="Далі",
                    on_release=lambda x: self.close_learning_dialog(dialog)
                )
            ]
        )
        dialog.open()

    def close_learning_dialog(self, dialog):
        dialog.dismiss()
        self.current_question_index += 1
        self.show_question()

    def show_result(self):
        percentage = (self.scores[self.test_topic] / len(self.selected_test)) * 100
        result_text = f"Ви відповіли правильно на {self.scores[self.test_topic]} из {len(self.selected_test)} питань.\nРівень знань: {percentage:.2f}%"
        dialog = MDDialog(
            title="Результати теста",
            text=result_text,
            buttons=[
                MDRaisedButton(
                    text="OK",
                    on_release=lambda x: self.go_to_menu(dialog)
                )
            ]
        )
        dialog.open()

    def go_to_menu(self, dialog=None):
        if dialog:
            dialog.dismiss()
        self.root.current = 'menu'

    def toggle_theme(self):
        self.theme_cls.theme_style = "Dark" if self.theme_cls.theme_style == "Light" else "Light"

    def show_progress(self):
        progress_screen = self.root.get_screen('progress')
        progress_list = progress_screen.ids.progress_list
        progress_list.clear_widgets()

        for item in self.learning_progress:
            progress_list.add_widget(
                TwoLineListItem(
                    text=item["question"],
                    secondary_text=f"Правильна відповідь: {item['correct_answer']}"
                )
            )
        self.root.current = 'progress'

    def show_profile(self):
        profile_screen = self.root.get_screen('profile')
        profile_screen.ids.finance_1_progress.value = self.calculate_progress('finance_1')
        profile_screen.ids.finance_1_percentage.text = "{}%".format(self.calculate_progress('finance_1'))
        profile_screen.ids.finance_2_progress.value = self.calculate_progress('finance_2')
        profile_screen.ids.finance_2_percentage.text = "{}%".format(self.calculate_progress('finance_2'))
        profile_screen.ids.finance_3_progress.value = self.calculate_progress('finance_3')
        profile_screen.ids.finance_3_percentage.text = "{}%".format(self.calculate_progress('finance_3'))
        profile_screen.ids.finance_4_progress.value = self.calculate_progress('finance_4')
        profile_screen.ids.finance_4_percentage.text = "{}%".format(self.calculate_progress('finance_4'))
        profile_screen.ids.finance_5_progress.value = self.calculate_progress('finance_5')
        profile_screen.ids.finance_5_percentage.text = "{}%".format(self.calculate_progress('finance_5'))
        profile_screen.ids.general_knowledge_progress.value = self.calculate_progress('general_knowledge')
        profile_screen.ids.general_knowledge_percentage.text = "{}%".format(self.calculate_progress('general_knowledge'))
        self.root.current = 'profile'

    def calculate_progress(self, test_topic):
        if test_topic not in self.scores:
            return 0
        total_questions = len(self.tests[test_topic])
        return (self.scores[test_topic] / total_questions) * 100 if total_questions > 0 else 0

if __name__ == "__main__":
    try:
        logging.debug("Starting the application...")
        QuizApp().run()
    except Exception as e:
        logging.exception("Exception occurred while running the app")
