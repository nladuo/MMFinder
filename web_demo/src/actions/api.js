import $ from "jquery";

export default {
    get(url, data, _emit) {
        url = '/api' + url;

        $.ajax({
            type : "GET",
            url : url,
            dataType: 'json',
            data : data,
            async: true,
            success(data) {
                _emit(data);
            },
            error() {
                _emit(null);
            }
        });
    },

    post(url, data, _emit) {
        url = '/api' + url;

        $.ajax({
            type : "POST",
            url : url,
            dataType: 'json',
            data : data,
            async: true,
            success(data) {
                _emit(data);
            },
            error() {
                _emit(null);
            }
        });
    }
}
