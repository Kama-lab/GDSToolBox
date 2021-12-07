$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});


$('#text-form').on('submit', function(event){
    event.preventDefault();
    console.log("form submitted!")  // sanity check
    process();
});


// AJAX for posting
function process() {
     // sanity check
    $.ajax({
      url:'process',
      type: 'GET',
      data: {
        the_get: $("#textarea").val(),
        input_type: $('input[name="select"]:checked').attr('id')
      },
      beforeSend: function() {
        $("#loader").css("display","block")
      },
      success: function(json) {
        $("#textarea").val('');
        console.log(json);
        console.log("success");
        $("#output_text").html(json.output_text);
      },
      error: function(xhr,errmsg,err) {
        console.log(xhr.status + ":" + xhr.responseText);
      },
      complete: function() {
        $("#loader").css("display","none")
      }
    })
    // .then(function() {
    //   $("#clipboard").attr('disabled',null);
    // })
    ;
};

//document.getElementById("clipboard").addEventListener("onclick",copyToClipboard);

function copyToClipboard(){
    var $temp = $("<textarea />");
    $("body").append($temp);
    $temp.val($("#textarea").val()).select();
    var result = false;
    try {
        result = document.execCommand("copy");
    } catch (err) {
        console.log("Copy error: " + err);
    }
    $temp.remove();
  }



  const toggleSwitch = document.querySelector('.switch input[type="checkbox"]');

  function switchTheme(e) {
      if (e.target.checked) {
          document.documentElement.setAttribute('data-theme', 'dark');
          localStorage.setItem('theme', 'dark');
      }
      else {
          document.documentElement.setAttribute('data-theme', 'light');
          localStorage.setItem('theme', 'light');
      }
  }

  toggleSwitch.addEventListener('change', switchTheme, false);


  const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

  if (currentTheme) {
      document.documentElement.setAttribute('data-theme', currentTheme);

      if (currentTheme === 'dark') {
          toggleSwitch.checked = true;
      }
  }
