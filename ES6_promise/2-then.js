export default function handleResponseFromAPI(promise) {
  const body = { status: 200, body: 'success' };
  promise.then(() => {
    return body;
  })
    .catch((err) => {
      return err;
    })
    .finally(() => console.log('Got a response from the API'));
}