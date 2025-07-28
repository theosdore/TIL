## .Then
.then() is a method used with Promises in JavaScript.

```javascript
fetch('https://jsonplaceholder.typicode.com/posts/1')
  .then((response) => response.json())
  .then((json) => console.log(json));
```

1. fetch('https://jsonplaceholder.typicode.com/posts/1')

   - This line sends an HTTP GET request to the given URL.

   - The URL points to a public fake API called JSONPlaceholder, commonly used for testing.

   - It requests the post with ID 1.

2. .then((response) => response.json())

   - The fetch() function returns a Promise that resolves to a Response object.

   - This line converts the response (which is a stream) into a JavaScript object using .json().

   - The .json() method itself also returns a Promise.

3. .then((json) => console.log(json))

   - Once the JSON data is available, this line logs the parsed object to the browser console.


## Continue
: The continue statement is used inside loops (like for or while) to Skip the rest of the current loop iteration and move to the next iteration immediately.