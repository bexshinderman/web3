
var name;
$.get("/country", function(response){
name = response.name;
console.log(response);
});

$('#postCountry').click(function(){
var name = $('#countryName').val()
$.ajax({
  url: "/country",
  type:"POST",
  data:{name:name},
  
})
console.log(name)
});
