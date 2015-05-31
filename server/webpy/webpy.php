<html>
<head>
<title>SOCCER ANALYTICS</title>
<style type=”text/css”>

</style>
</head>
<body  background="Football.jpg">
<?PHP
 
$a="hello";
$profpic = "footbal.jpg";
?>
<style type="text/css">

body {
background-image: url('<?php echo $profpic;?>');
-webkit-background-size: cover;
                -moz-background-size: cover;
                -o-background-size: cover;
                background-size: cover; 
                background-size: 100% 100%;
}

A:link {
 COLOR: #E65C00 /*The color of the link*/
}
A:visited {
 COLOR: 00FFCC /*The color of the visited link*/
}
A:hover {
 COLOR: #84C084 /*The color of the mouseover or 'hover' link*/
}
BODY { COLOR: #FFFF99 /*The color of all the other text within the body of the page*/
}
h1 {
    font-size: 80px;
}

</style>
 
<h1 align="center" style='color: #FF0000;' >Soccer Analytics</h1>
        <table border="1" align="center">
            <tr>
				<th colspan="2"><h2>Dashboard Actions</h2></th>
                <th><h2>Output</h2></th>
			</tr>
			<tr>
				<th><h2>Historical:</h2></th>
				<td>
					<a href="historical.php"><h2>Run Past Tweet Analysis from MongoDB</h2></a>
				</td>
                <td>
                    <ul>
                        <li><a href="kernel.php" >Twitter Sentiment Kernel</a></li>
                         <li><a href="raw.php" >Twitter Raw Sentiment</a></li>
                          <li><a href="vol.php" >Twitter Sentiment Volume </a></li>
                    </ul>
                </td>
			</tr>
			<tr>
				<th><h2>Runtime:</h2></th>
				<td>
					<a href="dyn.php"><h2>Run Current Tweet Analysis by fetching tweets</h2></a>
				</td>
                <td>
                    <ul>
                        <li><a href="kernel2.php" >Twitter Sentiment Kernel</a></li>
                        <li><a href="raw2.php" >Twitter Raw Sentiment</a></li>
                        <li><a href="vol2.php" >Twitter Sentiment Volume </a></li>
                    </ul>
                </td>
			</tr>
            <tr>
				<th><h2>Data Update:</h2></th>
				<td>
					<a href="dataupdate.php"><h2>Feed database with live tweets</h2></a>
				</td>
                <td></td>
			</tr>
            <tr>
				<th><h2>Top 10 Countries with MEAN:</h2></th>
				<td>
					<a href="top10.php"><h2>Soccer is famous here</h2></a>
				</td>
                <td>
                    <ul>
                        <li><a href="top10.png"><h2>View Graph</h2></a></li>
                    </ul>
                </td>
			</tr>			
            <tr>
				<th><h2>Stats Update:</h2></th>
				<td>
					<a href="stats.php"><h2>Update Stats Info</h2></a>
				</td>
                <td>
                    <ul>
                        <li><a href="stats.txt"><h2>Show Stats</h2></a></li>
                    </ul>
                </td>
			</tr>
            
            <tr>
				<th><h2>World Map:</h2></th>
				<td>
					<a href="world.php"><h2>Populate data</h2></a>
				</td>
                <td>
                    <ul>
                        <li><a href="http://localhost/webpy/updated_dashboard.html" target="_blank"><h2>View Standings</h2></a></li>
                    </ul>
                </td>
			</tr>
			
		</table>
</body>
</html>