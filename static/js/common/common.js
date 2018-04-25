$(function () {
  //不同环境切换认证中心域名
  if (
    location.hostname == "https://www.shiguangkey.com/res/js/common/www.shiguangkey.com" ||
    location.hostname == "https://www.shiguangkey.com/res/js/common/shiguangkey.com"
  ) {
    //prod
    window.authUrl = "//auth2.shiguangkey.com/api";
  } else if (location.hostname == "https://www.shiguangkey.com/res/js/common/www-pre.shiguangkey.com") {
    //test
    window.authUrl = "//auth2-pre.shiguangkey.com/api";
  } else if (location.hostname == "https://www.shiguangkey.com/res/js/common/www-git-test.shiguangkey.com") {
    //test
    window.authUrl = "//auth2-git-test.shiguangkey.com/api";
  } else if (location.hostname == "https://www.shiguangkey.com/res/js/common/www-git-dev.shiguangkey.com") {
    //dev
    window.authUrl = "//auth2-git-dev.shiguangkey.com/api";
  } else {
    //my
    window.authUrl = "//auth2-git-dev.shiguangkey.com/api";
  }
  var urlQueryString = getUrlQueryString(window.location.search);
  if (urlQueryString.token) {
    var cookieToken = getCookie("token");
    if (cookieToken) {
      if (cookieToken == urlQueryString.token) {
        //token相同，不用重新登陆（判断是否需要隐藏URL中的token）
        //	 			if(urlQueryString.hideToken==="0"){
        //	 				reloadPage();
        //	 			}
        reloadPage();
        return;
      }
    }
    //写token登陆
    loginServer(urlQueryString.token, urlQueryString.hideToken != "0");
    //	 	if(urlQueryString.hideToken==="0"){
    //			reloadPage()
    //		}
  }
});
function loginServer(token, b) {
  setCookie("token", token, 24 * 30 * 6);
  $.ajax({
    url: "/api/auth/login?token=" + token,
    type: "POST",
    dataType: "json",
    success: function (data) {
      if (data.status == 0) {
        $.ajax({
          url: window.authUrl + "/login/save-token",
          type: "POST",
          data: {
            token: token
          },
          dataType: "jsonp",
          jsonp: "callback"
        });
        reloadPage();
      } else {
        logoutServer();
      }
    },
    error: function (data) {
      errorTip("服务器繁忙！");
    }
  });
}
function logoutServer(callback) {
  var params = {
    url: "/api/auth/logout",
    type: "GET",
    dataType: "json",
    success: function (data) {
      if (data.status == 0) {
        var params2 = {
          url: window.authUrl + "/login/ignore",
          type: "GET",
          dataType: "jsonp",
          jsonp: "callback",
          success: function () {
            if (data.status == 0) {
              delCookie("token");
            }
          }
        };
        $.ajax(params2);
        reloadPage();
      }
    }
  };
  $.ajax(params);
}
function errorTip(msg) {
  $(".loginerror-pro p").text(msg);
  $(".loginerror-pro").removeClass("none");
  $("#loginDiv").removeClass("none");
  setTimeout(function () {
    $(".loginerror-pro").addClass("none");
  }, 2000);
}
function reloadPage() {
  var reloadUrl = biteOffUrlParams("token", location.href);
  reloadUrl = biteOffUrlParams("hideToken", reloadUrl);
  var hashParams = "";
  /*if(reloadUrl.indexOf("#")!=-1){
		hashParams= reloadUrl.substring(reloadUrl.indexOf("#"));
		reloadUrl = reloadUrl.substring(0,reloadUrl.indexOf("#"));
		location.href=reloadUrl;
		location.href=reloadUrl+hashParams;
	}
	if(reloadUrl.indexOf("?")==reloadUrl.length-1){
		reloadUrl=reloadUrl.substring(0,reloadUrl.length-1);
	}
	if(reloadUrl.indexOf("&")==reloadUrl.length-1){
		reloadUrl=reloadUrl.substring(0,reloadUrl.length-1);
	}*/
  location.href = reloadUrl;
}
function biteOffUrlParams(name, url) {
  var result = "";
  var fromIndex = url.indexOf(name);
  var endIndex = url.indexOf("&", fromIndex);
  var tail = url.indexOf("#"); //是否有iframe子页面
  if (tail != -1) {
    if (fromIndex != -1 && endIndex != -1) {
      result =
        url.substring(0, fromIndex - 1) +
        url.substring(endIndex + 1) +
        url.substring(tail, url.length);
    } else if (fromIndex != -1 && endIndex == -1) {
      result =
        url.substring(0, fromIndex - 1) + url.substring(tail, url.length);
    } else {
      result = url;
    }
  } else {
    if (fromIndex != -1 && endIndex != -1) {
      result = url.substring(0, fromIndex - 1) + url.substring(endIndex + 1);
    } else if (fromIndex != -1 && endIndex == -1) {
      result = url.substring(0, fromIndex - 1);
    } else {
      result = url;
    }
  }
  return result;
}
function getUrlQueryString(url) {
  //从url中获取参数的对象
  var splitUrl = url.split("?");
  var strUrl = splitUrl.length > 1 ? splitUrl[1].split("&") : 0;
  var i = 0;
  var iLen = strUrl.length;
  var str = "";
  var obj = {};
  for (i = 0; i < iLen; i++) {
    str = strUrl[i].split("=");
    obj[str[0]] = str[1];
  }
  return Array.prototype.sort.call(obj);
}
function setCookie(name, value, expiresHours) {
  var cookieStr = name + "=" + encodeURIComponent(value);
  var date = new Date();
  date.setTime(date.getTime() + expiresHours * 3600 * 1000);
  cookieStr += ";expires=" + date.toUTCString() + ";path=/";
  document.cookie = cookieStr;
}
function getCookie(name) {
  var arr,
    reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
  if ((arr = document.cookie.match(reg))) {
    return unescape(arr[2]);
  } else {
    return null;
  }
}
function delCookie(name) {
  var date = new Date();
  date.setTime(date.getTime() - 10000);
  document.cookie = name + "= ;expires=" + date.toUTCString() + ";path=/";
}
