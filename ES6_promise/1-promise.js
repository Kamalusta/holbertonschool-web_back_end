export default function getFullResponseFromAPI(success) {
  const obj = {
    status: 200,
    body: 'Success'
  };
  if (success) {
    return Promise.resolve(obj);
  }
  else {
    return Promise.reject('The fake API is not working currently');
  }
}
