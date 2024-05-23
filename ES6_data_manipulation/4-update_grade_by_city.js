export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents.filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find(grade => grade.studentId === student.id);
      if (gradeObj) {
        student.grade = gradeObj.grade;
      } else {
        student.grade = 'N/A';
      }
      return student;
    });
}
