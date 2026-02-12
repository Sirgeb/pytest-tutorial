import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

# --- Fixtures ---

@pytest.fixture
def mcgonagall():
    return Teacher("Minerva McGonagall")

@pytest.fixture
def potions_class(mcgonagall):
    """Provides a classroom with a teacher but no students."""
    return Classroom(
        teacher=mcgonagall, 
        students=[], 
        course_title="Advanced Potions"
    )

@pytest.fixture
def full_classroom(mcgonagall):
    """Provides a classroom already at the limit (11 students)."""
    # The logic in your code says <= 10 allows adding, 
    # so 11 students is the tipping point.
    students = [Student(f"Student {i}") for i in range(11)]
    return Classroom(mcgonagall, students, "Defense Against the Dark Arts")

# --- Tests ---

def test_change_teacher(potions_class):
    snape = Teacher("Severus Snape")
    potions_class.change_teacher(snape)
    assert potions_class.teacher.name == "Severus Snape"

@pytest.mark.parametrize("student_name", ["Harry Potter", "Hermione Granger", "Ron Weasley"])
def test_add_student(potions_class, student_name):
    new_student = Student(student_name)
    potions_class.add_student(new_student)
    assert any(s.name == student_name for s in potions_class.students)
    assert len(potions_class.students) == 1

def test_remove_student(potions_class):
    draco = Student("Draco Malfoy")
    potions_class.add_student(draco)
    potions_class.remove_student("Draco Malfoy")
    assert draco not in potions_class.students

@pytest.mark.smell_test # Custom mark
def test_too_many_students_raises_exception(full_classroom):
    luna = Student("Luna Lovegood")
    # This should trigger the TooManyStudents exception
    with pytest.raises(TooManyStudents):
        full_classroom.add_student(luna)

@pytest.mark.skip(reason="Waiting for the Half-Blood Prince's book")
def test_brew_felix_felicis():
    pass