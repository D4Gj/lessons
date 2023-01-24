import Lesson_16.double_import.main as main


def func_b():
    main.func_a()


class Child(main.Base):
    pass
