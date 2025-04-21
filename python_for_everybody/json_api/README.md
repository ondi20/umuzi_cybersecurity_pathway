## 📍 JSON API Plus Code Finder

This is a Python script that interacts with a web service to retrieve **Open Location Codes** (also known as **plus codes**) for user-specified locations. The API used is a simplified version of OpenStreetMap data provided for learning purposes as part of the [Python for Everybody](https://www.py4e.com) course.

---

### 🧠 Project Objective

The goal of this project is to:

- Accept a **location input** from the user.
- Call a **web-based API** with the location as a parameter.
- Retrieve and parse the **JSON response**.
- Extract and display the **plus code** of the location.

---

### 🔗 API Endpoint

The script connects to the following API:

```
http://py4e-data.dr-chuck.net/opengeo
```

This endpoint returns a subset of geolocation data in GeoJSON format, including plus codes.

---

### ⚙️ How It Works

1. The user is prompted to enter a location.
2. The script sends a request to the API using the `q` query parameter.
3. It parses the returned JSON data.
4. It extracts and displays the first matching `plus_code`.

---

### 💡 Example Usage

```bash
$ python solution.py
Enter location: South Federal University
Retrieving http://py4e-data.dr-chuck.net/opengeo?q=South+Federal+University
Retrieved 1290 characters
Plus code 6FV8QPRJ+VQ
```

---

### 📁 File Structure

```
opengeo.py     # Main Python script
README.md       # Project description and usage guide
```

---

### 🧪 Test Locations

Try the following test input to validate your script:

- **Beloit College** → Should return a plus code starting with `86JGG`

---

### 🛠 Dependencies

- Python 3.x
- Standard libraries: `urllib`, `json`

> No external packages are required.

---

### 🙌 Acknowledgments

This project is inspired by **Dr. Charles Severance's** "Python for Everybody" course and uses data adapted from **OpenStreetMap** under the [Open Database License (ODbL)](https://opendatacommons.org/licenses/odbl/).