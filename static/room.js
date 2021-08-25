$(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/send',
      data:{
          username:$('#username').val(),
          room_id:$('#room_id').val(),
          message:$('.form-control').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data){
        //  alert(data)
      }
    });
    document.getElementsByClassName('form-control')[0].value = ''
});

