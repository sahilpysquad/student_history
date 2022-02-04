from .models import GradeHistory, Student


def year_wise_spi(input_year,):
    first_year_student_spi = {}
    second_year_student_spi = {}
    third_year_student_spi = {}
    fourth_year_student_spi = {}

    objs = GradeHistory.objects.all()
    for obj in objs:
        print(obj)
        college_start_year = obj.student.start_first_year
        college_passing_year = college_start_year + 4 + len(obj.student.detain_year)
        passing_years = []
        for college_year in range(college_start_year + 1, college_passing_year + 1):
            if college_year not in obj.student.detain_year:
                passing_years.append(college_year)
        print(passing_years)
        if input_year == passing_years[0] and obj.first_year_spi is not None:
            first_year_student_spi[obj.student.id] = {obj.student.fname: obj.first_year_spi}

        if input_year == passing_years[1] and obj.second_year_spi is not None:
            second_year_student_spi[obj.student.id] = {obj.student.fname: obj.second_year_spi}

        if input_year == passing_years[2] and obj.third_year_spi is not None:
            third_year_student_spi[obj.student.id] = {obj.student.fname: obj.third_year_spi}

        if input_year == passing_years[3] and obj.fourth_year_spi is not None:
            fourth_year_student_spi[obj.student.id] = {obj.student.fname: obj.fourth_year_spi}

    students_spi = {
        "First Year Student SPI": first_year_student_spi,
        "Second Year Student SPI": second_year_student_spi,
        "Third Year Student SPI": third_year_student_spi,
        "Fourth Year Student SPI": fourth_year_student_spi,
    }
    return students_spi
