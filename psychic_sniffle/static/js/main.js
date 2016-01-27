$('.create_bookmark').on('click', function(){
	var place_id = $(this).data('place_id');
	$.get(
		'/profiles/bookmarks/add/',
		{place_id: place_id}
	).done(function(resp){
		alert(resp.message);
	})
});