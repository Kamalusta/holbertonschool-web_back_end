export default function getListStudentIds(arrObj) {
  if (typeof arrObj != 'object') {
    return [];
  }
  const newArr = arrObj.map((value) => value.id)
  return newArr;
}
