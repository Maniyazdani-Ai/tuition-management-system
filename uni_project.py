class student:
    tuition_per_unit = 12000000
    student_id = 4000
    def __init__(self,name,family,study,units):
        student.student_id += 1
        self.name = name
        self.family = family
        self.study = study
        self.units = units
        self.student_id_code = student.student_id
        pass


