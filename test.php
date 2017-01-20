<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<title>简陋空气质量</title>
	</head>
	<body>
		<center><table style="border:dotted;border-color:#F06">
		<caption>留言内容</caption>
		<tr><th>编号</th><th>日期</th><th>时间</th><th>aqi</th></tr>
		<?php
		$link=mysql_connect('localhost','root','root')or die("数据库连接失败");
		//连接数据库
		mysql_select_db('aqi',$link);//选择数据库
		mysql_query("set names utf8");//设置编码格式
		
		$q="select * from aqi";//设置查询指令
		$result=mysql_query($q);//执行查询
		while($row=mysql_fetch_assoc($result))//将result结果集中查询结果取出一条
		{
		echo"<tr><td>".$row["id"]."</td><td>".$row["date"]."</td><td>".$row["time"]."</td><td>".$row["aqi"]."</td><tr>";
		
		}
		?>
		</table>
		</center>
                <a href="http://s349.photobucket.com/user/Tifosili/media/683423488882294895_zpsl0tcfxy2.jpg.html" target="_blank"><img src="http://i349.photobucket.com/albums/q374/Tifosili/683423488882294895_zpsl0tcfxy2.jpg" border="0" alt="不吃了 photo 683423488882294895_zpsl0tcfxy2.jpg"/></a>
	</body>
<html>
