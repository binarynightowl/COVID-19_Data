function get_json(ele, url) {
    $(document).ready(function () {
        let data = $.getJSON(url, function (data) {
            return data
        });

        data.then(function (data, textStatus, jqxhr) {
            document.getElementById('test23').innerHTML = jqxhr.responseText;
        })
    })
}