$("#newuser").on('click',function(){
	$("#newUser").modal('show');
});

$("#username").on('input',function(){
	var uname = this.value;
	$.ajax({
		url: "/expenses/checkuser/",
		type : "POST",
		data : {uname:uname},
		success : function(response){
			if(response.count == 0){
				$("#userres").html('<h5 style = "color:green">*Username Available</h5>');
				$("#createaccount").prop('disabled',false);
			}
			else{
			$("#userres").html('<h5 style="color:red">*Username Unavailable, type other username</h5>');
			$("#createaccount").prop('disabled',true);
			}
		}

	});
});