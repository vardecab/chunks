// https://stackoverflow.com/questions/50941247/is-it-a-good-idea-to-lazy-load-gtm
// using jQuery - make sure it's loaded before this script fires

function loadGTM() {
	var GTM_ID = "GTM-########"; // change GTM_ID
	(function (w, d, s, l, i) {
		w[l] = w[l] || [];
		w[l].push({
			"gtm.start": new Date().getTime(),
			event: "gtm.js",
		});
		var f = d.getElementsByTagName(s)[0],
			j = d.createElement(s),
			dl = l != "dataLayer" ? "&l=" + l : "";
		j.async = true;
		j.src = "https://www.googletagmanager.com/gtm.js?id=" + i + dl;
		f.parentNode.insertBefore(j, f);
	})(window, document, "script", "dataLayer", GTM_ID); // change GTM_ID at the top
}
$(document).ready(loadGTM);