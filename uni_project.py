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
        self.tuition = self.all_tuition()
        self.finaly_tuition = self.discount()

    def all_tuition(self):
        all_tuition = self.units * student.tuition_per_unit
        return all_tuition

    def discount(self):
        if self.units < 12:
            return self.all_tuition()
        elif 12 <= self.units <= 18:
            return self.all_tuition() * 0.05
        else:
            return self.all_tuition * 0.1
          


