function get_json(ele, url) {
    window.onload = $(document).ready(function () {
        let data = $.getJSON(url, function (data) {
            return data
        });

        data.then(function (data, textStatus, jqxhr) {
            document.getElementById(ele).getElementsByClassName("json")[0].innerHTML = jqxhr.responseText;
        })
    })
}