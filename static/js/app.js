
function goToPage(pageURL) {
	var page = pageURL[pageURL.length -1];
	console.log(page);
	location.href='/viewalltickets?page='+page;
}

