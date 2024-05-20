export default function handleResponseFromAPI(promise) {
  promise.then(() => {
    return {
      status: 200,
      body: 'success',
    };
  })
    .catch((err) => {
      return new Error;
    })
  console.log("Got a response from the API");
}