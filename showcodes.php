<?php # showcodes.php 
    echo '<br><br>';
    if ($_REQUEST['showcode'] != 1) {
        echo '<a href="'.$_SERVER['PHP_SELF'].'?showcode=1">global-showcode</a>';
    } else {
        $file = file_get_contents(basename($_SERVER['PHP_SELF']));
        echo '<textarea cols="100" rows="10" style="overflow:auto">';
        echo htmlspecialchars($file);
        echo "</textarea>";
    }
?>
