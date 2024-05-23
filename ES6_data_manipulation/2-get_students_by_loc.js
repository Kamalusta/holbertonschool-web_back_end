export default function getStudentsByLocation(list, city) {
  return list.filter((values) => values.location === city);
}
