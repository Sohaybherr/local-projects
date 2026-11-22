<?php
include("data.php");

$c = isset($_GET["code"]) ? $_GET["code"] : "";
$etudiant = getDetailEtudiant($c);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Détail Etudiant</title>
</head>
<body>
    <h2>Détail de l'étudiant</h2>

    <?php if ($etudiant) { ?>
        <table border="1" cellpadding="8" cellspacing="0">
            <tr>
                <th>Code</th>
                <td><?php echo $etudiant["CodeE"]; ?></td>
            </tr>
            <tr>
                <th>Nom</th>
                <td><?php echo $etudiant["Nom"]; ?></td>
            </tr>
            <tr>
                <th>Prénom</th>
                <td><?php echo $etudiant["Prenom"]; ?></td>
            </tr>
            <tr>
                <th>Filière</th>
                <td><?php echo $etudiant["Filiere"]; ?></td>
            </tr>
            <tr>
                <th>Note</th>
                <td><?php echo $etudiant["Note"]; ?></td>
            </tr>
        </table>
    <?php } else { ?>
        <p>Etudiant introuvable.</p>
    <?php } ?>
</body>
</html>