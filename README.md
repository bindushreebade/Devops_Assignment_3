Flask API and Form Handling Application

Program Explanation

This project is a Flask-based web application that performs two main tasks:

API Route (`/api`)

The application defines a route `/api` which returns data in JSON format.

1. How it works:
- A file named `data.json` is used to store data.
- When the `/api` route is accessed:
  1. The application opens the `data.json` file.
  2. It reads the data using Python's `json.load()` function.
  3. The data is converted into a proper JSON response using `jsonify()`.
  4. The JSON data is displayed in the browser.

2. Purpose:
This demonstrates how backend data can be served as an API.

3. Form Submission

The application provides a frontend form where users can enter details such as name and email.

4. How it works:
- The form is created using HTML (`form.html`).
- When the user submits the form:
  1. A POST request is sent to the `/submit` route.
  2. The backend retrieves the data using `request.form`.
  3. The data is processed and stored.

5. Data Storage

Depending on implementation, data is stored in:

Option A: JSON File
- Existing data is read from `data.json`.
- New user data is appended to the list.
- The updated data is written back to the file using `json.dump()`.

Option B: MongoDB Atlas
- A connection is established using `MongoClient`.
- User data is inserted into a collection using `insert_one()`.
- The database stores all submitted entries.

6. Success and Error Handling

### Success Case:
- If data is stored successfully:
  - The user is redirected to `/success`.
  - A message "Data submitted successfully" is displayed.

### Error Case:
- If an error occurs:
  - The same form page is shown again.
  - The error message is displayed to the user.

7. Overall Flow

1. User opens the application.
2. User fills and submits the form.
3. Backend receives the data.
4. Data is stored (JSON or MongoDB).
5. User is redirected to success page OR shown an error.

8. Conclusion

This program demonstrates:
- Creating API routes using Flask
- Reading and returning JSON data
- Handling form submissions
- Storing data in backend (file/database)
- Implementing success and error handling