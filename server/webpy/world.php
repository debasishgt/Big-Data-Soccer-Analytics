
<?PHP
set_time_limit ( 9999999 );
exec('c:\WINDOWS\system32\cmd.exe /c START C:\xampp\htdocs\webpy\world.bat');

function Redirect($url, $permanent = false)
{
    header('Location: ' . $url, true, $permanent ? 301 : 302);

    exit();
}

Redirect('http://localhost/webpy/webpy.php', false);
?>
 