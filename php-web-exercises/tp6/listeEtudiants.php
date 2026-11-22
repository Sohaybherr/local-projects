<?php
include("data.php");

$codeF = isset($_GET["code"]) ? $_GET["code"] : "";
$etudiants = getListeEtudiants($codeF);
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Liste Etudiants</title>
</head>
<body>
    <h2>Liste des étudiants réussis - <?php echo getIntituleFiliere($codeF); ?></h2>

    <table border="1" cellpadding="8" cellspacing="0">
        <tr>
            <th>Code</th>
            <th>Nom</th>
            <th>Prénom</th>
            <th>Filière</th>
            <th>Note</th>
            <th>Actions</th>
        </tr>

        <?php foreach ($etudiants as $e) { ?>
            <tr>
                <td><?php echo $e["CodeE"]; ?></td>
                <td>
                    <a href="detail.php?code=<?php echo $e["CodeE"]; ?>">
                        <?php echo $e["Nom"]; ?>
                    </a>
                </td>
                <td><?php echo $e["Prenom"]; ?></td>
                <td><?php echo $e["Filiere"]; ?></td>
                <td><?php echo $e["Note"]; ?></td>
                <td>
                    <a href="supprimer.php?code=<?php echo $e["CodeE"]; ?>&filiere=<?php echo $e["Filiere"]; ?>">Supprimer</a>
                </td>
            </tr>
        <?php } ?>
    </table>

    <br>
    <a href="formAjout.php?filiere=<?php echo $codeF; ?>">Ajouter étudiant</a>
    <br><br>
    <a href="accueil.php">Retour accueil</a>
</body>
</html>