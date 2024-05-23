export default function getListStudentIds(arrObj) {
  if (Array.isArray(arrObj)) {
    const newArr = arrObj.map((value) => value.id);
    return newArr;
  }
  return [];
}
