//  NOTE: no longer working with newest UAC update

rows = document.querySelectorAll('.particle-table-row');
assets = [];
for (i=0; i < rows.length; i++) {
    try {
        name = rows[i].querySelectorAll('[essfield="segmentation_info"]')[0].firstChild.innerText;
    } catch (err) {
        name = rows[i].querySelectorAll('[essfield="feed_item_id"]')[0].firstChild.innerText
    }

    cost_per_conversion = rows[i].querySelectorAll('[essfield="stats.cost_per_conversion"]')[0].firstChild.innerText;
    cost = rows[i].querySelectorAll('[essfield="stats.cost"]')[0].firstChild.innerText;
    clicks = rows[i].querySelectorAll('[essfield="stats.clicks"]')[0].firstChild.innerText;
    impressions = rows[i].querySelectorAll('[essfield="stats.impressions"]')[0].firstChild.innerText;
    conversions = rows[i].querySelectorAll('[essfield="stats.conversions"]')[0].firstChild.innerText;
    cost = cost.replace(/($|£|€|,|)/gm, "");
    cost = cost.replace("GBP", "");
    clicks = clicks.replace(",", "");
    impressions = impressions.replace(",", "");
    conversions = conversions.replace(",", "");
    name = name.replace(/(\r\n|\n|\r)/gm," ");
    //name = name.replace("zip", "zip ")
    asset = [name, cost, clicks, impressions, conversions].join(";");

    assets.push(asset);
}
assets.join("\n");