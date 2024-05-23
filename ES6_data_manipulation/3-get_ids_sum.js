export default function getStudentIdsSum(students) {
    const arr = students.map((value) => value.id);
    return arr.reduce((accumulator, currentValue) => accumulator + currentValue);
}
