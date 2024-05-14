export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string')
      throw new TypeError('Name must be a string');
    if (typeof length !== 'number')
      throw new TypeError('Length must be a number');
    if (!Array.isArray(students)) {
      throw new TypeError('Students must be an array');
    }
    students.forEach((student) => {
      if (typeof student !== 'string') {
        throw new TypeError('Students must be an array of strings');
      }
    });
    this._name = name;
    this._length = length;
    this._students = students;
  }
  get name() {
    return this._name;
  }

  set name(nname) {
    if (typeof nname === 'string') {
      this._name = nname;
    }
    else {
      throw new TypeError("Name must be a string");
    }
  }
  get length() {
    return this._length;
  }

  set length(nlength) {
    if (typeof nlength === 'number') {
      this._length = nlength;
    }
    else {
      throw new TypeError("Length must be a number");
    }
  }
  get students() {
    return this._students;
  }

  set students(newStudents) {
    if (!Array.isArray(newStudents)) {
      throw new TypeError('Students must be an array');
    }
    this.students.forEach((student) => {
      if (typeof student !== 'string') {
        throw new TypeError('Students must be an array of strings');
      }
    });
    this._students = newStudents;
  }
}
