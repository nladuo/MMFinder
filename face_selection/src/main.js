
const updateImageUrl = ()=> {
  $('#loading').css('display','block');

    $.ajax({
      type : "GET",
      url : "/api/get_face_url",
      dataType: 'json',
      async: true,
      success(data) {
        $('#loading').css('display', 'none');
        $('#mm').attr("src", "/mm_images/" + data.path);
        $('#mm_face').attr("src", "/mm_images/face-" + data.path);
      },
      error() {
        alert("error");
        $('#loading').css('display', 'none');
      }
    });
}

$(document).ready(()=>{
  updateImageUrl();
})