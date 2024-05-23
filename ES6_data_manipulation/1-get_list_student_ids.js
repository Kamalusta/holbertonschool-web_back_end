export default function getListStudentIds(arrObj) {
  if (Array.isArray(listOfStudents)) {
    const newArr = arrObj.map((value) => value.id);
    return newArr;
  }
  return [];
}
