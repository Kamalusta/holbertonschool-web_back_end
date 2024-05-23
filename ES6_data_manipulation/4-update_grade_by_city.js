export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  return getListStudents.filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      const updatedStudent = { ...student };
      if (gradeObj) {
        updatedStudent.grade = gradeObj.grade;
      } else {
        updatedStudent.grade = 'N/A';
      }
      return updatedStudent;
    });
}
