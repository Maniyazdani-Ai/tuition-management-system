class student:

    tuition_per_unit = 1000000
    student_id = 4000 

    def __init__(self,name,family,study,units):
        student.student_id += 1
        self._name = name
        self._family = family
        self._study = study
        self._units = units
        self._student_id_code = student.student_id
        self._finaly_tuition = self.discount()
         

    def discount(self):
        all_tuition = self._units * student.tuition_per_unit
        if self._units < 12:
            return all_tuition
        elif 12 <= self._units <= 18:
            return all_tuition * 0.05
        else:
            return all_tuition * 0.1

    @property
    def name(self):
        return self._name

    @property
    def family(self):
        return self._family

    @property
    def study(self):
        return self._study

    @property
    def units(self):
        return self._units

    @property
    def studeny_id_code(self):
        return self._student_id_code

    @property
    def tuition(self):
        return self._tuition

    @property
    def finaly_tuition(self):
        return self._finaly_tuition

    @name.setter
    def name(self,name):
        self._name = name

    @family.setter
    def family(self,family):
        self._family = family

    @study.setter
    def study(self,study):
        self._study = study

    @units.setter
    def units(self,units):
        self._units = units

    def __str__(self):
        return f"name and family : {self._name} {self._family}\nstudy:{self._study}\nunits : {self._units}\nstudent code : {self._student_id_code}\ntuition:{self._finaly_tuition}"

