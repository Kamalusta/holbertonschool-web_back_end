export default function cleanSet(set, startString) {
  if (!startString || !startString.length) return '';
  const newArr = Array.from(set)
    .filter((values) => values.startsWith(startString));
  const newarr = newArr.map((value) => value.replace(startString, ''))
  return newarr.join('-');
}
