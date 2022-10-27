$("#contact-form").submit(function(e)
{
    console.log(e);
    $.ajax({
                  data: $(this).serialize(), // получаяем данные формы
                  url: submit_url,
                  type: "POST",
                  // если успешно, то
                  success: function (response) {
                        $(".u-form-send-success").show();
                  },
                  // если ошибка, то
                  error: function (response) {
                      // предупредим об ошибке
                      $(".u-form-send-error").show();
                  }
              });
    return false;
});
