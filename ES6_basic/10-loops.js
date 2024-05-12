export default function appendToEachArrayValue(array, appendString) {
    const newArray = [];
    for (const idx of array) {
        let value = idx;
        newArray.push(appendString + value);
    }

    return array;
}
