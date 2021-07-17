$(document).ready(function(){
  $('.likin').click(function(){
    $.ajax({
      'type':'POST',
      'url':'/',
      'data':{'content_id': $(this).attr('name'), 'operation':'like_submit','csrfmiddlewaretoken': '{{ csrf_token }}'},
      'datatype':'json',
      'success': function(response){
        selector = document.getElementsByName(response.content_id);
        if(response.liked == true ){
          $(selector).css("color","blue");
        }
        else if(response.liked == false){
          $(selector).css('color','black');
        }
      }
    })
  })
})