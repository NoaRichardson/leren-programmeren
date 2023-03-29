<?php
if (isset($_POST["nr"])){
    $getal = $_POST["nr"];
    if(is_numeric($getal)){
        for ($i = 1; $i <= 10; $i++){
            $ant = $getal * $i;
            echo('<br>');
            echo("$getal x $i = $ant"); 
        }
        echo'<a href="demo.php">Terug</a>';
    }else{
        echo "Geen getal gegeven";
        echo'<a href="demo.php">Terug</a>';
    } 
}else{
    ?>
    <form method="post">
        getal:<input name = "nr">
        <input type="submit">
    </form>
    <?php
}


