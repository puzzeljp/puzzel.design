#!/usr/bin/perl
#サーバによっては上の一文を変更する必要があります。サーバ管理者にお尋ねください。
$ver = 3.50; #バージョン情報

#-----これ以下の著作者表示を変更しないでください-----
#
#ネットマニア　WEBアンケートシステムカスタマイズ版
#http://www.netmania.jp
#このスクリプトはフリーウェアです。
#このスクリプトの設定・設置・運用はスクリプト使用者の責任において行ってください。
#著作者表示を改変しないで下さい。
#カスタマイズ版の再配布は禁止します。

#-----スクリプト配布元--------------------------------
#[Web Qnaire 1]
#(C)narishin,2000-2004
#http://www.narishin.com

#-----設置方法----------------------------------------
#
#	enq.cgi		[755][707]	お使いのサーバーに合わせて変更
#	data.txt	[666][600]
#	jcode.pl	[644]
#	graph.gif	[644]
#


#※連続投票を禁止したい場合、229・230行目、先頭の「#」を取って下さい。



#----------------------
#初期設定
#---------------------- 


$mkazu = 10000;				#フリーメッセージ表示数(0:非表示)
$home='http://103.coxb.net/~x103/';	#ホームページ(帰り先、絶対パスで指定)
$mail='hitomi.s.akky@gmai.com';		#管理者メール
$pass='saku2';				#管理者用パスワード

$title='アンケート';	#タイトル

$iken='ご意見・ご感想をどうぞ(必須ではありません)';	#意見表示タイトル
$iken2='ご意見・ご感想';				#意見表示タイトル（結果）

$bgcolor='#ffffff';		#背景色
$bgimage='http://';		#背景画像

#説明文(タグも使用可能)
$subtitle='テンプレートの展示ページについてです。';

#----------------------
#初期設定２（特に変更の必要ナシ）
#---------------------- 

require './jcode.pl';		#日本語処理系(このファイルと同じディレクトリにおいてください)
$kanji='sjis';			#漢字変換方式(sjis(推奨)かjisかeuc)
$method='POST';			#メソッド形式(POST(推奨)かGET)
$lockkey = 0;			# ロック機構 (0:不使用 1:使用)
$lockfile = './lock';		# ロックファイル名
$script='./enq.cgi';		#スクリプト名(このファイルの名前)
$logfile='./data.txt';		#データファイル名(このファイルと同じディレクトリにおいてください)
$graphgif='graph.gif';		#グラフ用画像データ(絶対パスで指定)
$twidth='660';			#テーブルの幅
$twidth2='640';			#説明文テーブルの幅（上記テーブルより小さめに）
#以下スタイルシート
$style='

<!--

/***** default styles
*******************************************/

body {
	font-size: 13px;
	*font-size: small; /* IE7 */
	*font: x-small; /* IE6 */
}

* {line-height: 1.6;font-size: 100%;}


/***** text styles
*******************************************/

p {
	line-height: 1.9;
	text-align: justify;
	text-justify: distribute;

}

html {
	padding: 0;
	margin: 0;
}

body {
	text-align: center;
	color: #5D5D5D;
	margin:0 auto;
	padding:0;
	text-align:center;
	font-family: Verdana, Arial, "ヒラギノ角ゴ Pro W3", "ＭＳ Ｐゴシック", sans-serif;}


#out {
	width:700px;
	margin:10px auto;
	text-align:left;

}

p, ul, ol, dl, table, pre {
	font-size: 100%;
	letter-spacing: 0.02em;
}
ul {	list-style: none;margin: 20px 0 50px 5px;}

li {margin:0.5em 0}

img {
	border: 0;
	vertical-align: bottom;
}

form {margin:0;padding:0;}

a:link{
  color: #39399E;
  text-decoration: none;
  }
a:visited{
  color: #26266A;
  text-decoration: none;
  }
a:hover,a:active{
  color: #1939BD;
  text-decoration: underline;
  background: none;
  }


.foot {
	font-size: 82%;
	background-color:#EFEFEF;
	padding:10px 0;
	text-align:center;
}

h1 {font-size:120%;padding:3px 5px;margin:25px 0 10px 0;font-weight:normal;}
h2 {font-size:110%;border-left:3px solid #999999;border-bottom:1px solid #999999;padding:3px 10px;margin:10px 0 5px 0;}
h3 {font-size:110%;background-color:#EFEFEF;padding:5px 8px;margin:0 0 10px 0;text-align:left;}
h4 {font-size:100%;background-color:#EFEFEF;padding:3px 5px;margin:20px 0 10px 0;}

.head {
	border-top:1px solid #999999;
	padding:8px 0 0 0;margin:5px 0 20px 0;
	text-align:right;
}


.tab {
	font-weight: normal;
	font-size: 100%;
	margin:1em auto;
	border-collapse:collapse;
	border-top:1px solid #CECFCE;
	border-right:1px solid #CECFCE;

}

.tab2 {
	width:550px;
	font-weight: normal;
	font-size: 92%;
	margin:1em auto;
	border-collapse:collapse;
	border-top:1px solid #CECFCE;
	border-right:1px solid #CECFCE;

}

.tab3 {
	width:600px;
	font-weight: normal;
	font-size: 100%;
	margin:1em auto 20px auto;
	border-collapse:collapse;
	border-top:1px solid #999999;
	border-right:1px solid #999999;

}

.tab4 {
	width:600px;
	font-weight: normal;
	font-size: 100%;
	margin:1em auto 20px auto;
	border-collapse:collapse;
	border-top:1px solid #999999;
	border-right:1px solid #999999;

}

.tab5 {
	font-weight: normal;
	font-size: 92%;
	margin:1em auto;
	border-collapse:collapse;
	border-top:1px solid #CECFCE;
	border-right:1px solid #CECFCE;

}

.tab6 {
	font-weight: normal;
	font-size: 100%;
	margin:1em auto;
	border-collapse:collapse;
	border-top:1px solid #CECFCE;
	border-right:1px solid #CECFCE;

}

.tab th {padding:3px;font-weight:normal;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;background-color:#EFEFEF;width:120px;}
.tab td {padding:8px;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;}

.tab2 th {font-size:100%;padding:3px;font-weight:normal;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;background-color:#EFEFEF;width:250px;}
.tab2 td {font-size:100%;padding:2px;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;}
.tab3 td {font-size:100%;padding:2px 10px 2px 10px;;border-bottom:1px solid #999999;text-align:center;border-left:1px solid #999999;}
.tab3 th {font-size:92%;padding:2px 10px 2px 10px;border-bottom:1px solid #999999;border-left:1px solid #999999;text-align:left;font-weight:normal;background-color:#EFEFEF;}
.tab4 td {font-size:100%;padding:2px 10px 2px 10px;;border-bottom:1px solid #999999;text-align:left;border-left:1px solid #999999;}
.tab4 th {font-size:92%;padding:2px;border-bottom:1px solid #999999;border-left:1px solid #999999;text-align:center;font-weight:normal;}

.tab5 th {font-size:92%;padding:3px;font-weight:normal;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;background-color:#EFEFEF;width:200px;}
.tab5 td {font-size:92%;padding:8px;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;}

.tab6 th {padding:3px 0 3px 10px;font-weight:normal;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;background-color:#EFEFEF;width:140px;text-align:left;}
.tab6 td {padding:8px;border-bottom:1px solid #CECFCE;border-left:1px solid #CECFCE;}


.mes {border:1px solid #cccccc;padding:10px;margin:10px 0 0px 0;width:500px;}
.com {font-size:82%;margin:0 0 20px 10px;}

.error {border:1px solid #999999;padding:10px;margin:100px auto 50px auto;width:300px;background-color:#EFEFEF}
.erroe_mes {font-size:120%;padding:3px 5px;margin:20px 0 10px 0;font-weight:normal;}
.error_bottom {font-size:92%;margin: 0 0 15px 0;}
.admin {padding:10px;margin:50px auto;width:300px;}
.enq {width:95%;text-align:left;}
.sou {margin:20px 0 0 50px;border-left:3px solid #999999;padding:0 0 0 5px;text-align:left;}
.kanri_enq {border:1px solid #999999;padding:0 0 10px 0;margin:0 0 50px 0;}
.add {border:3px solid #999999;padding:0 0 10px 0;margin:0 0 50px 0;}
.back {font-size:110%;border:1px solid #999999;padding:3px;margin:20px 0;background-color:#EFEFEF;width:150px;}
-->

';

#----------------------------------
#メイン処理系
#----------------------------------
&decode;

if ($mode eq 'tohyo' || $mode eq 'kekka'){
	&tsuika;
}elsif($mode eq 'kanri'){
	&kanri;

}else {
	&tohyo;
}

#----------------------------------
#初期投票画面
#----------------------------------
sub tohyo{
	&head;

	print "<h1>$title</h1><div class=head>


\n";
	if ($home ne 'http://'){
		print "<a href=$home>ホームへ</a> | \n";
	}
	print "<a href=$script?mode=kekka>投票結果</a>\n";

print <<"EOM";
</div>
<script type="text/javascript"><!--
   location.href = "http://103.coxb.net/~x103/";
// --></script>

<center><div class=mes>$subtitle</div></center><br />
EOM

	print " 

<FORM action=\"$script\" method=\"$method\"> \n";

	open (IN,$logfile) || &error("ログファイルを開けません"); #データファイル読み込み
	@qset = <IN>;		#配列qsetにtohyo.logの各行が要素としてはいる
	close(IN);

	chop($qset[0]);
	$qkazu = $qset[0];
	for ($i=1;$i<=$qkazu;$i++){			#質問と選択肢の読み込み
		@qtemp=split( /,/,$qset[$i]);		#読み込んだ行を｢,｣で区切る
		print "\n<center><div class=enq><h2>$qtemp[0]</h2>\n




<ul>\n";	#問題文の表示
		if ($qtemp[3] =~ m/select/){		#プルダウン形式の選択肢
			print "<li><select name=$i>\n";
			print "<option value='none'>選択してください</option>\n";
		}
		for ($j=1;$j<=$qtemp[1];$j++){			#選択肢の表示
			($anstmp,$hyotmp)=split( /=/,$qtemp[$j+3]);	#選択肢と得票数を分ける
			if ($qtemp[3] =~ m/select/){		#プルダウン形式の選択肢
				print "<option value=$i/$j>$anstmp</option>\n";
			}else{
				$t_temp3 = $qtemp[3];
				$t_temp3 =~ s/=sort// , $t_temp3 =~ s/=sosu//;
				print "<li><input type=$t_temp3 name=$i value=$i/$j> $anstmp</li>\n";
			}
		}
		if ($qtemp[3] =~ m/select/){		#プルダウン形式の選択肢
			print "</select></li><br />\n\n";
		}
		if ($qtemp[2] eq 'yes'){			#選択肢の追加を尋ねる
			if ($qtemp[3] =~ m/select/){
				$tmpadd = 'checkbox';
			}else{
				$tmpadd = $qtemp[3];
				$tmpadd =~ s/=sort// , $tmpadd =~ s/=sosu//;
			}
			print "<li><input type=$tmpadd name=$i value=add>\n";
			print "その他 <input type=text size=30 name=add$i></li>\n";
		}
		print "</ul></div></center>\n";	
	}
	
	if ($mkazu > 0){
		print <<"EOM";



<center><div class=enq><h2>$iken</h2>
<ul><li>名前　<input type=text name=tname size="20"></li>
<li><textarea name=toko rows=5 cols=70></textarea></li></ul>
</div></center>
EOM
 
	}

	print <<"EOM";
<center>

<INPUT type="submit" value="　　　投票する　　　"><br><br>
ご協力ありがとうございました。
<input type="hidden" name="mode" value="tohyo"></CENTER></form>

EOM
	
	&foot;
}

#----------------------------------
#結果表示
#----------------------------------
sub tsuika{
	&lock if ($lockkey); 	# ロック開始

	open (IN,$logfile) || &error("ログファイルを開けません"); #データファイル読み込み
	@qset=<IN>;			#データを一行ごと配列qsetに入れる
	close (IN);

	chop(@qset);			#qsetの最後の改行を取り除く

	$lahost=$qset[$qset[0]+3];
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
	#if ($lahost eq $host && $mode eq 'tohyo') {
	#	&error("連続投票はできません。<br><br>(接続ホストを変えて投票を試してみてください)");}

	&head;				#ヘッダ出力
	&jikan(0);			#現時間読み込み


	print "<h1>投票状況</h1><div class=head>\n";
	if ($home ne 'http://'){
		print "<a href=$home>ホーム</a> | \n";
	}

	print "<a href=$script>アンケートへ戻る</a>\n";
	print "<BR>[$jikanl]現在の投票状況です。</div>\n";

	if ($mode eq 'tohyo'){
		print "

<center><div class=\"mes\">お答え頂きありがとうございました。</div></center>
\n";
		print "<br>\n\n";
	}



	$qkazu=$qset[0];
	$qset[0]="$qset[0]\n";
	for ($i=1;$i<=$qkazu;$i++){		#質問ごとの処理		
		@qtemp=split(/,/,$qset[$i]);	#行内データを｢,｣で分けて配列qtempに格納	
		$add = $in{"add$i"};	#追加する選択肢内容
		$tothyo = 0;		#質問別の総票数
		$maxhyo = 1;		#質問別の最高得票数
		for ($j=1;$j<=$qtemp[1];$j++){			#既存の選択肢への処理
			($anstmp[$j],$hyotmp[$j])=split(/=/,$qtemp[$j+3]);
			$done=0;
			foreach $x (@ans){		
				if ("$i/$j" eq $x){
					$hyotmp[$j]++,$done=1; #票数の追加
				}
			}
			if ($add eq $anstmp[$j] ){
				$add='';			#追加する選択肢が既存
				if ($done == 0 ){
					$hyotmp[$j]++;
				}
			}
			if ($hyotmp[$j] > $maxhyo){	#最高得票数の更新
				$maxhyo = $hyotmp[$j];
			}
			$qtemp[$j+3]="$anstmp[$j]=$hyotmp[$j]";	#更新データを格納
			$tothyo += $hyotmp[$j];			#質問ごと総票数更新
		}
		if ($in{$i} eq 'add' && $add ne ''){		#選択肢追加
			$qtemp[$j+3]="$add=1",$tothyo++;
			$anstmp[$j]=$add,$hyotmp[$j]=1,$qtemp[1]++,$j++;
		}

		#票数によるソート表示
		if ($qtemp[3] =~ m/sort/){
			$hyotmp[0] = 0; #ダミー
			@sizensu = ();
			for ($j=0;$j<$qtemp[1];$j++){
				$sizensu[$j] = $j + 1 ;
			}
			$j = 1;
			foreach (sort({$hyotmp[$b] <=> $hyotmp[$a]} @sizensu)){
				$h_anstmp[$j] = $anstmp[$_];
				$h_hyotmp[$j] = $hyotmp[$_];
				$j++;
			}
		}else{
			for ($j=1;$j<=$qtemp[1];$j++){
				$h_anstmp[$j] = $anstmp[$j];
				$h_hyotmp[$j] = $hyotmp[$j];
			}
		}				

		print "\n<h3>$qtemp[0]</h3>";		#質問文の表示
		if ($qtemp[3] =~ m/sosu/){
			print "\n<div class=sou>投票総数 $tothyo 票</div>";	#投票総数表示
		}
		print "\n<center><table class=tab4>";	#結果表示
		for ($j=1;$j<=$qtemp[1];$j++){
			$wari[$j]=0;	#票の割合
			$width = 0;	#グラフ画像表示幅
			print "\n<tr><td>$h_anstmp[$j]</td>";
			print "<th width=60 align=center>$h_hyotmp[$j] 票</th>";
			if ($qtemp[3] =~ m/radio/ || $qtemp[3] =~ m/select/){
				if ($tothyo>0) {
					$wari[$j]=sprintf("%.1f",$h_hyotmp[$j]*100/$tothyo);
				}
				$width = int ( 2 * $wari[$j] );
				print "<th align=center width=80>$wari[$j] %</th>";
			}else{
				if ($maxhyo > 0){
					$width = int(200*$h_hyotmp[$j]/$maxhyo);	
				}
			}
			print "<td width=200>";
			print "<img src=$graphgif height=8 width=$width></td></tr>\n";
		}
		print "</table></center>\n\n";
		push(@qtemp,"\n");		#行末に改行をつける
		$qset[$i]=join(",",@qtemp);	#行データを更新する
	}					#質問ごとの処理の終了

	#メッセージの処理
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
 
	@tnaiyo = split(/<br>/,$qset[$qkazu+1],$mkazu+1);
	if($in{'toko'} ne ''){			#メッセージ更新
		unshift (@tnaiyo,"<tr><th>$in{'tname'} ($jikanl)</th><td>$in{'toko'}</td>");
	} 
	splice (@tnaiyo,$mkazu);
	$qset[$qkazu+1] = join('',@tnaiyo);
	$qset[$qkazu+1] = "$qset[$qkazu+1]\n";

	if ($mkazu > 0){

		print "<h4>$iken2</h4>\n";
		print "<table class=tab5>\n";
		print "$qset[$qkazu+1]\n";	#メッセージ表示
		print "</table>\n";
	}

	if ($mode eq 'tohyo'){
 	$qset[$qkazu+2]="$jikanl \n";			#最終投票時間更新
	}else{
	$qset[$qkazu+2]="$qset[$qkazu+2]\n";
	}

	if ($mode eq 'tohyo'){
 	$qset[$qkazu+3]="$host\n";			#最終投票ホスト更新
	}else{
	$qset[$qkazu+3]="$qset[$qkazu+3]\n";
	}

	$qset[$qkazu+4]="$qset[$qkazu+4]\n";		#末データ処理
	$qset[$qkazu+5]="$qset[$qkazu+5]\n";		#末データ処理
	$qset[$qkazu+6]="$qset[$qkazu+6]\n";		#末データ処理
	$qset[$qkazu+7]="$qset[$qkazu+7]\n";		#末データ処理
	$qset[$qkazu+8]="$qset[$qkazu+8]\n";		#末データ処理

	#データファイル更新
	open (OUT,">$logfile") || &error("ログファイルを開けません");				
	print OUT @qset;
	close(OUT);
	
	&unlock if ($lockkey); # ロック解除
	
	print "<center><div class=back><a href=$script>アンケートに戻る</a></div></center>\n";
	&foot;					#フッタ表示
}

#----------------------------------
#管理者用
#----------------------------------
sub kanri{
	if ($in{'pass'} ne "$pass") {&error('管理者モード');}	

	&jikan(0);

	&head;
	print <<"EOM";

<h1>管理ページ</h1><div class=head><a href=$script>アンケート画面へ</a></div>

EOM

	&lock if ($lockkey); 	# ロック開始

	open (IN,$logfile) || &error("ログファイルを開けません"); #データファイル読み込み
	@qset=<IN>;			#データを一行ごと配列qsetに入れる
	close (IN);

	chop(@qset);			#qsetの最後の改行を取り除く

	print "\n";


	$qkazu=$qset[0];
	$qset[0]="$qset[0]\n";

	#質問の消去
	foreach $x (@delque){
		splice(@qset,$x,1);
		$qkazu--;
		$qset[0]="$qkazu\n";
	}

	#質問の追加
	if ($in{'addque'} ne ''){
		$qkazu++;
		$qset[0]="$qkazu\n";		#質問数の更新
		splice(@qset,1+$in{'ajun'},0,"$in{'addque'},0,$in{'aadd'},$in{'rc'},"); 
	}

	for ($i=1;$i<=$qkazu;$i++){		#質問ごとの処理		
		@qtemp=split(/,/,$qset[$i]);	#行内データを｢,｣で分けて配列qtempに格納	
		$add=$in{"add$i"},$tothyo=0;	

		if ($in{'qubunc'} eq $i){	#質問文の更新
			$qtemp[0] = $in{'qubun'};
		}		
		if ($in{'qtyc'} eq $i){		#回答方法の更新
			$qtemp[2] = $in{'aadd'};
			$qtemp[3] = $in{'rc'};
			if ($in{'sort'} && $qtemp[3] !~ m/sort/){
				$qtemp[3] .= '=sort';	#ソート有無の変更
			}elsif (!$in{'sort'}){
				$qtemp[3] =~ s/=sort//;
			}
			if ($in{'sosu'} && $qtemp[3] !~ m/sosu/){
				$qtemp[3] .= '=sosu';	#投票総数表示有無の変更
			}elsif (!$in{'sort'}){
				$qtemp[3] =~ s/=sosu//;
			}
		}		


		print "\n<div class=kanri_enq><center><h3>$qtemp[0]</h3>\n";		#質問文の表示
		print "
			<table class=\"tab\">
			<form action=$script method=$method>
			<input type=hidden name=mode value=kanri>
			<input type=hidden name=pass value=$pass>
			<input type=hidden name=k_mode value=bunhen>
			<input type=hidden name=qubunc value=$i>
			<tr>
			<th>質問文の変更</th>
			<td><input type=text size=70 name=qubun value='$qtemp[0]'></td>
			<td><input type=submit value='変更'></td>
			</tr>
			</form>
			
			<form action=$script method=$method>
			<input type=hidden name=mode value=kanri>
			<input type=hidden name=pass value=$pass>
			<input type=hidden name=$i value=add>
			<tr>
			<th>選択肢を追加</th>
			<td><input type=text size=70 name=add$i></td>
			<td><input type=submit value='追加'></td>
			</tr>
			</form>
			</table>


		\n";		#質問文の変更と追加



		for ($j=1;$j<=$qtemp[1];$j++){			#既存の選択肢への処理
			($anstmp[$j],$hyotmp[$j])=split(/=/,$qtemp[$j+3]);
			$done=0;

			if ($in{'qrset'} eq $i){
				$hyotmp[$j] = 0;	#票数をリセット
			}

			if ($add eq $anstmp[$j] ){
				$add='';			#追加する選択肢が既存
			}

			$qtemp[$j+3]="$anstmp[$j]=$hyotmp[$j]";	#更新データを格納
			$tothyo += $hyotmp[$j];			#質問ごと総票数更新

			foreach $x (@del){
				if ("$i/$j" eq $x && $chfl == 0){
					splice(@qtemp,$j+3,1);	#選択肢の除去
					$tothyo -= $hyotmp[$j];
					$hyotmp[$j]=0;
					$qtemp[1]--;
					$j--,$chfl=1;
				}
			}
		}

		if ($in{$i} eq 'add' && $add ne ''){		#選択肢追加
			$qtemp[$j+3]="$add=0";
			$anstmp[$j]=$add,$hyotmp[$j]=0,$qtemp[1]++,$j++;
		}

		print "<div class=sou>投票総数 $tothyo 票</div>";	#投票総数表示
		print "\n<table class=\"tab3\">";	#結果表示
		for ($j=1;$j<=$qtemp[1];$j++){
			$wari[$j]=0;
			if ($tothyo>0) {
				$wari[$j]=sprintf("%.1f",$hyotmp[$j]*100/$tothyo);
			}
			$width = int ( 3 * $wari[$j] );
			print "\n<tr><th>$anstmp[$j]</th>";
			print "<td align=center width=100>$hyotmp[$j] 票</td>";
			if ($qtemp[3] =~ m/radio/){
				print "<td align=center width=100>$wari[$j] %</td>";
			}

			print "<form action=$script method=$method><td align=center width=50>\n";
			print "\n";
			print "<input type=hidden name=mode value=kanri>\n";
			print "<input type=hidden name=pass value=$pass>\n";
			print "<input type=submit value='削除'>\n";
			print "<input type=hidden name=del value=$i/$j>\n";
			print "</td></form></tr>\n";
		}
		print "</table></center>\n\n";



		print "<center><form action=$script method=$method>\n";
		print "<input type=hidden name=mode value=kanri>\n";
		print "<input type=hidden name=pass value=$pass>\n";
		print "<input type=hidden name=qtyc value=$i>\n";
		print "<br>\n";
		if ($qtemp[3] =~ m/radio/){
			print " <select name=rc>
 <option value=radio selected>ラジオボタン</option>
 <option value=select>プルダウン</option>
 <option value=checkbox>複数回答チェック</option>
 </select>\n";



		}elsif($qtemp[3] =~ m/select/){
			print " <select name=rc>
 <option value=radio>ラジオボタン</option>
 <option value=select selected>プルダウン</option>
 <option value=checkbox>複数回答チェック</option>
 </select>\n";

		}else{
			print " <select name=rc>
 <option value=radio>ラジオボタン</option>
 <option value=select>プルダウン</option>
 <option value=checkbox selected>複数回答チェック</option>
 </select>\n";

		}
		if ($qtemp[2] eq 'yes'){
			print " <select name=aadd>
 <option value=yes selected>選択肢の追加を許可</option>
 <option value=no>選択肢の追加なし</option>
 </select>\n";

		}else{
			print " <select name=aadd>
 <option value=yes>選択肢の追加を許可</option>
 <option value=no selected>選択肢の追加なし</option>
 </select>\n";

		}
		if($qtemp[3] =~ m/sort/){
			print " <select name=sort>
 <option value=1 selected>票数順に並替え</option>
 <option value=0>提示順に\表\示</option>
 </select>\n";

		}else{
			print " <select name=sort>
 <option value=1>票数順に並替え</option>
 <option value=0 selected>提示順に\表\示</option>
 </select>\n";

		}
		if ($qtemp[3] =~ m/sosu/){
			print " <select name=sosu>
 <option value=1 selected>投票数を\表\示する</option>
 <option value=0>投票数を\表\示しない</option>
 </select>\n";

		}else{	
			print " <select name=sosu>
 <option value=1>投票数を\表\示する</option>
 <option value=0 selected>投票数を\表\示しない</option>
 </select>\n";

		}
		print "<input type=submit value='変更'>\n";
		print "</form>\n\n";

		print "<BR><table><tr>
<td width=100><form action=$script method=$method>\n";
		print "\n";
		print "<input type=hidden name=mode value=kanri>\n";
		print "<input type=hidden name=pass value=$pass>\n";
		print "<input type=hidden name=qrset value=$i>\n";
		print "<input type=submit value='票数リセット'>\n";

		print "</form></td>\n";

		print "<td><form action=$script method=$method>\n";
		print "<input type=hidden name=mode value=kanri>\n";
		print "<input type=hidden name=pass value=$pass>\n";
		print "<input type=submit value='この質問を削除する'>\n";
		if ($qtemp[1] == 0){	#この質問に選択肢がない場合
		print "<input type=hidden name=delque value=$i>\n";
		}else{			#この質問の選択肢が残っている場合
		print "<input type=hidden name=delque value=\"muko\">\n";
		}
		print "</form></td></table>\n";
		print "<br>質問を削除する場合はすべての選択肢を削除してから行ってください。</center></div>\n";


		push(@qtemp,"\n");		#行末に改行をつける
		$qset[$i]=join(",",@qtemp);	#行データを更新する
	}					#質問ごとの処理の終了









	print "<div class=add><form action=$script method=$method>\n";
	print "<h3>質問を追加する</h3>\n";
	print "\n";
	print "<input type=hidden name=mode value=kanri>\n";
	print "<input type=hidden name=pass value=$pass>\n";
	print "<input type=hidden name=k_mode value=bunadd>\n";
	print "<center><table class=tab6><tr><th>質問追加位置</th><td>\n";

	print "<select name=ajun>\n";
	if ($qkazu > 0){
	print "<option value=$qkazu>最後  ($qkazu番目の質問の後)</option>\n";
	}
	print "<option value=0>先頭</option>\n";
	for ($i=1;$i<=$qkazu-1;$i++){
		print "<option value=$i>$i番目の質問の後</option>\n";
	}
	print "</select> に追加</td></tr>\n";
	print "<tr><th>質問文</th><td>\n";
	print "<input type=text size=60 name=addque></td></tr>\n";
	print "<tr><th>選択形式</th><td>\n";
	print "<input type=radio name=rc value=radio checked>ラジオボタン\n";
	print "<input type=radio name=rc value=select>プルダウン\n";
	print "<input type=radio name=rc value=checkbox>複数回答チェックボックス</td></tr>\n";
	print "<tr><th>選択肢の追加</th><td>\n";

	print "<input type=radio name=aadd value=yes>許可する\n";
	print "<input type=radio name=aadd value=no checked>許可しない</td></tr>\n";
	print "<tr><th>並び替え</th><td>\n";

	print "<input type=radio name=sort value=1>票数順に並替える\n";
	print "<input type=radio name=sort value=0 checked>提示順に\表\示</td></tr>\n";
	print "<tr><th>投票数\表\示</th><td>\n";

	print "<input type=radio name=sosu value=1>投票数を\表\示する\n";
	print "<input type=radio name=sosu value=0 checked>投票数を\表\示しない</td></tr>\n";
	print "</table></center>\n";
	print "<center><input type=submit value='追加する'></center>\n";
	print "</form></div>\n\n";
	
	#メッセージの処理
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
 
	@tnaiyo = split(/<br>/,$qset[$qkazu+1],$mkazu+1);
	if($in{'toko'} ne ''){			#メッセージ更新



		unshift (@tnaiyo,"<tr><th>$in{'tname'} ($jikanl)</th><td>$in{'toko'}</td>");
	} 
	splice (@tnaiyo,$mkazu);
	
	if ($in{'todel'} ne ''){
		$tnaiyocp = $tnaiyo[$in{'todel'}-1];
		$tnaiyocp =~ tr/<> //d; 
		if ($tnaiyocp eq $in{'todelnai'}){
			splice (@tnaiyo,$in{'todel'}-1,1);	#投稿内容の削除
		}else{
			print "<font color=red>新規投稿がありました。確認してください。データ保護のため投稿を削除しません。</font>\n";
		}
	}
	$tnkazu = @tnaiyo;
	if ($mkazu > 0){
		print "\n";
		print "<h4>$iken2</h4>\n";
		print "<table class=tab5>\n";
		if ($tnkazu == 0){
			print "(現在 発言はありません)\n";
		}
	}
	for ($i=1;$i<=$tnkazu;$i++){

	print "$tnaiyo[$i-1]\n";	#メッセージ表示


	}

	$qset[$qkazu+1] = join('<br>',@tnaiyo);
	$qset[$qkazu+1] = "$qset[$qkazu+1]\n";
	$qset[$qkazu+2]="$qset[$qkazu+2]\n";
	$qset[$qkazu+3]="$qset[$qkazu+3]\n";		#末データ処理
	$qset[$qkazu+4]="$qset[$qkazu+4]\n";		#末データ処理
	$qset[$qkazu+5]="$qset[$qkazu+5]\n";		#末データ処理
	$qset[$qkazu+6]="$qset[$qkazu+6]\n";		#末データ処理
	$qset[$qkazu+7]="$qset[$qkazu+7]\n";		#末データ処理

		print "</table>\n";

	#データファイル更新
	open (OUT,">$logfile") || &error("ログファイルを開けません");				
	print OUT @qset;
	close(OUT);

	&unlock if ($lockkey); # ロック解除
	
	&foot;
}




#----------------------------------
#入力情報の解析
#----------------------------------
sub decode{
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }

	open (IN,"$logfile") || &error("ログファイルを開けません");
	@qset=<IN>;
	close (IN);

	chop($qset[0]);

	for($i=1;$i<=$qset[0];$i++){	#解答チェックのための配列
		$input[$i] = 0;
		$addc[$i] = 0;
	}

	@pairs = split(/&/, $buffer);	#入力データごとに分ける
	foreach $pair (@pairs) {
		($name,$value) = split(/=/, $pair);	#nameとvalueに分ける
		$value =~ tr/+/ /d;			#空白変換
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ tr/\n/\ /d; #改行拒否
		$value =~ tr/\n/ /d;			#改行拒否
		$value =~ s/,/&sbquo;/g;		#｢,｣拒否
		if ($in{'k_mode'} ne 'bunhen'){$value =~ s/=/&#61;/g;}#｢=｣拒否
		if ($in{'mode'} ne 'kanri'){$value =~ s/</&lt;/g;}#｢<｣拒否
		&jcode'convert(*value,"$kanji");	#漢字変換コード指定

		$in{$name} = $value;
			
		if ($name <= $qset[0] && $value ne 'none'){	#質問への解答を解析
			if( $value ne 'add'){
				push (@ans,$value);	#既存の選択肢への投票
				if ($addc[$name] == 0){ #選択肢追加情報無し
					$addc[$name] = 0;
				}
			}else{
				$addc[$name] = 1 ;	#選択肢の追加
			}
		$input[$name]=1;
		}
		if ($name > $qset[0]){ #回答しようとした質問がすでに削除済み
			&error('回答しようとした質問が削除されています。確認してください。');
		}

		if ($name eq 'del'){
			push (@del,$value);		#選択肢の削除
		}

		if ($name eq 'delque'){
			if ($value eq 'muko'){
			&error('消去したい質問の選択肢をすべて削除してから実行してください。<br><br>
(既にすべての選択肢が削除されている場合、1回 票数リセットを行ってみてください。)');
			}else{
			push (@delque,$value);		#質問の消去
			}
		}
	}

	if ($in{'mode'} eq 'tohyo'){			#回答情報の不備をチェック
		for ($i=1;$i<=$qset[0];$i++){
			if ($input[$i] != 1){
				&error("$i 番目の質問が未解答です");
			}
			if ($addc[$i] == 1 && $in{"add$i"} eq ''){
				&error("$i 番目の質問の選択肢に追加したい内容が書かれていません");
			}
		}
		if ($in{'tname'} eq '' && $in{'toko'} ne ''){
			&error('メッセージにお名前がありません');
		}
	}
	if ($in{'mode'} eq 'kanri'){			#回答情報の不備をチェック
		for ($i=1;$i<=$qset[0];$i++){
			if ($addc[$i] == 1 && $in{"add$i"} eq ''){
				&error("$i 番目の質問の選択肢に追加したい内容が書かれていません");
			}
		}
		if ($in{'k_mode'} eq 'bunadd' && $in{'addque'} eq ''){
			&error("追加する質問文に内容がありません");
		}	
	}
	$mode = $in{'mode'};
}

#----------------------------------
#時間読み込み
#----------------------------------
sub jikan{

	#更新履歴用
	($sec,$min,$hour,$mday,$mon,$year,) = localtime;
	$mon++;
	$mon = sprintf("%.2d",$mon);
	$mday = sprintf("%.2d",$mday);
	$hour = sprintf("%.2d",$hour);
	$min = sprintf("%.2d",$min);
	$sec = sprintf("%.2d",$sec);

	$year += 1900;

	$jikanl = "$year/$mon/$mday";

}	

#----------------------------------
#ヘッダ表示
#----------------------------------
sub head{
	print "Content-type: text/html\n";
	print "\n";
	print <<"EOM";
<html><head><title>$title</title>
<style type="text/css">$style</style></head>
<body>
<div id="out">
EOM

}

#----------------------------------
#フッタ表示
#----------------------------------
sub foot{
	print <<"EOM";
</div>
<DIV class=foot>ウェブアンケートシステム<a href=http://www.narishin.com>Web Qnaire 1</a> + <a href=http://www.netmania.jp>Netmania</a> | <a href=$script?mode=kanri>管理</a></div>
</body></html>
EOM
	exit;
}

#----------------------------------
#  ロック処理  
#----------------------------------
sub lock {
	local($retry, $mtime);

	# 1分以上古いロックは削除する
	if (-e $lockfile) {
		($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 60) { &unlock; }
	}
	# ロック処理
	$retry=5;
	while (!mkdir($lockfile, 0755)) {
		if (--$retry <= 0) { &error('LOCK is BUSY'); }
		sleep(1);
	}
	$lockflag=1;
}

#----------------------------------
#  ロック解除  
#----------------------------------
sub unlock {
	rmdir($lockfile);
	$lockflag=0;
}

#----------------------------------
#エラー処理
#----------------------------------
sub error{
	&unlock if ($lockflag); # ロック解除
	&jikan(0);

	print "Content-type: text/html\n";
	print "\n";
	print <<"EOM";
<html><head><title>$title</title>
<style type="text/css">$style</style></head>
<body>

<div class=error>

<div class=erroe_mes>$_[0]</div>
<div class=error_bottom>[<a href="javascript:history.back()">BACK</a>]</div>

</div>
<div class=admin><form action=\"$script\" method=\"$method\"><input type=hidden name=mode value=\"kanri\"><input type=password name=pass size=8> <input type=submit value=\"管理用\"></form></div>



EOM

	&foot;
}


