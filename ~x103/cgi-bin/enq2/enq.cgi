#!/usr/bin/perl
#�T�[�o�ɂ���Ă͏�̈ꕶ��ύX����K�v������܂��B�T�[�o�Ǘ��҂ɂ��q�˂��������B
$ver = 3.50; #�o�[�W�������

#-----����ȉ��̒���ҕ\����ύX���Ȃ��ł�������-----
#
#�l�b�g�}�j�A�@WEB�A���P�[�g�V�X�e���J�X�^�}�C�Y��
#//www.netmania.jp
#���̃X�N���v�g�̓t���[�E�F�A�ł��B
#���̃X�N���v�g�̐ݒ�E�ݒu�E�^�p�̓X�N���v�g�g�p�҂̐ӔC�ɂ����čs���Ă��������B
#����ҕ\�������ς��Ȃ��ŉ������B
#�J�X�^�}�C�Y�ł̍Ĕz�z�͋֎~���܂��B

#-----�X�N���v�g�z�z��--------------------------------
#[Web Qnaire 1]
#(C)narishin,2000-2004
#//www.narishin.com

#-----�ݒu���@----------------------------------------
#
#	enq.cgi		[755][707]	���g���̃T�[�o�[�ɍ��킹�ĕύX
#	data.txt	[666][600]
#	jcode.pl	[644]
#	graph.gif	[644]
#


#���A�����[���֎~�������ꍇ�A229�E230�s�ځA�擪�́u#�v������ĉ������B



#----------------------
#�����ݒ�
#---------------------- 


$mkazu = 10000;				#�t���[���b�Z�[�W�\����(0:��\��)
$home='//103.coxb.net/~x103/';	#�z�[���y�[�W(�A���A��΃p�X�Ŏw��)
$mail='hitomi.s.akky@gmai.com';		#�Ǘ��҃��[��
$pass='saku2';				#�Ǘ��җp�p�X���[�h

$title='�A���P�[�g';	#�^�C�g��

$iken='���ӌ��E�����z���ǂ���(�K�{�ł͂���܂���)';	#�ӌ��\���^�C�g��
$iken2='���ӌ��E�����z';				#�ӌ��\���^�C�g���i���ʁj

$bgcolor='#ffffff';		#�w�i�F
$bgimage='//';		#�w�i�摜

#������(�^�O���g�p�\)
$subtitle='�e���v���[�g�̓W���y�[�W�ɂ��Ăł��B';

#----------------------
#�����ݒ�Q�i���ɕύX�̕K�v�i�V�j
#---------------------- 

require './jcode.pl';		#���{�ꏈ���n(���̃t�@�C���Ɠ����f�B���N�g���ɂ����Ă�������)
$kanji='sjis';			#�����ϊ�����(sjis(����)��jis��euc)
$method='POST';			#���\�b�h�`��(POST(����)��GET)
$lockkey = 0;			# ���b�N�@�\ (0:�s�g�p 1:�g�p)
$lockfile = './lock';		# ���b�N�t�@�C����
$script='./enq.cgi';		#�X�N���v�g��(���̃t�@�C���̖��O)
$logfile='./data.txt';		#�f�[�^�t�@�C����(���̃t�@�C���Ɠ����f�B���N�g���ɂ����Ă�������)
$graphgif='graph.gif';		#�O���t�p�摜�f�[�^(��΃p�X�Ŏw��)
$twidth='660';			#�e�[�u���̕�
$twidth2='640';			#�������e�[�u���̕��i��L�e�[�u����菬���߂Ɂj
#�ȉ��X�^�C���V�[�g
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
	font-family: Verdana, Arial, "�q���M�m�p�S Pro W3", "�l�r �o�S�V�b�N", sans-serif;}


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
#���C�������n
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
#�������[���
#----------------------------------
sub tohyo{
	&head;

	print "<h1>$title</h1><div class=head>


\n";
	if ($home ne '//'){
		print "<a href=$home>�z�[����</a> | \n";
	}
	print "<a href=$script?mode=kekka>���[����</a>\n";

print <<"EOM";
</div>
<script type="text/javascript"><!--
   location.href = "//103.coxb.net/~x103/";
// --></script>

<center><div class=mes>$subtitle</div></center><br />
EOM

	print " 

<FORM action=\"$script\" method=\"$method\"> \n";

	open (IN,$logfile) || &error("���O�t�@�C�����J���܂���"); #�f�[�^�t�@�C���ǂݍ���
	@qset = <IN>;		#�z��qset��tohyo.log�̊e�s���v�f�Ƃ��Ă͂���
	close(IN);

	chop($qset[0]);
	$qkazu = $qset[0];
	for ($i=1;$i<=$qkazu;$i++){			#����ƑI�����̓ǂݍ���
		@qtemp=split( /,/,$qset[$i]);		#�ǂݍ��񂾍s��,��ŋ�؂�
		print "\n<center><div class=enq><h2>$qtemp[0]</h2>\n




<ul>\n";	#��蕶�̕\��
		if ($qtemp[3] =~ m/select/){		#�v���_�E���`���̑I����
			print "<li><select name=$i>\n";
			print "<option value='none'>�I�����Ă�������</option>\n";
		}
		for ($j=1;$j<=$qtemp[1];$j++){			#�I�����̕\��
			($anstmp,$hyotmp)=split( /=/,$qtemp[$j+3]);	#�I�����Ɠ��[���𕪂���
			if ($qtemp[3] =~ m/select/){		#�v���_�E���`���̑I����
				print "<option value=$i/$j>$anstmp</option>\n";
			}else{
				$t_temp3 = $qtemp[3];
				$t_temp3 =~ s/=sort// , $t_temp3 =~ s/=sosu//;
				print "<li><input type=$t_temp3 name=$i value=$i/$j> $anstmp</li>\n";
			}
		}
		if ($qtemp[3] =~ m/select/){		#�v���_�E���`���̑I����
			print "</select></li><br />\n\n";
		}
		if ($qtemp[2] eq 'yes'){			#�I�����̒ǉ���q�˂�
			if ($qtemp[3] =~ m/select/){
				$tmpadd = 'checkbox';
			}else{
				$tmpadd = $qtemp[3];
				$tmpadd =~ s/=sort// , $tmpadd =~ s/=sosu//;
			}
			print "<li><input type=$tmpadd name=$i value=add>\n";
			print "���̑� <input type=text size=30 name=add$i></li>\n";
		}
		print "</ul></div></center>\n";	
	}
	
	if ($mkazu > 0){
		print <<"EOM";



<center><div class=enq><h2>$iken</h2>
<ul><li>���O�@<input type=text name=tname size="20"></li>
<li><textarea name=toko rows=5 cols=70></textarea></li></ul>
</div></center>
EOM
 
	}

	print <<"EOM";
<center>

<INPUT type="submit" value="�@�@�@���[����@�@�@"><br><br>
�����͂��肪�Ƃ��������܂����B
<input type="hidden" name="mode" value="tohyo"></CENTER></form>

EOM
	
	&foot;
}

#----------------------------------
#���ʕ\��
#----------------------------------
sub tsuika{
	&lock if ($lockkey); 	# ���b�N�J�n

	open (IN,$logfile) || &error("���O�t�@�C�����J���܂���"); #�f�[�^�t�@�C���ǂݍ���
	@qset=<IN>;			#�f�[�^����s���Ɣz��qset�ɓ����
	close (IN);

	chop(@qset);			#qset�̍Ō�̉��s����菜��

	$lahost=$qset[$qset[0]+3];
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
	#if ($lahost eq $host && $mode eq 'tohyo') {
	#	&error("�A�����[�͂ł��܂���B<br><br>(�ڑ��z�X�g��ς��ē��[�������Ă݂Ă�������)");}

	&head;				#�w�b�_�o��
	&jikan(0);			#�����ԓǂݍ���


	print "<h1>���[��</h1><div class=head>\n";
	if ($home ne '//'){
		print "<a href=$home>�z�[��</a> | \n";
	}

	print "<a href=$script>�A���P�[�g�֖߂�</a>\n";
	print "<BR>[$jikanl]���݂̓��[�󋵂ł��B</div>\n";

	if ($mode eq 'tohyo'){
		print "

<center><div class=\"mes\">�������������肪�Ƃ��������܂����B</div></center>
\n";
		print "<br>\n\n";
	}



	$qkazu=$qset[0];
	$qset[0]="$qset[0]\n";
	for ($i=1;$i<=$qkazu;$i++){		#���₲�Ƃ̏���		
		@qtemp=split(/,/,$qset[$i]);	#�s���f�[�^��,��ŕ����Ĕz��qtemp�Ɋi�[	
		$add = $in{"add$i"};	#�ǉ�����I�������e
		$tothyo = 0;		#����ʂ̑��[��
		$maxhyo = 1;		#����ʂ̍ō����[��
		for ($j=1;$j<=$qtemp[1];$j++){			#�����̑I�����ւ̏���
			($anstmp[$j],$hyotmp[$j])=split(/=/,$qtemp[$j+3]);
			$done=0;
			foreach $x (@ans){		
				if ("$i/$j" eq $x){
					$hyotmp[$j]++,$done=1; #�[���̒ǉ�
				}
			}
			if ($add eq $anstmp[$j] ){
				$add='';			#�ǉ�����I����������
				if ($done == 0 ){
					$hyotmp[$j]++;
				}
			}
			if ($hyotmp[$j] > $maxhyo){	#�ō����[���̍X�V
				$maxhyo = $hyotmp[$j];
			}
			$qtemp[$j+3]="$anstmp[$j]=$hyotmp[$j]";	#�X�V�f�[�^���i�[
			$tothyo += $hyotmp[$j];			#���₲�Ƒ��[���X�V
		}
		if ($in{$i} eq 'add' && $add ne ''){		#�I�����ǉ�
			$qtemp[$j+3]="$add=1",$tothyo++;
			$anstmp[$j]=$add,$hyotmp[$j]=1,$qtemp[1]++,$j++;
		}

		#�[���ɂ��\�[�g�\��
		if ($qtemp[3] =~ m/sort/){
			$hyotmp[0] = 0; #�_�~�[
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

		print "\n<h3>$qtemp[0]</h3>";		#���╶�̕\��
		if ($qtemp[3] =~ m/sosu/){
			print "\n<div class=sou>���[���� $tothyo �[</div>";	#���[�����\��
		}
		print "\n<center><table class=tab4>";	#���ʕ\��
		for ($j=1;$j<=$qtemp[1];$j++){
			$wari[$j]=0;	#�[�̊���
			$width = 0;	#�O���t�摜�\����
			print "\n<tr><td>$h_anstmp[$j]</td>";
			print "<th width=60 align=center>$h_hyotmp[$j] �[</th>";
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
		push(@qtemp,"\n");		#�s���ɉ��s������
		$qset[$i]=join(",",@qtemp);	#�s�f�[�^���X�V����
	}					#���₲�Ƃ̏����̏I��

	#���b�Z�[�W�̏���
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
 
	@tnaiyo = split(/<br>/,$qset[$qkazu+1],$mkazu+1);
	if($in{'toko'} ne ''){			#���b�Z�[�W�X�V
		unshift (@tnaiyo,"<tr><th>$in{'tname'} ($jikanl)</th><td>$in{'toko'}</td>");
	} 
	splice (@tnaiyo,$mkazu);
	$qset[$qkazu+1] = join('',@tnaiyo);
	$qset[$qkazu+1] = "$qset[$qkazu+1]\n";

	if ($mkazu > 0){

		print "<h4>$iken2</h4>\n";
		print "<table class=tab5>\n";
		print "$qset[$qkazu+1]\n";	#���b�Z�[�W�\��
		print "</table>\n";
	}

	if ($mode eq 'tohyo'){
 	$qset[$qkazu+2]="$jikanl \n";			#�ŏI���[���ԍX�V
	}else{
	$qset[$qkazu+2]="$qset[$qkazu+2]\n";
	}

	if ($mode eq 'tohyo'){
 	$qset[$qkazu+3]="$host\n";			#�ŏI���[�z�X�g�X�V
	}else{
	$qset[$qkazu+3]="$qset[$qkazu+3]\n";
	}

	$qset[$qkazu+4]="$qset[$qkazu+4]\n";		#���f�[�^����
	$qset[$qkazu+5]="$qset[$qkazu+5]\n";		#���f�[�^����
	$qset[$qkazu+6]="$qset[$qkazu+6]\n";		#���f�[�^����
	$qset[$qkazu+7]="$qset[$qkazu+7]\n";		#���f�[�^����
	$qset[$qkazu+8]="$qset[$qkazu+8]\n";		#���f�[�^����

	#�f�[�^�t�@�C���X�V
	open (OUT,">$logfile") || &error("���O�t�@�C�����J���܂���");				
	print OUT @qset;
	close(OUT);
	
	&unlock if ($lockkey); # ���b�N����
	
	print "<center><div class=back><a href=$script>�A���P�[�g�ɖ߂�</a></div></center>\n";
	&foot;					#�t�b�^�\��
}

#----------------------------------
#�Ǘ��җp
#----------------------------------
sub kanri{
	if ($in{'pass'} ne "$pass") {&error('�Ǘ��҃��[�h');}	

	&jikan(0);

	&head;
	print <<"EOM";

<h1>�Ǘ��y�[�W</h1><div class=head><a href=$script>�A���P�[�g��ʂ�</a></div>

EOM

	&lock if ($lockkey); 	# ���b�N�J�n

	open (IN,$logfile) || &error("���O�t�@�C�����J���܂���"); #�f�[�^�t�@�C���ǂݍ���
	@qset=<IN>;			#�f�[�^����s���Ɣz��qset�ɓ����
	close (IN);

	chop(@qset);			#qset�̍Ō�̉��s����菜��

	print "\n";


	$qkazu=$qset[0];
	$qset[0]="$qset[0]\n";

	#����̏���
	foreach $x (@delque){
		splice(@qset,$x,1);
		$qkazu--;
		$qset[0]="$qkazu\n";
	}

	#����̒ǉ�
	if ($in{'addque'} ne ''){
		$qkazu++;
		$qset[0]="$qkazu\n";		#���␔�̍X�V
		splice(@qset,1+$in{'ajun'},0,"$in{'addque'},0,$in{'aadd'},$in{'rc'},"); 
	}

	for ($i=1;$i<=$qkazu;$i++){		#���₲�Ƃ̏���		
		@qtemp=split(/,/,$qset[$i]);	#�s���f�[�^��,��ŕ����Ĕz��qtemp�Ɋi�[	
		$add=$in{"add$i"},$tothyo=0;	

		if ($in{'qubunc'} eq $i){	#���╶�̍X�V
			$qtemp[0] = $in{'qubun'};
		}		
		if ($in{'qtyc'} eq $i){		#�񓚕��@�̍X�V
			$qtemp[2] = $in{'aadd'};
			$qtemp[3] = $in{'rc'};
			if ($in{'sort'} && $qtemp[3] !~ m/sort/){
				$qtemp[3] .= '=sort';	#�\�[�g�L���̕ύX
			}elsif (!$in{'sort'}){
				$qtemp[3] =~ s/=sort//;
			}
			if ($in{'sosu'} && $qtemp[3] !~ m/sosu/){
				$qtemp[3] .= '=sosu';	#���[�����\���L���̕ύX
			}elsif (!$in{'sort'}){
				$qtemp[3] =~ s/=sosu//;
			}
		}		


		print "\n<div class=kanri_enq><center><h3>$qtemp[0]</h3>\n";		#���╶�̕\��
		print "
			<table class=\"tab\">
			<form action=$script method=$method>
			<input type=hidden name=mode value=kanri>
			<input type=hidden name=pass value=$pass>
			<input type=hidden name=k_mode value=bunhen>
			<input type=hidden name=qubunc value=$i>
			<tr>
			<th>���╶�̕ύX</th>
			<td><input type=text size=70 name=qubun value='$qtemp[0]'></td>
			<td><input type=submit value='�ύX'></td>
			</tr>
			</form>
			
			<form action=$script method=$method>
			<input type=hidden name=mode value=kanri>
			<input type=hidden name=pass value=$pass>
			<input type=hidden name=$i value=add>
			<tr>
			<th>�I������ǉ�</th>
			<td><input type=text size=70 name=add$i></td>
			<td><input type=submit value='�ǉ�'></td>
			</tr>
			</form>
			</table>


		\n";		#���╶�̕ύX�ƒǉ�



		for ($j=1;$j<=$qtemp[1];$j++){			#�����̑I�����ւ̏���
			($anstmp[$j],$hyotmp[$j])=split(/=/,$qtemp[$j+3]);
			$done=0;

			if ($in{'qrset'} eq $i){
				$hyotmp[$j] = 0;	#�[�������Z�b�g
			}

			if ($add eq $anstmp[$j] ){
				$add='';			#�ǉ�����I����������
			}

			$qtemp[$j+3]="$anstmp[$j]=$hyotmp[$j]";	#�X�V�f�[�^���i�[
			$tothyo += $hyotmp[$j];			#���₲�Ƒ��[���X�V

			foreach $x (@del){
				if ("$i/$j" eq $x && $chfl == 0){
					splice(@qtemp,$j+3,1);	#�I�����̏���
					$tothyo -= $hyotmp[$j];
					$hyotmp[$j]=0;
					$qtemp[1]--;
					$j--,$chfl=1;
				}
			}
		}

		if ($in{$i} eq 'add' && $add ne ''){		#�I�����ǉ�
			$qtemp[$j+3]="$add=0";
			$anstmp[$j]=$add,$hyotmp[$j]=0,$qtemp[1]++,$j++;
		}

		print "<div class=sou>���[���� $tothyo �[</div>";	#���[�����\��
		print "\n<table class=\"tab3\">";	#���ʕ\��
		for ($j=1;$j<=$qtemp[1];$j++){
			$wari[$j]=0;
			if ($tothyo>0) {
				$wari[$j]=sprintf("%.1f",$hyotmp[$j]*100/$tothyo);
			}
			$width = int ( 3 * $wari[$j] );
			print "\n<tr><th>$anstmp[$j]</th>";
			print "<td align=center width=100>$hyotmp[$j] �[</td>";
			if ($qtemp[3] =~ m/radio/){
				print "<td align=center width=100>$wari[$j] %</td>";
			}

			print "<form action=$script method=$method><td align=center width=50>\n";
			print "\n";
			print "<input type=hidden name=mode value=kanri>\n";
			print "<input type=hidden name=pass value=$pass>\n";
			print "<input type=submit value='�폜'>\n";
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
 <option value=radio selected>���W�I�{�^��</option>
 <option value=select>�v���_�E��</option>
 <option value=checkbox>�����񓚃`�F�b�N</option>
 </select>\n";



		}elsif($qtemp[3] =~ m/select/){
			print " <select name=rc>
 <option value=radio>���W�I�{�^��</option>
 <option value=select selected>�v���_�E��</option>
 <option value=checkbox>�����񓚃`�F�b�N</option>
 </select>\n";

		}else{
			print " <select name=rc>
 <option value=radio>���W�I�{�^��</option>
 <option value=select>�v���_�E��</option>
 <option value=checkbox selected>�����񓚃`�F�b�N</option>
 </select>\n";

		}
		if ($qtemp[2] eq 'yes'){
			print " <select name=aadd>
 <option value=yes selected>�I�����̒ǉ�������</option>
 <option value=no>�I�����̒ǉ��Ȃ�</option>
 </select>\n";

		}else{
			print " <select name=aadd>
 <option value=yes>�I�����̒ǉ�������</option>
 <option value=no selected>�I�����̒ǉ��Ȃ�</option>
 </select>\n";

		}
		if($qtemp[3] =~ m/sort/){
			print " <select name=sort>
 <option value=1 selected>�[�����ɕ��ւ�</option>
 <option value=0>�񎦏���\�\\��</option>
 </select>\n";

		}else{
			print " <select name=sort>
 <option value=1>�[�����ɕ��ւ�</option>
 <option value=0 selected>�񎦏���\�\\��</option>
 </select>\n";

		}
		if ($qtemp[3] =~ m/sosu/){
			print " <select name=sosu>
 <option value=1 selected>���[����\�\\������</option>
 <option value=0>���[����\�\\�����Ȃ�</option>
 </select>\n";

		}else{	
			print " <select name=sosu>
 <option value=1>���[����\�\\������</option>
 <option value=0 selected>���[����\�\\�����Ȃ�</option>
 </select>\n";

		}
		print "<input type=submit value='�ύX'>\n";
		print "</form>\n\n";

		print "<BR><table><tr>
<td width=100><form action=$script method=$method>\n";
		print "\n";
		print "<input type=hidden name=mode value=kanri>\n";
		print "<input type=hidden name=pass value=$pass>\n";
		print "<input type=hidden name=qrset value=$i>\n";
		print "<input type=submit value='�[�����Z�b�g'>\n";

		print "</form></td>\n";

		print "<td><form action=$script method=$method>\n";
		print "<input type=hidden name=mode value=kanri>\n";
		print "<input type=hidden name=pass value=$pass>\n";
		print "<input type=submit value='���̎�����폜����'>\n";
		if ($qtemp[1] == 0){	#���̎���ɑI�������Ȃ��ꍇ
		print "<input type=hidden name=delque value=$i>\n";
		}else{			#���̎���̑I�������c���Ă���ꍇ
		print "<input type=hidden name=delque value=\"muko\">\n";
		}
		print "</form></td></table>\n";
		print "<br>������폜����ꍇ�͂��ׂĂ̑I�������폜���Ă���s���Ă��������B</center></div>\n";


		push(@qtemp,"\n");		#�s���ɉ��s������
		$qset[$i]=join(",",@qtemp);	#�s�f�[�^���X�V����
	}					#���₲�Ƃ̏����̏I��









	print "<div class=add><form action=$script method=$method>\n";
	print "<h3>�����ǉ�����</h3>\n";
	print "\n";
	print "<input type=hidden name=mode value=kanri>\n";
	print "<input type=hidden name=pass value=$pass>\n";
	print "<input type=hidden name=k_mode value=bunadd>\n";
	print "<center><table class=tab6><tr><th>����ǉ��ʒu</th><td>\n";

	print "<select name=ajun>\n";
	if ($qkazu > 0){
	print "<option value=$qkazu>�Ō�  ($qkazu�Ԗڂ̎���̌�)</option>\n";
	}
	print "<option value=0>�擪</option>\n";
	for ($i=1;$i<=$qkazu-1;$i++){
		print "<option value=$i>$i�Ԗڂ̎���̌�</option>\n";
	}
	print "</select> �ɒǉ�</td></tr>\n";
	print "<tr><th>���╶</th><td>\n";
	print "<input type=text size=60 name=addque></td></tr>\n";
	print "<tr><th>�I���`��</th><td>\n";
	print "<input type=radio name=rc value=radio checked>���W�I�{�^��\n";
	print "<input type=radio name=rc value=select>�v���_�E��\n";
	print "<input type=radio name=rc value=checkbox>�����񓚃`�F�b�N�{�b�N�X</td></tr>\n";
	print "<tr><th>�I�����̒ǉ�</th><td>\n";

	print "<input type=radio name=aadd value=yes>������\n";
	print "<input type=radio name=aadd value=no checked>�����Ȃ�</td></tr>\n";
	print "<tr><th>���ёւ�</th><td>\n";

	print "<input type=radio name=sort value=1>�[�����ɕ��ւ���\n";
	print "<input type=radio name=sort value=0 checked>�񎦏���\�\\��</td></tr>\n";
	print "<tr><th>���[��\�\\��</th><td>\n";

	print "<input type=radio name=sosu value=1>���[����\�\\������\n";
	print "<input type=radio name=sosu value=0 checked>���[����\�\\�����Ȃ�</td></tr>\n";
	print "</table></center>\n";
	print "<center><input type=submit value='�ǉ�����'></center>\n";
	print "</form></div>\n\n";
	
	#���b�Z�[�W�̏���
	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};
	if ($host eq $addr) { $host = gethostbyaddr(pack('C4',split(/\./,$host)),2) || $addr; }
 
	@tnaiyo = split(/<br>/,$qset[$qkazu+1],$mkazu+1);
	if($in{'toko'} ne ''){			#���b�Z�[�W�X�V



		unshift (@tnaiyo,"<tr><th>$in{'tname'} ($jikanl)</th><td>$in{'toko'}</td>");
	} 
	splice (@tnaiyo,$mkazu);
	
	if ($in{'todel'} ne ''){
		$tnaiyocp = $tnaiyo[$in{'todel'}-1];
		$tnaiyocp =~ tr/<> //d; 
		if ($tnaiyocp eq $in{'todelnai'}){
			splice (@tnaiyo,$in{'todel'}-1,1);	#���e���e�̍폜
		}else{
			print "<font color=red>�V�K���e������܂����B�m�F���Ă��������B�f�[�^�ی�̂��ߓ��e���폜���܂���B</font>\n";
		}
	}
	$tnkazu = @tnaiyo;
	if ($mkazu > 0){
		print "\n";
		print "<h4>$iken2</h4>\n";
		print "<table class=tab5>\n";
		if ($tnkazu == 0){
			print "(���� �����͂���܂���)\n";
		}
	}
	for ($i=1;$i<=$tnkazu;$i++){

	print "$tnaiyo[$i-1]\n";	#���b�Z�[�W�\��


	}

	$qset[$qkazu+1] = join('<br>',@tnaiyo);
	$qset[$qkazu+1] = "$qset[$qkazu+1]\n";
	$qset[$qkazu+2]="$qset[$qkazu+2]\n";
	$qset[$qkazu+3]="$qset[$qkazu+3]\n";		#���f�[�^����
	$qset[$qkazu+4]="$qset[$qkazu+4]\n";		#���f�[�^����
	$qset[$qkazu+5]="$qset[$qkazu+5]\n";		#���f�[�^����
	$qset[$qkazu+6]="$qset[$qkazu+6]\n";		#���f�[�^����
	$qset[$qkazu+7]="$qset[$qkazu+7]\n";		#���f�[�^����

		print "</table>\n";

	#�f�[�^�t�@�C���X�V
	open (OUT,">$logfile") || &error("���O�t�@�C�����J���܂���");				
	print OUT @qset;
	close(OUT);

	&unlock if ($lockkey); # ���b�N����
	
	&foot;
}




#----------------------------------
#���͏��̉��
#----------------------------------
sub decode{
	if ($ENV{'REQUEST_METHOD'} eq "POST") {
		read(STDIN, $buffer, $ENV{'CONTENT_LENGTH'});
	} else { $buffer = $ENV{'QUERY_STRING'}; }

	open (IN,"$logfile") || &error("���O�t�@�C�����J���܂���");
	@qset=<IN>;
	close (IN);

	chop($qset[0]);

	for($i=1;$i<=$qset[0];$i++){	#�𓚃`�F�b�N�̂��߂̔z��
		$input[$i] = 0;
		$addc[$i] = 0;
	}

	@pairs = split(/&/, $buffer);	#���̓f�[�^���Ƃɕ�����
	foreach $pair (@pairs) {
		($name,$value) = split(/=/, $pair);	#name��value�ɕ�����
		$value =~ tr/+/ /d;			#�󔒕ϊ�
		$value =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
		$value =~ tr/\n/\ /d; #���s����
		$value =~ tr/\n/ /d;			#���s����
		$value =~ s/,/&sbquo;/g;		#�,�����
		if ($in{'k_mode'} ne 'bunhen'){$value =~ s/=/&#61;/g;}#�=�����
		if ($in{'mode'} ne 'kanri'){$value =~ s/</&lt;/g;}#�<�����
		&jcode'convert(*value,"$kanji");	#�����ϊ��R�[�h�w��

		$in{$name} = $value;
			
		if ($name <= $qset[0] && $value ne 'none'){	#����ւ̉𓚂����
			if( $value ne 'add'){
				push (@ans,$value);	#�����̑I�����ւ̓��[
				if ($addc[$name] == 0){ #�I�����ǉ���񖳂�
					$addc[$name] = 0;
				}
			}else{
				$addc[$name] = 1 ;	#�I�����̒ǉ�
			}
		$input[$name]=1;
		}
		if ($name > $qset[0]){ #�񓚂��悤�Ƃ������₪���łɍ폜�ς�
			&error('�񓚂��悤�Ƃ������₪�폜����Ă��܂��B�m�F���Ă��������B');
		}

		if ($name eq 'del'){
			push (@del,$value);		#�I�����̍폜
		}

		if ($name eq 'delque'){
			if ($value eq 'muko'){
			&error('��������������̑I���������ׂč폜���Ă�����s���Ă��������B<br><br>
(���ɂ��ׂĂ̑I�������폜����Ă���ꍇ�A1�� �[�����Z�b�g���s���Ă݂Ă��������B)');
			}else{
			push (@delque,$value);		#����̏���
			}
		}
	}

	if ($in{'mode'} eq 'tohyo'){			#�񓚏��̕s�����`�F�b�N
		for ($i=1;$i<=$qset[0];$i++){
			if ($input[$i] != 1){
				&error("$i �Ԗڂ̎��₪���𓚂ł�");
			}
			if ($addc[$i] == 1 && $in{"add$i"} eq ''){
				&error("$i �Ԗڂ̎���̑I�����ɒǉ����������e��������Ă��܂���");
			}
		}
		if ($in{'tname'} eq '' && $in{'toko'} ne ''){
			&error('���b�Z�[�W�ɂ����O������܂���');
		}
	}
	if ($in{'mode'} eq 'kanri'){			#�񓚏��̕s�����`�F�b�N
		for ($i=1;$i<=$qset[0];$i++){
			if ($addc[$i] == 1 && $in{"add$i"} eq ''){
				&error("$i �Ԗڂ̎���̑I�����ɒǉ����������e��������Ă��܂���");
			}
		}
		if ($in{'k_mode'} eq 'bunadd' && $in{'addque'} eq ''){
			&error("�ǉ����鎿�╶�ɓ��e������܂���");
		}	
	}
	$mode = $in{'mode'};
}

#----------------------------------
#���ԓǂݍ���
#----------------------------------
sub jikan{

	#�X�V����p
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
#�w�b�_�\��
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
#�t�b�^�\��
#----------------------------------
sub foot{
	print <<"EOM";
</div>
<DIV class=foot>�E�F�u�A���P�[�//��<a href=http://www.narishin.com>Web //1</a> + <a href=http://www.netmania.jp>Netmania</a> | <a href=$script?mode=kanri>�Ǘ�</a></div>
</body></html>
EOM
	exit;
}

#----------------------------------
#  ���b�N����  
#----------------------------------
sub lock {
	local($retry, $mtime);

	# 1���ȏ�Â����b�N�͍폜����
	if (-e $lockfile) {
		($mtime) = (stat($lockfile))[9];
		if ($mtime < time - 60) { &unlock; }
	}
	# ���b�N����
	$retry=5;
	while (!mkdir($lockfile, 0755)) {
		if (--$retry <= 0) { &error('LOCK is BUSY'); }
		sleep(1);
	}
	$lockflag=1;
}

#----------------------------------
#  ���b�N����  
#----------------------------------
sub unlock {
	rmdir($lockfile);
	$lockflag=0;
}

#----------------------------------
#�G���[����
#----------------------------------
sub error{
	&unlock if ($lockflag); # ���b�N����
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
<div class=admin><form action=\"$script\" method=\"$method\"><input type=hidden name=mode value=\"kanri\"><input type=password name=pass size=8> <input type=submit value=\"�Ǘ��p\"></form></div>



EOM

	&foot;
}


