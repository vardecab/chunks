// https://marketingexamples.com/seo/performance

window.addEventListener(
	"scroll",
	() =>
		setTimeout(() => {
			// load marketing scripts like Intercom, Segment
		}, 1000),
	{ once: true }
);