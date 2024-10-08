$(document).ready(function() {
    $('.star-icon').each(function() {
      $(this).hover(function() {
        $(this).prevAll().addBack().css("color", "#FFDF00");
      }, function() {
        if (!$(this).parent().attr("data-rating")) {
          $(this).prevAll().addBack().css("color", "lightgrey");
        } else {
          $(this).siblings().addBack().each(function(index) {
            index + 1 <= $(this).parent().attr("data-rating") ? 
              $(this).css("color", "#FFDF00") : $(this).css("color", "lightgrey");
          });
        }
      }).click(function () {
        $(this).parent().attr("data-rating", $(this).prevAll().length + 1);
      });
    });
  });