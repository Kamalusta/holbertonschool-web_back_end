export default async function getFullResponseFromAPI(success) {
  const obj = {
    status: 200,
    body: 'Success'
  };
  if (success) {
    return obj;
  }
  else {
    throw 'The fake API is not working currently';
  }
}
