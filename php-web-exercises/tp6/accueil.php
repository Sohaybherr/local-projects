<?php
include("data.php");
$filieres = getListeFilieres();
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Accueil</title>
</head>
<body>
    <h2>Liste des filières</h2>

    <table border="1" cellpadding="8" cellspacing="0">
        <tr>
            <th>Code</th>
            <th>Intitulé</th>
        </tr>

        <?php foreach ($filieres as $f) { ?>
            <tr>
                <td><?php echo $f["CodeF"]; ?></td>
                <td>
                    <a href="listeEtudiants.php?code=<?php echo $f["CodeF"]; ?>">
                        <?php echo $f["IntituleF"]; ?>
                    </a>
                </td>
            </tr>
        <?php } ?>
    </table>
</body>
</html>