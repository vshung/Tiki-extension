var CURRENT_URL = window.location.toString()
let PATTERN = /-p\w*\./i
var p_id = CURRENT_URL.match(PATTERN)

try{
	var product_id = p_id[0];
	product_id = product_id.substr(1).slice(0, -1);
	product_id = product_id.substr(1);

	iframe_url = 'http://127.0.0.1:5000/c/' + product_id

	var wrapper = document.createElement('div');
	wrapper.id = 'ssg-chart-wrapper';
	wrapper.setAttribute("style", "background: rgb(255, 255, 255); padding: 10px; overflow: unset; position: relative; z-index: 1; clear: both; flex: 1 1 0%;")

	// đoạn này là code chèn cái iframe. đó, muốn chèn ở đâu cũng đc, chỉnh lại tí là đc, mà cứ để thế là đẹp r, giống bọn kia làm

	var iframe  = document.createElement ('iframe');
	iframe.width = '100%';
	iframe.height = '460';
	iframe.frameborder = 0;
	iframe.class = 'iframe';
	iframe.setAttribute("style", "border-style: inset; box-radius: 5px")
	iframe.src  = chrome.extension.getURL(iframe_url);


	$('.product-summary').after(wrapper);
	$('#ssg-chart-wrapper').prepend(iframe)
}
catch(err) {
  
}