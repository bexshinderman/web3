var name;
$.get("/country", function(response){
    name = response.name;
    console.log(name);
});

