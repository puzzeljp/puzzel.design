#!/usr/bin/perl

#=======================================================================================
#				 PatiPati System                                                   Script by HAL
#                                                                 Last Update 2007.02.28
#=======================================================================================
require 'preset.cgi';
require 'sub.pl';
require $jcode;
$cgi_file = 'view.cgi';
$cookie_name = 'patipatiview';

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
	$QUERY{$name} = $value;
}

# ���å�����ǽ�Υ����å�
&get_adcookie;
$passw = $COOKIE{'pass'};

if($QUERY{'passwd'} ne ""){ $passw = $QUERY{'passwd'}; }

if($passw ne $admin_pass){
	print "Content-Type: text/html\n\n";
	print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
	print <<"EOM";
<html>
<head><title></title>
<center>
	<form action="$cgi_file" method="post">
	Password <input type="password" name="passwd" size="10">
	<input type="submit" value="login">
	</form>
	</center>
</body></html>
EOM
	exit;
}

$cook="pass<>$passw";
&set_adcookie("60",$cook);

$time_w = time();
$gw = &get_date($time_w);

if($QUERY{'mode'} eq "menu"){ &menu; }
elsif($QUERY{'mode'} eq "view"){ &view; }
elsif($QUERY{'mode'} eq "bin"){ &bin; }
elsif($QUERY{'mode'} eq "bout"){ &bout; }
elsif($QUERY{'mode'} eq "blist"){ &blist; }
elsif($QUERY{'mode'} eq 'logout') { &logout; }
else{ &html; }

#===============================ɽ��HTML�ɥ�����Ȥ�����===========================
sub html {
	# ���ǡ����õ�
		&del_logs;

	print "Content-Type: text/html\n\n";
	print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
	print <<"EOM";
		<html>
		<head><title>PATIPATI LOG</title></head>

		<frameset cols="130,*" frameborder="NO" border="0" framespacing="0">
		  <frame src="$cgi_file?mode=menu" name="patimenu" scrolling="YES" noresize>
		  <frame src="$cgi_file?mode=view" name="patiview">
		</frameset>
		<noframes><body>
		</body></noframes>
		</html>
EOM
		exit;
}

#===============================ɽ��HTML�ɥ�����Ȥ�����===========================
sub menu {
	&log_shushu;
	# �ӥ塼��󥯺���
		$vlink = ""; $mlink = ""; $last_m = "";
		foreach (@wfilesw){
			($yymmw,$dmy) = split(/\./,$_);
			$ymw = substr($yymmw,0,4) .substr($yymmw,4,2);
			$ymw2 = substr($yymmw,0,4) .'/' .substr($yymmw,4,2);
			if($last_m != $ymw){
				$mlink .= "&nbsp;<a href=\"$cgi_file?mode=view&yymm=$ymw\">$ymw2</a><br>\n";
			}
			$ymw = substr($yymmw,0,4) .'/' .substr($yymmw,4,2) .'/' .substr($yymmw,6,2);
			$vlink .= "<a href=\"$cgi_file?mode=view&yymmdd=$yymmw\">$ymw</a><br>\n";
			$last_m = substr($yymmw,0,4) .substr($yymmw,4,2);
		}

	print "Content-Type: text/html\n\n";
	print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
	print <<"EOM";
		<html>
		<head><title>PATIPATI LOG</title>
		<meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
		<style type="text/css">
		<!--
		body, tr, td { font-size: 10pt; }
		small        { font-size: 8pt; }
		big          { font-size: 12pt; }
		A:link,A:visited,A:active {text-decoration:none;}
		A:link,A:active { color: #6699cc }
		A:visited { color: #336699 }
		A:hover { color: #999999 }
		input,textarea,select {            /* �ե������������  */
			font-size       :12px;             /* ʸ��������  */
			color           :#666666;          /*   ʸ����    */
			background-color:#eeeeee;          /*   �طʿ�    */
			border          :1 solid #999999; /* ������������*/ 
		}
		-->
		</style>
		<base target="patiview">
		</head>
		<body bgcolor="#ffffff" text="#666666">
		<a href="$cgi_file?mode=logout" target=\"_top\">&gt;&gt;��������</a><br><br>
		<a href="$cgi_file?mode=blist">&gt;&gt;�֥�å��ꥹ��</a><br><br>
		<b><font color="#990000">&lt;��ӥ塼&gt;</font></b><br>$mlink<br>
		<b><font color="#990000">&lt;����\ɽ\��&gt;</font></b><br>
		$vlink
		</body></html>
EOM
	exit;
}
#===============================ɽ��HTML�ɥ�����Ȥ�����===========================
sub view {
	if($hiritsu <= 0){ $hiritsu = 1; }
	if($view_pre == 1 && $QUERY{'yymmdd'} eq "" && $QUERY{'yymm'} eq ""){ $QUERY{'yymm'} = $nen .$tsuki; }
	elsif($QUERY{'yymmdd'} eq ""){ $QUERY{'yymmdd'} = $nen .$tsuki .$hi; }
	$now_date = substr($QUERY{'yymmdd'},0,4) .'/' .substr($QUERY{'yymmdd'},4,2) .'/' .substr($QUERY{'yymmdd'},6,2);
	$log_file = $log_dir .$QUERY{'yymmdd'} .'.' .$kakucho; # ���ե�����
	# �֥�å��ꥹ�ȥե������ɤ߹���
		open(BLT,"$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
		@blists = <BLT>;
		close(BLT);
	# �ǡ���ɽ��
		if($QUERY{'yymm'} ne ""){ # ��ǡ���ɽ��
			&log_shushu;
			$view_data = '
				<table cellspacing=1 cellpadding=4 border=0 bgcolor="#666666">
				<tr><td bgcolor="#eeeeee" align="middle" nowrap>����</td><td bgcolor="#eeeeee" align="middle" nowrap>�����</td><td bgcolor="#eeeeee" align="middle">������</td></tr>
			';
			$gokei = 0; @wks = ();
			foreach (@wfilesw){
				($yymmw,$dmy) = split(/\./,$_);
				$ymw = substr($yymmw,0,4) .substr($yymmw,4,2);
				if($QUERY{'yymm'} == $ymw){
					$now_date = substr($yymmw,0,4) .'/' .substr($yymmw,4,2);
					$dw = substr($yymmw,6,2);
					$ymd = $ymw .$dw;
					$log_filew = $log_dir .$ymd .'.' .$kakucho; # ���ե�����
					if(-e $log_filew){
						$comm = ""; $shokei = 0;
						open(LOG,"$log_filew") || &error('FILE OPEN ERROR - log');
						@logs = <LOG>;
						close(LOG);
						foreach (@logs) {
							($jikanw,$user_ipw,$kaisuw,$comw) = split("<>",$_);
							if($comw ne ""){
								@coms = split(/<#>/,$comw);
								# crypt
									$ic = length($user_ipw) / 8;
									if(length($user_ipw) % 8 != 0){ $ic++; }
									$i = 0; $user_ipc = "";
									while($i <= $ic){
										$keta = $i*8;
										$user_ipc .= crypt(substr($user_ipw,$keta,8),$salt);
										$i++;
									}
								foreach $cw (@coms){
									if($cw ne ""){
										if($ip_ck == 1){
											$bw = "<a href=\"$cgi_file?mode=bin&day=$ymd&ip=$user_ipc\">�֥�å��ꥹ�Ȥ�</a>";
											foreach $bk(@blists){
												($n_ip,$c_ip) = split(/<>/,$bk);
												if($c_ip eq $user_ipc){ $cw = "<font color=\"#ffffff\">$cw</font>"; $bw = "<b><font color=\"#cc3300\">BLACK!</font></b><a href=\"$cgi_file?mode=bout&ip=$user_ipc\">���</a>"; last; }
											}
											$cw .= " ��$bw";
										}
										$comm .= "$cw<hr noshade size=1>";
									}
								}
							}
							$shokei += $kaisuw;
							$gokei += $kaisuw;
							push(@wks,$kaisuw);
						}
					}
					if($comm ne ""){ $comm = substr($comm,0,-19); }
					$width = int($shokei / $hiritsu);
					$view_data .= "<tr bgcolor=\"#ffffff\" valign=\"top\"><td align=\"right\" nowrap><a href=\"$cgi_file?mode=view&yymmdd=$QUERY{'yymm'}$dw\">$dw��</a></td><td nowrap><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td><td>$comm&nbsp;</td></tr>\n";
				}
			}
			$view_data .= '</table>';
			if($gokei <= 0){ $view_data = '���Ϥ���ޤ���Ǥ�����'; }
			else{
				@wks = sort { $b <=> $a } @wks;
				$view_data .= '<br>Ϣ³��������<br>';
				$view_data .= '
					<table cellspacing=1 cellpadding=4 border=0 bgcolor="#666666">
					<tr><td bgcolor="#eeeeee" align="middle" nowrap>�����</td><td bgcolor="#eeeeee" align="middle">�Ϳ�</td></tr>
				';
				$shokei = 0; $last_data = "";
				foreach $kw (@wks) {
					if($last_data ne "" && $kw ne $last_data){
						$width = int($shokei / $hiritsu);
						$view_data .= "<tr bgcolor=\"#ffffff\"><td align=\"right\" nowrap>$last_data��&nbsp;</td><td><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td></tr>\n";
						$shokei = 0;
					}
					$shokei++;
					$last_data = $kw;
				}
			$width = int($shokei / $hiritsu);
			$view_data .= "<tr bgcolor=\"#ffffff\"><td align=\"right\" nowrap>$last_data��</td><td><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td></tr>\n";
			$view_data .= '</table>';
			}
		}
		else{ # ���ǡ���ɽ��
			if(-e $log_file){
				open(LOG,"$log_file") || &error('FILE OPEN ERROR - log');
				@logs = <LOG>;
				close(LOG);
			}
			$view_data = '
				<table cellspacing=1 cellpadding=4 border=0 bgcolor="#666666">
				<tr><td bgcolor="#eeeeee" align="middle" nowrap>����</td><td bgcolor="#eeeeee" align="middle" nowrap>�����</td><td bgcolor="#eeeeee" align="middle">������</td></tr>
			';
			$gokei = 0; $comm = ""; $last_time = ""; $shokei = 0; @wks = ();
			foreach (@logs) {
				($jikanw,$user_ipw,$kaisuw,$comw) = split("<>",$_);
				if($last_time ne "" && $jikanw ne $last_time){
					if($comm ne ""){ $comm = substr($comm,0,-19); }
					$width = int($shokei / $hiritsu);
					$view_data .= "<tr bgcolor=\"#ffffff\" valign=\"top\"><td align=\"right\" nowrap>$last_time��</td><td nowrap><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td><td>$comm&nbsp;</td></tr>\n";
					$comm = ""; $last_time = ""; $shokei = 0;
				}
				if($comw ne ""){
					@coms = split(/<#>/,$comw);
					foreach $cw (@coms){
						if($cw ne ""){
							if($ip_ck == 1){
								# crypt
									$ic = length($user_ipw) / 8;
									if(length($user_ipw) % 8 != 0){ $ic++; }
									$i = 0; $user_ipc = "";
									while($i <= $ic){
										$keta = $i*8;
										$user_ipc .= crypt(substr($user_ipw,$keta,8),$salt);
										$i++;
									}
								$bw = "<a href=\"$cgi_file?mode=bin&day=$QUERY{'yymmdd'}&ip=$user_ipc\">�֥�å��ꥹ�Ȥ�</a>";
								foreach $bk(@blists){
									($n_ip,$c_ip) = split(/<>/,$bk);
									if($c_ip eq $user_ipc){ $cw = "<font color=\"#ffffff\">$cw</font>"; $bw = "<b><font color=\"#cc3300\">BLACK!</font></b><a href=\"$cgi_file?mode=bout&ip=$user_ipc\">���</a>"; last; }
								}
								$cw .= " ��$bw";
							}
							$comm .= "$cw<hr noshade size=1>";
						}
					}
				}
				$shokei += $kaisuw;
				$gokei += $kaisuw;
				$last_time = $jikanw;
				push(@wks,$kaisuw);
			}
			if($comm ne ""){ $comm = substr($comm,0,-19); }
			$width = int($shokei / $hiritsu);
			$view_data .= "<tr bgcolor=\"#ffffff\" valign=\"top\"><td align=\"right\" nowrap>$last_time��</td><td nowrap><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td><td>$comm&nbsp;</td></tr>\n";
			$view_data .= '</table>';
			if($gokei <= 0){ $view_data = '���Ϥ���ޤ���Ǥ�����'; }
			else{
				@wks = sort { $b <=> $a } @wks;
				$view_data .= '<br>Ϣ³��������<br>';
				$view_data .= '
					<table cellspacing=1 cellpadding=4 border=0 bgcolor="#666666">
					<tr><td bgcolor="#eeeeee" align="middle" nowrap>�����</td><td bgcolor="#eeeeee" align="middle">�Ϳ�</td></tr>
				';
				$shokei = 0; $last_data = "";
				foreach $kw (@wks) {
					if($last_data ne "" && $kw ne $last_data){
						$width = int($shokei / $hiritsu);
						$view_data .= "<tr bgcolor=\"#ffffff\"><td align=\"right\" nowrap>$last_data��</td><td><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td></tr>\n";
						$shokei = 0;
					}
					$shokei++;
					$last_data = $kw;
				}
			$width = int($shokei / $hiritsu);
			$view_data .= "<tr bgcolor=\"#ffffff\"><td align=\"right\" nowrap>$last_data��</td><td><img src=\"$graph\" height=\"12\" width=\"$width\">&nbsp;$shokei��</td></tr>\n";
			$view_data .= '</table>';
			}
		}

	print "Content-Type: text/html\n\n";
	print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
	print <<"EOM";
		<html>
		<head><title>PATIPATI LOG</title>
		<meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
		<style type="text/css">
		<!--
		body, tr, td { font-size: 10pt; }
		small        { font-size: 8pt; }
		big          { font-size: 12pt; }
		A:link,A:visited,A:active {text-decoration:none;}
		A:link,A:active { color: #6699cc }
		A:visited { color: #336699 }
		A:hover { color: #999999 }
		input,textarea,select {            /* �ե������������  */
			font-size       :12px;             /* ʸ��������  */
			color           :#666666;          /*   ʸ����    */
			background-color:#eeeeee;          /*   �طʿ�    */
			border          :1 solid #999999; /* ������������*/ 
		}
		-->
		</style>
		<base target="patiview">
		</head>
		<body bgcolor="#ffffff" text="#666666">
		$now_date ����ס�<big><b>$gokei</b>��</big>
		<hr noshade size=1>
		$view_data
		<hr noshade size=1>- $systeminfo -
		</body></html>
EOM
	exit;
}

#===============================���ե��������===========================
sub log_shushu{
	if($shell_use == 1){
		$time_w2 = $time_w - 60*60*24*30*$log_max;
		$dayw = $time_w;
		@wfiles = ();
		while($dayw >= $time_w2){
			$wk = &get_date($dayw);
			$wk = substr($wk,0,8) .'.' .$kakucho;
			$fck = $log_dir .$wk;
			if(-e $fck){ push(@wfiles,$wk); }
			$dayw -= 60*60*24;
		}
	}else{
		@files = glob("$log_dir*");
		$i = @files;
		@wfiles = ();
		foreach (@files){
			@dmy = split(/\//,$_);
			$dmy_su = @dmy - 1;
			$fn = $dmy[$dmy_su];
			@dmy = split(/\//,$ip_ck_file);
			$dmy_su = @dmy - 1;
			$ipw = $dmy[$dmy_su];
			$fck = $log_dir .$fn;
			if($fn ne $ipw && (-e $fck)){ push(@wfiles,$fn); }
		}
	}
	@wfilesw = sort { $b <=> $a } @wfiles;
}

#===============================�֥�å��ꥹ�ȵ�Ģ===========================
sub bin{
	$log_file = $log_dir .$QUERY{'day'} .'.' .$kakucho; # ���ե�����
	if(-e $log_file){
		open(LOG,"$log_file") || &error('FILE OPEN ERROR - log');
		@logs = <LOG>;
		close(LOG);
		$ipw = "";
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
			if($user_ipc eq $QUERY{'ip'}){ $ipw = $user_ipw; }
		}
	}
	open(BLT,"$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
	@blists = <BLT>;
	close(BLT);
	if($ip_ck_su != 0){ while(@blists >= $ip_ck_su){ pop @blists; } }
	unshift(@blists,"$ipw<>$QUERY{'ip'}<>\n");
	open(OUT,">$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
	print OUT @blists;
	close(OUT);
	# ����ɽ���
    print "Location: $cgi_file?mode=view\n\n";
}

#===============================�֥�å��ꥹ�Ȳ��===========================
sub bout{
	open(BLT,"$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
	@blists = <BLT>;
	close(BLT);
	@news = ();
	foreach (@blists){
		($n_ip,$c_ip) = split(/<>/,$_);
		if($c_ip ne $QUERY{'ip'}){ push(@news,$_); }
	}
	open(OUT,">$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
	print OUT @news;
	close(OUT);
	# ����ɽ���
    print "Location: $cgi_file?mode=view\n\n";
}

#===============================�֥�å��ꥹ��ɽ��===========================
sub blist{
	open(BLT,"$ip_ck_file") || &error('FILE OPEN ERROR - Black List');
	@blists = <BLT>;
	close(BLT);
	$bdata = "";
	foreach $bk(@blists){
		($n_ip,$c_ip) = split(/<>/,$bk);
		$bdata .= "<tr><td bgcolor=\"#ffffff\">$c_ip</td><td bgcolor=\"#ffffff\"><a href=\"$cgi_file?mode=bout&ip=$c_ip\">���</a></td></tr>";
	}
	print "Content-Type: text/html\n\n";
	print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\">\n";
	print <<"EOM";
		<html>
		<head><title>PATIPATI �֥�å��ꥹ��ɽ��</title>
		<meta http-equiv="Content-Type" content="text/html; charset=EUC-JP">
		<style type="text/css">
		<!--
		body, tr, td { font-size: 10pt; }
		small        { font-size: 8pt; }
		big          { font-size: 12pt; }
		A:link,A:visited,A:active {text-decoration:none;}
		A:link { color: #ff9900 }
		A:active { color: #ffcc00 }
		A:visited { color: #660000 }
		A:hover { color: #ffcc00 }
		-->
		</style>
		<base target="patiview">
		</head>
		<body bgcolor="#ffffff" text="#666666">
		<table cellspacing=1 cellpadding=4 border=0 bgcolor="#666666">
		<tr><td bgcolor="#cccccc">�Ź沽���줿IP</td><td bgcolor="#cccccc">���</td></tr>
		$bdata
		</table>
		<hr noshade size=1>- $systeminfo -
		</body></html>
EOM
	exit;
}

#===============================�������Ƚ���===========================
sub logout{
	&set_adcookie("0","");
	# ����ɽ���
    print "Location: $cgi_file?\n\n";
}

#===============================���å����μ���===========================
sub get_adcookie{
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

#===============================���å�����ȯ��($days����ͭ��)===========================
sub set_adcookie{
	my $days = $_[0];
	my $cook = $_[1];
	($secg,$ming,$hourg,$mdayg,$mong,$yearg,$wdayg,$dmy,$dmy) = gmtime(time + 60*24*60*$days);
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

