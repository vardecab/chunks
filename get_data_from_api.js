// how to use JSON API in JavaScript

const api_key = "";

// grab data from URL
fetch("https://airapi.airly.eu/v2/measurements/point?indexType=AIRLY_CAQI&lat=" + lat + "&lng=" + lng + "&apikey=" + api_key)

    // convert data to JSON
    .then(function (res) {
        return res.json();
    })

    // use the data stored in object to do whatever
    .then(function (data) {
        console.error(data); // debug: output everything stored in the object

        // 💨 air quality
        current_air_quality = data.current.indexes["0"].level;
    })