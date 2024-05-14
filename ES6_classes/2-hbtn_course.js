export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string')
      throw new TypeError('Name must be a string');
    if (typeof length !== 'number')
      throw new TypeError('Length must be a number');
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

  set students(nstudents) {
    this._students = nstudents;
  }
}
