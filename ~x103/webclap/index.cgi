#!/usr/bin/perl

#=======================================================================================
#				 PatiPati System                                                   Script by HAL
#                                                                 Last Update 2007.08.15
#=======================================================================================
require 'preset.cgi';
require 'sub.pl';
require $jcode;
$cookie_name1 = 'patipati';
$cookie_name2 = 'patiinput';
$cook_yuko = $cook_yuko * 24;

if ($ENV{'REQUEST_METHOD'} eq "POST") {
	read(STDIN, $formdata, $ENV{'CONTENT_LENGTH'});
} else { $formdata = $ENV{'QUERY_STRING'}; }
@pairs = split(/&/,$formdata);
foreach $pair (@pairs) {
	($name, $value) = split(/=/, $pair);
	$value =~ tr/+/ /;
	$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$value =~ s/</&lt;/g;
	$value =~ s/>/&gt;/g;
	$value =~ s/\n//g;
	$value =~ s/\,//g;
	jcode::convert(\$value,"euc","sjis", "");
	$QUERY{$name} = $value;
}

#================================メイン処理=================================
	&get_cookie($cookie_name2);
	&get_cookie($cookie_name1);
	if($COOKIE{'f'} == 1){
		open(HTML,"$last_file") || die "ファイルオープンに失敗しました - design";
		@htmls = <HTML>;
		close(HTML);
	}else{
		$time_w = time();
		$QUERY{'pkai'}++;
		$hidden = "<input type=\"hidden\" name=\"pkai\" value=\"$QUERY{'pkai'}\">";
		$gn = &get_date($time_w);
		# 過去データ消去
			&del_logs;
		$gn = &get_date($time_w);
		$user_ipg = $ENV{'REMOTE_ADDR'};
		# crypt
			$ic = length($user_ipg) / 8;
			if(length($user_ipg) % 8 != 0){ $ic++; }
			$i = 0; $crypt_ip = "";
			while($i <= $ic){
				$keta = $i*8;
				$crypt_ip .= crypt(substr($user_ipg,$keta,8),$salt);
				$i++;
			}
		# ブラックリスト処理
			$bk_ck = 0;
			if($ip_ck == 1){
				open(BLT,"$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
				@blists = <BLT>;
				close(BLT);
			}
			foreach $bk(@blists){
				($n_ip,$c_ip) = split(/<>/,$bk);
				if($c_ip eq $crypt_ip){ $bk_ck = 1; last; }
			}
			
		if($ip_ck == 1 && $bk_ck == 1 && $ip_ck_msg ne ""){ &error("$ip_ck_msg"); }
		if($bk_ck == 0){
			$i = 1;
			while($i <= $sub_su){
				$wk = 'sub' .$i;
				if($QUERY{$wk} ne ""){
					$QUERY{$wk} =~ s/\r\n//g;
					$QUERY{$wk} =~ s/\r//g;
					$QUERY{$wk} =~ s/\n//g;
					$QUERY{'com'} .= "（$QUERY{$wk}）";
				}
				$i++;
			}
			$QUERY{'com'} =~ s/\r\n/\n/g;
			$QUERY{'com'} =~ s/\r/\n/g;
			$msg = $QUERY{'com'};
			$msgw = $msg;
			$msgw =~ tr/A-Z/a-z/;
			if($com_jisu != 0 && $com_jisu < length($msg)){ &error("送信できるメッセージは半角$com_jisu文字（全角の場合その半分）までです。"); }
			$ng_ck = 0;
			if($msg ne ""){
				foreach $ngw (@ngs){
					&jcode'convert(*ngw,'euc');
					$ngw =~ tr/A-Z/a-z/;
					if($ngw ne "" && index($msgw,$ngw) >= 0){ $ng_ck = 1; }
				}
			}
			if($ng_ck == 1 && $ng_ck_msg ne ""){ &error($ng_ck_msg); }
			elsif($ng_ck == 0){
				$QUERY{'com'} =~ s/\n/<br>/g;
				$log_file = $log_dir .$gw .'.' .$kakucho; # ログファイル
				# ロック開始
					if ($lockkey == 1) { &lock1; }
					elsif ($lockkey == 2) { &lock2; }
				if(!(-e $log_file)){ # ログファイルがない場合は生成
					open(OUT,">$log_file") || &error('FILE OPEN ERROR - log');
					print OUT "";
					close(OUT);
					chmod (0666,$log_file);
				}
				open(LOG,"$log_file") || &error('FILE OPEN ERROR - log');
				@logs = <LOG>;
				close(LOG);
				@news = ();
				$kaisu = 1;
				foreach (@logs) {
					($jikanw,$user_ipw,$kaisuw,$comw) = split("<>",$_);
					# crypt
						$ic = length($user_ipw) / 8;
						if(length($user_ipw) % 8 != 0){ $ic++; }
						$i = 0; $user_ipc = "";
						while($i <= $ic){
							$keta = $i*8;
							$user_ipc .= crypt(substr($user_ipw,$keta,8),$salt);
							$i++;
					}
					if($user_ipg eq $user_ipw && $jikanw eq $jikan){
						$kaisu = $kaisuw + 1;
						if($QUERY{'com'} ne ""){ $QUERY{'com'} = $comw ."<#>$QUERY{'com'}"; }
						else{ $QUERY{'com'} = $comw; }
					}else{ push(@news,$_); }
				}
				if($clap_su == 0 || $kaisu <= $clap_su){
					push(@news,"$jikan<>$user_ipg<>$kaisu<>$QUERY{'com'}<>\n");
					@sorted = sort { $a <=> $b } @news;
					open(OUT,">$log_file") || &error('FILE OPEN ERROR - log');
					print OUT @sorted;
					close(OUT);
				}
				&unlock; # ロック解除
				if($msg ne "" && $mail_ck == 1){ $msg .="\n"; &mail; }
			}
	  }
		$ifile = @location_files;
		if($locate_rand == 1){
			srand;
			$r = int(rand($ifile));
			$location_file = @location_files[$r];
		}elsif($locate_rand == 2){
			$i = $kaisu;
			$location_file = @location_files[$i-1];
			if($i >= $ifile){ $location_file = @location_files[$ifile-1]; }
		}else{
			$i = $QUERY{'pkai'};
			while($i > $ifile){ $i -= $ifile; }
			$location_file = @location_files[$i-1];
		}
		if($clap_su != 0 && $kaisu >= $clap_su){
			$cook="f<>1";
			&set_cookie($cookie_name1,$clap_kankaku,$cook);
			open(HTML,"$last_file") || die "ファイルオープンに失敗しました - design";
			@htmls = <HTML>;
			close(HTML);
		}else{
			open(HTML,"$location_file") || die "ファイルオープンに失敗しました - design";
			@htmls = <HTML>;
			close(HTML);
		}
	}
	$html = "";
	foreach (@htmls) { $html .= $_; }
	$html =~ s/<!--cgi-->/$cgi_file/g;
	$html =~ s/<!--hidden-->/$hidden/g;
	$i = 1; $cook = "";
	while($i <= $sub_su){
		$wk = 'sub' .$i;
		if($QUERY{$wk} ne ""){
			my $wk2 = $QUERY{$wk};
			$wk2 =~ s/\r\n/\n/g;
			$wk2 =~ s/\r/\n/g;
			jcode::convert(\$wk2,"sjis");
			$cook .= "$wk<>$wk2,";
		}else{ $cook .= "$wk<>$COOKIE{$wk},"; }
		$html =~ s/<!--$wk-->/$COOKIE{$wk}/g;
		$i++;
	}
	&set_cookie($cookie_name2,$cook_yuko,$cook);
	$html =~ s/<!--clap_su-->/$clap_su/g;
	$html =~ s/<!--clap_kankaku-->/$clap_kankaku/g;
	$html =~ s/<!--moji_hmax-->/$com_jisu/g;
	$moji_zmax = int($com_jisu / 2);
	$html =~ s/<!--moji_zmax-->/$moji_zmax/g;
	$msg =~ s/\n/<br>/g;
	&jcode'convert(*msg,'sjis');
	$html =~ s/<!--view_msg-->/$msg/g;
	$html =~ s/<!--system-->/$systeminfo/g;
	print "Content-Type: text/html\n\n";
	print $html;
	exit;

#================================メール転送処理=================================
sub mail{
	&jcode'convert(*subject,'jis');
	&jcode'convert(*msg,'jis');

	foreach $mlw (@mailtos){
		$mailtow = $mlw;
		if (!open(MAIL,"| $sendmail $mailtow")) { &error('何らかの原因で送信できませんでした。'); }
			print MAIL "X-Mailer: GNBSys\n";
			print MAIL "To: $mailtow\n";
			print MAIL "From: $mailtow\n";
			print MAIL "Subject: $subject\n";
			print MAIL "Content-Transfer-Encoding: 7bit\n";
			print MAIL "Content-Type: text/plain\; charset=\"ISO-2022-JP\"\n\n";
			print MAIL "$msg";
			close(MAIL);
	}
}

#===============================クッキーの取得===========================
sub get_cookie{
	my $cookie_name = $_[0];
	@pairs = split(/\;/, $ENV{'HTTP_COOKIE'});
	foreach $pair (@pairs) {
		local($name, $value) = split(/\=/, $pair);
		$name =~ s/ //g;
		$DUMMY{$name} = $value;
	}
	@pairs = split(/\,/, $DUMMY{$cookie_name});
	foreach $pair (@pairs) {
		local($name, $value) = split(/<>/, $pair);
		$COOKIE{$name} = $value;
	}
}

#===============================クッキーの発行===========================
sub set_cookie{
	my $cookie_name = $_[0];
	my $cookie_time = $_[1];
	my $cook = $_[2];
	($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$dmy,$dmy)
					 	= gmtime(time + 60*60*$cookie_time);
	$yearg += 1900;
	if ($secg  < 10) { $secg  = "0$secg";  }
	if ($ming  < 10) { $ming  = "0$ming";  }
	if ($hourg < 10) { $hourg = "0$hourg"; }
	if ($mdayg < 10) { $mdayg = "0$mdayg"; }

	$month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')[$mong];
	$youbi = ('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')[$wdayg];
	$date_gmt = "$youbi, $mdayg\-$month\-$yearg $hourg:$ming:$secg GMT";
	print "Set-Cookie: $cookie_name=$cook; expires=\"$date_gmt\"\n";
}
