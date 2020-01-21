<script src="https://cdn.jsdelivr.net/npm/js-cookie@beta/dist/js.cookie.min.js"></script>

// set 🍪
Cookies.set("cookie_name", variable_to_store, {
	expires: 30, // for how many days we want to store it
	path: "/"
});

// get 🍪
someVariable = Cookies.get("cookie_name");
