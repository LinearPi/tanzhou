$(function() {
	var baseurl="https://tzdata.shiguangkey.com";
	String.prototype.replaceAll = function(s1,s2){
	　　	return this.replace(new RegExp(s1,"gm"),s2);
　　	}

	function getCookie(name) {
		var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
		if(arr = document.cookie.match(reg)) {
			return unescape(arr[2]);
		} else {
			return null;
		}
	}
	
	function setCookie(name, value) {
		var Days = 365;
		var exp = new Date();
		exp.setTime(exp.getTime() + Days * 24 * 60 * 60 * 1000);
		document.cookie = name + "=" + escape(value) + ";expires=" + exp.toGMTString();
	}
	
	function track(){
		var options=[];
		options=window.location.pathname.split('/');
		
		//if(!window.location.search)return; 
		if(window.location.search){
			var params=window.location.search.split('&');
			for(var i=0;i<params.length;i++){
				if(params[i].indexOf('=')){
					options.push(params[i].split('=')[1]);
				}
			}
		}
				
		options[0]=encodeURIComponent(window.location.href);
		
		var body="type="+location.hostname;
		var ga = getCookie('_ga');
		var token = getCookie('token');
		if(token)body+="&token="+token;
		if(ga)body+="&ga="+ga;
		for(var i=1;i<options.length+1;i++){
			if(i>9)break;
			if(body!="")body+="&";
			body+="col"+i+"="+options[i-1];
		}
	
	
		/*$.ajax({
			type:"get",
			url:baseurl+'/data/saveSpreadWebLog.json?'+body,
			dataType: 'jsonp',
   			jsonp: 'callback',
		});*/
//		fetch(baseurl+'/data/saveSpreadWebLog.json?mode', {
//			method: 'POST',
//			mode: 'cors',
//			headers: {
//				"Content-Type": "application/x-www-form-urlencoded"
//			},
//			body: body
//		}).then(
//			function(response) {
//				if(response.status !== 200) {
//					
//					return;
//				}
//				response.json().then(function(data) {
//					
//				});
//			}
//		)
//		.catch(function(err) {
//			
//		});
	}

	track();
});