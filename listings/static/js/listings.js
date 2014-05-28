/**
 * Created by mwalker on 23/05/2014.
 */
(function ($) {
    $(document).ready(function ($) {
        var duration = $('#id_duration');

        duration.change(function () {
            var end_date_field = $('#listing_form > div > fieldset > div.form-row.field-end_date > div > p'),
                d = $('#id_start_date_0').val().split("/"),
                t = $('#id_start_date_1').val().split(":"),
                months = this.options[this.selectedIndex].value,
                austDay = new Date(
                    parseInt(d[2], 10),
                    parseInt(d[1], 10) - 1,
                    parseInt(d[0], 10)
                );
            if (t[2]){
                var austDay = new Date(austDay.getFullYear(), austDay.getMonth(), austDay.getDate(), t[0], t[1], t[2]);
            } else {
                var austDay = new Date(austDay.getFullYear(), austDay.getMonth(), austDay.getDate(), t[0], t[1]);
            }

            austDay.setMonth(austDay.getMonth() + parseInt(months));
            $(end_date_field).text(austDay.toString('HH:mm d MMM yyyy'));
        });
    });
})(django.jQuery);