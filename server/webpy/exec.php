
<?PHP
exec('c:\WINDOWS\system32\cmd.exe /c START C:\xampp\htdocs\webpy\web.bat');

function Redirect($url, $permanent = false)
{
    header('Location: ' . $url, true, $permanent ? 301 : 302);

    exit();
}

Redirect('http://localhost/webpy/webpy.php', false);
?>
 