if (!("Notification" in window)) {
	console.error("This browser does not support desktop notifications.");
}

// Let's check whether notification permissions have already been granted
else if (Notification.permission === "granted") {
	// If it's okay let's create a notification
	var notification = new Notification("notification title", {
		icon: "./path",
		body: "body text"
	});
}

// Otherwise, we need to ask the user for permission
else if (Notification.permission !== "denied") {
	Notification.requestPermission().then(function(permission) {
		// If the user accepts, let's create a notification
		if (permission === "granted") {
			var notification = new Notification("notification title", {
				icon: "./path",
				body: "body text"
			});
		}
	});
}
