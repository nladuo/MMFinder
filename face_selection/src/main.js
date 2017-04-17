var path;

const updateImageUrl = ()=> {
  $('#loading').css('display','block');

  $.ajax({
    type : "GET",
    url : "/api/get_face_url",
    dataType: 'json',
    async: true,
    success(data) {
      $('#loading').css('display', 'none');
      path = data.path
      $('#mm').attr("src", "/mm_images/" + data.path);
      $('#mm_face').attr("src", "/mm_images/face-" + data.path);
      let picHeight=$("#mm").height();
      $('.right-div').height(picHeight);
    },
    error() {
      alert("error");
      $('#loading').css('display', 'none');
    }
  });
}

const handleFace = (opt) => {
  $('#loading').css('display','block');
  $.ajax({
      type : "GET",
      url : "/api/handle_face",
      dataType: 'json',
      data: {path: path, opt: opt},
      async: true,
      success(data) {
        console.log(data);
        $('#loading').css('display', 'none');
        updateImageUrl();
      },
      error() {
        alert("error");
        $('#loading').css('display', 'none');
      }
    });
}


$(document).ready(()=>{
  updateImageUrl();

  $("#like_btn").click(()=>{
    handleFace("like");
  })

  $("#dislike_btn").click(()=>{
    handleFace("dislike");
  })

  $("#ignore_btn").click(()=>{
    handleFace("ignore");
  })
})