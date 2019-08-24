#=======================================================================================
# ���̥��֥롼����
#=======================================================================================
$systeminfo = '<a href="http://www.gnbnet.com/" target="_blank">PatiPati (Ver 4.3)</a>';
$salt = 'pt';

#======================================���ּ����롼����=================================
sub get_date{
	$timew = $_[0];
	$ENV{'TZ'} = "JST-9";
	@date = localtime($timew);
	$nen = $date[5] + 1900;
	$tsuki = sprintf("%02d",$date[4] + 1);
	$hi = sprintf("%02d",$date[3]);
	$jikan = sprintf("%02d",$date[2]);
	$youbi = ('��','��','��','��','��','��','��') [$date[6]];
	$gw = $nen .$tsuki .$hi;
	return $gw;
}

#======================================��å������롼����=================================
sub lock1 { # flock�ؿ�
 	eval { flock( LOCKCHK, 8 ) ; } ;
	if ( ! $@ ){
		open(LOCK,">$lock_file") or die "Can't open lockfile: $!";
	  flock(LOCK, 2) or die "Can't flock        : $!";
	}else{
		&error('���Υ����С��Ǥ�flock�ؿ��ϻȤ��ʤ��褦�Ǥ���');
	}
}

sub lock2 { # mkdir�ؿ�
	$retry = 5; # ��ȥ饤������å�
	$lockdir = $lock_file;
	$lockdir =~ s/\./_/g;
	$lockdir2 =  'c_' .$lockdir;
	while (!mkdir($lockdir, 0755)) {
		if (--$retry <= 0) {
			if (mkdir($lockdir2, 0755)) {          # ��å���ä��������¾
				if ((-M $lockdir) * 86400 > 600) { # �������֤�10ʬ�ʾ����ʤ�
					rename($lockdir2, $lockdir) or die 'LOCK ERROR'; # ��å������ؤ�
					last;                          # ��Ϣ�ν�����
				}else { rmdir($lockdir2); }         # ��ʬ��å����
			}
			&error("BUSY");
		}
		sleep(1);
	}
}

sub unlock { # ��å����
	if ($lockkey == 1) { close(LOCK); }
	elsif ($lockkey == 2) {
		$lockdir = $lock_file;
		$lockdir =~ s/\./_/g;
		rmdir($lockdir);
	}
}

#================================���ǡ����õ����=================================
sub del_logs{
	$g_mon = $log_dir .'*.' .$kakucho;
	$i = 0;
	while($i <= $log_max){
		$yw = $nen - 1;
		$mw = $tsuki + 12 - $i;
		if($mw > 12){ $yw++; $mw = $mw - 12; }
		$mww = sprintf("%02d",$mw);
		$datew = "$yw$mww" .'31';
		$i++;
	}
	if($shell_use == 1){
		@months = ();
		$dayw = time();
		$dayw = $dayw - 60*60*24*30*$log_max;
		$dayw2 = $dayw - 60*60*24*30*$log_max;
		while($dayw >= $dayw2){
			$wk = &get_date($dayw);
			$wk = $log_dir .substr($wk,0,8) .'.' .$kakucho;
			push(@months,$wk);
			$dayw -= 60*60*24;
		}
	}else{
		@months = glob($g_mon);
	}
	foreach $ml (@months) {
		@ms = split(/\//,$ml);
		$msw = pop(@ms);
		($mw,$ft) = split(/\./,$msw);
		if($mw <= $datew){
			unlink $ml;
		}
	}
}

#================================���顼����=================================
sub error {
	$error = $_[0];
	if ($error eq "") { $error = '���������Υ��顼�ǽ������³�Ǥ��ޤ���'; }
	&jcode'convert(*error,'sjis');
	&unlock; # ��å����
	open(HTML,"$error_file") || die "FILE OPEN ERROR - error";
	@html = <HTML>;
	close(HTML);
	print "Content-Type: text/html\n\n";
	print "<!DOCTYPE HTML PUBLIC -//IETF//DTD HTML//EN>\n";
	foreach $line (@html) {
		$line =~ s/<!--error-->/$error/g;
		$line =~ s/<!--system-->/$systeminfo/g;
		print $line;
	}
	exit;
}


return 1;
