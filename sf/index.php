<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Sky Fine! - PHOTO SITE</title> 
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
<meta name="keywords" content="大判写真,素材,Photo,無料写真素材,写真素材,風景素材,空素材,夕焼け素材,x103,福地,無料素材"> 
<meta name="description" content="空/夕焼け/風景などの大判素材配布してます。"> 
<link rel="stylesheet" type="text/css" href="style.css" />
<link href="js/facebox/facebox.css" media="screen" rel="stylesheet" type="text/css" /> 
<!-- JavaScripts--> 
<script type="text/javascript" src="js/facebox/jquery.js"></script>
<script type="text/javascript" src="js/jq.js"></script> 
<script type="text/javascript" src="js/facebox/facebox.js"></script>
<script type="text/javascript" src="js/fade.js"></script>
</head>

<body>
<!--*ベース*-->
<div id="base">
<!--*ヘッダー*-->
<div id="header">
<h1><a href="./">sky fine!</a></h1>
</div>
<!--*メニュー*-->
<div id="menu">
<ul class="menu">
<li><a href="info">Information</a></li>
<li><a href="photos">Photos</a></li>
</ul>
</div>
<!--*メイン*-->
<div id="maincontent">
<div class="maincontents">
<h2>What's new.</h2>
<div class="content">
<dl>
<dt>1/3</dt>
<dd>Photo + 21</dd>
</dl>
</div>
</div>
	<div class="maincontents">
<h2>Photozou New Photo</h2>
<div class="content">
<?php
//フォト蔵の写真を表示する関数
function photozou($user_id,$limit){
//XMLデータ取得用ベースURL
$req = "http://api.photozou.jp/rest/photo_list_public?type=public&user_id=306994&limit=10";
//XMLファイルをパースし、オブジェクトに代入
$xml = simplexml_load_file($req)
 or die("XMLパースエラー");	
echo "";

//画像を表示
$ret = '<div class="image">';
foreach ($xml->info->photo as $photo){
$ret .= "<a rel=facebox href=".$photo->image_url.">";
$ret .= "<img src=".$photo->thumbnail_image_url." class=phz alt=".$photo->photo_title." />";
$ret .= "</a>";
}
$ret .= "</div>";
return $ret;
}
echo photozou($user_id,$limit);
?>
</div>
</div>
<!--*コンテンツ終わり*-->
</div>
<!--*フッタ*-->
<div class="footer">
Copyright (C) sky fine! All Rights Reserved.
</div>
<div class="none">
<!--shinobi1--> 
<script type="text/javascript" src="http://x5.ojaru.jp/ufo/059517600"></script> 
<noscript><a href="http://x5.ojaru.jp/bin/gg?059517600" target="_blank"> 
<img src="http://x5.ojaru.jp/bin/ll?059517600" border="0"></a><br> 
<span style="font-size:9px"><img style="margin:0;vertical-align:text-bottom;" src="http://img.shinobi.jp/tadaima/fj.gif" width="19" height="11"> <a href="http://weekly_hukuoka.rentalurl.net" target="_blank">ウィークリーマンション 福岡</a></span></noscript> 
<!--shinobi2--> 
<!-- FC2カウンター ここから --> 
<script language="JavaScript" type="text/javascript" src="http://counter1.fc2.com/counter.php?id=10157980"></script><noscript><img src="http://counter1.fc2.com/counter_img.php?id=10157980"><br><strong><a href="http://rentalserver.fc2.com/">格安レンタルサーバー</a></strong></noscript> 
<!-- FC2カウンター ここまで --> 
</div>

</div>
</body>
</html>
